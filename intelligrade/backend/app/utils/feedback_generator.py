"""
Feedback Generator for IntelliGrade
Generates personalized feedback for students based on their performance
"""

import openai
import json
import logging
from typing import Dict, List, Any, Optional
from config import settings

logger = logging.getLogger(__name__)

class FeedbackGenerator:
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=settings.openai_api_key)
        
        # Learning style templates
        self.learning_styles = {
            'visual': {
                'strengths': 'diagrams, charts, visual examples',
                'recommendations': 'use mind maps, flowcharts, and visual study aids'
            },
            'auditory': {
                'strengths': 'listening, discussion, verbal explanation',
                'recommendations': 'try reading aloud, group discussions, and audio recordings'
            },
            'kinesthetic': {
                'strengths': 'hands-on activities, practical examples',
                'recommendations': 'use practice exercises, real-world applications, and interactive learning'
            },
            'reading_writing': {
                'strengths': 'text-based learning, note-taking',
                'recommendations': 'focus on reading materials, written summaries, and detailed notes'
            }
        }
    
    async def generate_overall_feedback(self, 
                                      questions: List[Dict], 
                                      student_answers: List[str], 
                                      question_results: List[Dict],
                                      overall_percentage: float,
                                      student_id: int = None,
                                      learning_style: str = None) -> Dict[str, Any]:
        """Generate comprehensive feedback for entire assessment"""
        
        try:
            # Analyze performance patterns
            analysis = self._analyze_performance_patterns(question_results)
            
            # Generate personalized feedback using AI
            feedback_prompt = self._create_overall_feedback_prompt(
                questions, student_answers, question_results, 
                overall_percentage, analysis, learning_style
            )
            
            response = await self.client.chat.completions.create(
                model=settings.ai_model,
                messages=[
                    {"role": "system", "content": "You are an expert educational advisor providing personalized feedback to help students improve their learning."},
                    {"role": "user", "content": feedback_prompt}
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            ai_feedback = response.choices[0].message.content.strip()
            
            # Structure the feedback response
            feedback_data = {
                "overall_performance": {
                    "percentage": overall_percentage,
                    "letter_grade": self._calculate_letter_grade(overall_percentage),
                    "performance_level": self._get_performance_level(overall_percentage)
                },
                "strengths": analysis["strengths"],
                "areas_for_improvement": analysis["weaknesses"],
                "ai_feedback": ai_feedback,
                "study_recommendations": self._generate_study_recommendations(
                    analysis, learning_style or settings.default_learning_style
                ),
                "next_steps": self._generate_next_steps(analysis, overall_percentage),
                "performance_analysis": analysis,
                "generated_at": "now"  # Will be replaced with actual timestamp
            }
            
            return feedback_data
            
        except Exception as e:
            logger.error(f"Error generating overall feedback: {str(e)}")
            return self._fallback_feedback(overall_percentage)
    
    async def generate_question_feedback(self, 
                                       question: Dict, 
                                       student_answer: str,
                                       correct_answer: str,
                                       is_correct: bool,
                                       points_earned: int,
                                       points_possible: int) -> str:
        """Generate specific feedback for a single question"""
        
        try:
            feedback_prompt = f"""
Provide helpful, constructive feedback for this question response:

Question: {question.get('question', '')}
Question Type: {question.get('type', 'unknown')}
Student Answer: {student_answer}
Correct Answer: {correct_answer}
Points Earned: {points_earned}/{points_possible}

Feedback should be:
- Encouraging and constructive
- Specific about what was correct/incorrect
- Include a brief explanation of the correct answer
- Suggest how to improve for similar questions
- Keep it concise (2-3 sentences)

Feedback:
"""
            
            response = await self.client.chat.completions.create(
                model=settings.ai_model,
                messages=[
                    {"role": "system", "content": "You are a supportive teacher providing helpful feedback to students."},
                    {"role": "user", "content": feedback_prompt}
                ],
                temperature=0.6,
                max_tokens=200
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Error generating question feedback: {str(e)}")
            return self._fallback_question_feedback(is_correct, correct_answer)
    
    def _analyze_performance_patterns(self, question_results: List[Dict]) -> Dict[str, Any]:
        """Analyze patterns in student performance"""
        
        analysis = {
            "total_questions": len(question_results),
            "correct_answers": 0,
            "question_types_performance": {},
            "strengths": [],
            "weaknesses": [],
            "confidence_levels": [],
            "points_by_type": {}
        }
        
        # Analyze by question type
        for result in question_results:
            q_type = result.get('question_type', 'unknown')
            is_correct = result.get('is_correct', False)
            confidence = result.get('confidence', 0.0)
            points_earned = result.get('points_earned', 0)
            points_possible = result.get('points_possible', 1)
            
            if is_correct:
                analysis["correct_answers"] += 1
            
            analysis["confidence_levels"].append(confidence)
            
            # Track performance by question type
            if q_type not in analysis["question_types_performance"]:
                analysis["question_types_performance"][q_type] = {
                    "total": 0,
                    "correct": 0,
                    "points_earned": 0,
                    "points_possible": 0
                }
            
            analysis["question_types_performance"][q_type]["total"] += 1
            if is_correct:
                analysis["question_types_performance"][q_type]["correct"] += 1
            analysis["question_types_performance"][q_type]["points_earned"] += points_earned
            analysis["question_types_performance"][q_type]["points_possible"] += points_possible
        
        # Identify strengths and weaknesses
        for q_type, perf in analysis["question_types_performance"].items():
            if perf["total"] > 0:
                accuracy = perf["correct"] / perf["total"]
                percentage = (perf["points_earned"] / perf["points_possible"]) * 100 if perf["points_possible"] > 0 else 0
                
                if accuracy >= 0.8 or percentage >= 80:
                    analysis["strengths"].append({
                        "area": q_type.replace('_', ' ').title(),
                        "performance": f"{percentage:.0f}%",
                        "description": f"Strong performance in {q_type.replace('_', ' ')} questions"
                    })
                elif accuracy <= 0.5 or percentage <= 50:
                    analysis["weaknesses"].append({
                        "area": q_type.replace('_', ' ').title(),
                        "performance": f"{percentage:.0f}%",
                        "description": f"Needs improvement in {q_type.replace('_', ' ')} questions"
                    })
        
        # Overall confidence
        analysis["average_confidence"] = sum(analysis["confidence_levels"]) / len(analysis["confidence_levels"]) if analysis["confidence_levels"] else 0.0
        analysis["overall_accuracy"] = analysis["correct_answers"] / analysis["total_questions"] if analysis["total_questions"] > 0 else 0.0
        
        return analysis
    
    def _create_overall_feedback_prompt(self, 
                                      questions: List[Dict],
                                      student_answers: List[str],
                                      question_results: List[Dict],
                                      overall_percentage: float,
                                      analysis: Dict,
                                      learning_style: str = None) -> str:
        """Create prompt for overall feedback generation"""
        
        prompt = f"""
Generate personalized, encouraging feedback for a student's assessment performance:

PERFORMANCE SUMMARY:
- Overall Score: {overall_percentage:.1f}%
- Questions Answered: {analysis['total_questions']}
- Correct Answers: {analysis['correct_answers']}
- Overall Accuracy: {analysis['overall_accuracy']*100:.1f}%

PERFORMANCE BY QUESTION TYPE:
"""
        
        for q_type, perf in analysis["question_types_performance"].items():
            percentage = (perf["points_earned"] / perf["points_possible"]) * 100 if perf["points_possible"] > 0 else 0
            prompt += f"- {q_type.replace('_', ' ').title()}: {percentage:.0f}% ({perf['correct']}/{perf['total']})\n"
        
        if analysis["strengths"]:
            prompt += f"\nSTRENGTHS:\n"
            for strength in analysis["strengths"]:
                prompt += f"- {strength['description']}\n"
        
        if analysis["weaknesses"]:
            prompt += f"\nAREAS FOR IMPROVEMENT:\n"
            for weakness in analysis["weaknesses"]:
                prompt += f"- {weakness['description']}\n"
        
        if learning_style and learning_style in self.learning_styles:
            style_info = self.learning_styles[learning_style]
            prompt += f"\nLEARNING STYLE: {learning_style.replace('_', ' ').title()}\n"
            prompt += f"Strengths: {style_info['strengths']}\n"
        
        prompt += f"""

Please provide:
1. Encouraging opening statement about their performance
2. Specific praise for their strengths
3. Constructive guidance for improvement areas
4. Motivational closing with next steps

Keep the tone positive, specific, and actionable. Focus on growth and learning opportunities.
"""
        
        return prompt
    
    def _generate_study_recommendations(self, analysis: Dict, learning_style: str) -> List[Dict[str, str]]:
        """Generate personalized study recommendations"""
        
        recommendations = []
        
        # General recommendations based on performance
        if analysis["overall_accuracy"] < 0.6:
            recommendations.append({
                "category": "Review Fundamentals",
                "recommendation": "Focus on reviewing basic concepts and foundational material",
                "priority": "high"
            })
        
        # Specific recommendations based on weaknesses
        for weakness in analysis["weaknesses"]:
            area = weakness["area"].lower()
            if "multiple choice" in area:
                recommendations.append({
                    "category": "Multiple Choice Strategy",
                    "recommendation": "Practice elimination techniques and careful reading of all options",
                    "priority": "medium"
                })
            elif "essay" in area:
                recommendations.append({
                    "category": "Essay Writing",
                    "recommendation": "Work on organizing ideas clearly and providing specific examples",
                    "priority": "high"
                })
            elif "short answer" in area:
                recommendations.append({
                    "category": "Concept Understanding",
                    "recommendation": "Focus on understanding key concepts rather than memorization",
                    "priority": "medium"
                })
        
        # Learning style specific recommendations
        if learning_style in self.learning_styles:
            style_info = self.learning_styles[learning_style]
            recommendations.append({
                "category": f"For {learning_style.replace('_', ' ').title()} Learners",
                "recommendation": f"Try {style_info['recommendations']}",
                "priority": "medium"
            })
        
        return recommendations[:5]  # Limit to 5 recommendations
    
    def _generate_next_steps(self, analysis: Dict, overall_percentage: float) -> List[str]:
        """Generate specific next steps for the student"""
        
        next_steps = []
        
        if overall_percentage >= 90:
            next_steps.append("Excellent work! Consider helping peers or exploring advanced topics")
            next_steps.append("Review any missed questions to achieve perfect understanding")
        elif overall_percentage >= 80:
            next_steps.append("Great job! Focus on the areas where you lost points")
            next_steps.append("Practice similar questions to reinforce your understanding")
        elif overall_percentage >= 70:
            next_steps.append("Good effort! Review the concepts from questions you missed")
            next_steps.append("Seek additional practice in your weaker areas")
        elif overall_percentage >= 60:
            next_steps.append("Review the fundamental concepts covered in this assessment")
            next_steps.append("Consider meeting with your instructor for additional support")
        else:
            next_steps.append("Schedule a meeting with your instructor to discuss the material")
            next_steps.append("Focus on understanding basic concepts before moving forward")
        
        # Add specific steps based on weaknesses
        if len(analysis["weaknesses"]) > 0:
            next_steps.append(f"Pay special attention to {analysis['weaknesses'][0]['area'].lower()} concepts")
        
        return next_steps[:4]  # Limit to 4 next steps
    
    def _calculate_letter_grade(self, percentage: float) -> str:
        """Convert percentage to letter grade"""
        if percentage >= 97: return "A+"
        elif percentage >= 93: return "A"
        elif percentage >= 90: return "A-"
        elif percentage >= 87: return "B+"
        elif percentage >= 83: return "B"
        elif percentage >= 80: return "B-"
        elif percentage >= 77: return "C+"
        elif percentage >= 73: return "C"
        elif percentage >= 70: return "C-"
        elif percentage >= 67: return "D+"
        elif percentage >= 63: return "D"
        elif percentage >= 60: return "D-"
        else: return "F"
    
    def _get_performance_level(self, percentage: float) -> str:
        """Get performance level description"""
        if percentage >= 90: return "Excellent"
        elif percentage >= 80: return "Good"
        elif percentage >= 70: return "Satisfactory"
        elif percentage >= 60: return "Needs Improvement"
        else: return "Requires Attention"
    
    def _fallback_feedback(self, overall_percentage: float) -> Dict[str, Any]:
        """Fallback feedback when AI generation fails"""
        
        performance_level = self._get_performance_level(overall_percentage)
        
        return {
            "overall_performance": {
                "percentage": overall_percentage,
                "letter_grade": self._calculate_letter_grade(overall_percentage),
                "performance_level": performance_level
            },
            "ai_feedback": f"You achieved a {overall_percentage:.1f}% on this assessment. Keep working hard and don't hesitate to ask for help when needed!",
            "study_recommendations": [
                {
                    "category": "General Study",
                    "recommendation": "Review the material and practice similar questions",
                    "priority": "medium"
                }
            ],
            "next_steps": [
                "Review your incorrect answers",
                "Practice similar questions",
                "Seek help if needed"
            ]
        }
    
    def _fallback_question_feedback(self, is_correct: bool, correct_answer: str) -> str:
        """Fallback question feedback when AI generation fails"""
        
        if is_correct:
            return "Correct! Well done."
        else:
            return f"Incorrect. The correct answer is: {correct_answer}. Review this concept for better understanding."