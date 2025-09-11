"""
Enhanced AI Grading Engine - Production-ready grading system
Handles automatic grading using OpenAI GPT models with advanced features
"""

import openai
import json
import asyncio
import logging
from typing import Dict, List, Any, Optional, Tuple, Union
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from enum import Enum
import re
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import time
from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    SHORT_ANSWER = "short_answer"
    ESSAY = "essay"
    FILL_BLANK = "fill_blank"
    MATCHING = "matching"
    ORDERING = "ordering"

class GradingStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    NEEDS_REVIEW = "needs_review"

@dataclass
class GradingConfig:
    """Configuration for grading parameters"""
    api_key: str
    model: str = "gpt-4"
    temperature: float = 0.2
    max_tokens: int = 1000
    timeout: int = 30
    max_retries: int = 3
    batch_delay: float = 0.5
    manual_review_threshold: float = 0.7
    partial_credit_threshold: float = 0.3
    enable_caching: bool = True
    cache_ttl: int = 3600  # 1 hour

@dataclass
class QuestionResult:
    """Result of grading a single question"""
    question_id: str
    question_type: QuestionType
    student_answer: str
    correct_answer: Optional[str] = None
    points_possible: float = 1.0
    points_earned: float = 0.0
    percentage: float = 0.0
    is_correct: bool = False
    confidence: float = 0.0
    feedback: str = ""
    explanation: str = ""
    rubric_breakdown: Optional[Dict[str, float]] = None
    grading_time: float = 0.0
    needs_review: bool = False
    error_message: Optional[str] = None

@dataclass
class AssessmentResult:
    """Complete assessment grading result"""
    assessment_id: str
    student_id: str
    total_questions: int
    total_points_possible: float
    total_points_earned: float
    percentage: float
    letter_grade: str
    question_results: List[QuestionResult]
    overall_feedback: str
    ai_confidence: float
    needs_manual_review: bool
    grading_duration: float
    graded_at: datetime
    model_used: str
    status: GradingStatus

class GradingCache:
    """Simple in-memory cache for grading results"""
    
    def __init__(self, ttl: int = 3600):
        self._cache: Dict[str, Tuple[Any, datetime]] = {}
        self.ttl = ttl
    
    def _generate_key(self, question_text: str, student_answer: str, question_type: str) -> str:
        """Generate cache key from question and answer"""
        content = f"{question_text}|{student_answer}|{question_type}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def get(self, question_text: str, student_answer: str, question_type: str) -> Optional[Dict]:
        """Get cached result if available and not expired"""
        key = self._generate_key(question_text, student_answer, question_type)
        
        if key in self._cache:
            result, timestamp = self._cache[key]
            if datetime.utcnow() - timestamp < timedelta(seconds=self.ttl):
                logger.debug(f"Cache hit for question: {key[:8]}...")
                return result
            else:
                del self._cache[key]
        return None
    
    def set(self, question_text: str, student_answer: str, question_type: str, result: Dict):
        """Cache grading result"""
        key = self._generate_key(question_text, student_answer, question_type)
        self._cache[key] = (result, datetime.utcnow())
        logger.debug(f"Cached result for question: {key[:8]}...")
    
    def clear_expired(self):
        """Remove expired cache entries"""
        now = datetime.utcnow()
        expired_keys = [
            key for key, (_, timestamp) in self._cache.items()
            if now - timestamp >= timedelta(seconds=self.ttl)
        ]
        for key in expired_keys:
            del self._cache[key]

class RateLimiter:
    """Rate limiter for API calls"""
    
    def __init__(self, calls_per_minute: int = 20):
        self.calls_per_minute = calls_per_minute
        self.calls: List[float] = []
    
    async def wait_if_needed(self):
        """Wait if rate limit would be exceeded"""
        now = time.time()
        # Remove calls older than 1 minute
        self.calls = [call_time for call_time in self.calls if now - call_time < 60]
        
        if len(self.calls) >= self.calls_per_minute:
            wait_time = 60 - (now - self.calls[0]) + 1
            logger.info(f"Rate limit reached, waiting {wait_time:.1f} seconds")
            await asyncio.sleep(wait_time)
        
        self.calls.append(now)

class AIGradingEngine:
    """Enhanced AI grading engine with production features"""
    
    def __init__(self, config: GradingConfig):
        self.config = config
        self.client = openai.AsyncOpenAI(api_key=config.api_key)
        self.cache = GradingCache(config.cache_ttl) if config.enable_caching else None
        self.rate_limiter = RateLimiter()
        
        # Initialize grading prompts
        self.prompts = self._initialize_prompts()
        
        logger.info(f"AI Grading Engine initialized with model: {config.model}")
    
    async def grade_assessment(self, 
                             questions: List[Dict], 
                             student_answers: List[str],
                             student_id: str,
                             assessment_id: str,
                             progress_callback: Optional[callable] = None) -> AssessmentResult:
        """Grade a complete assessment with progress tracking"""
        
        start_time = time.time()
        logger.info(f"Starting assessment grading: {assessment_id} for student: {student_id}")
        
        if len(questions) != len(student_answers):
            raise ValueError(f"Mismatch: {len(questions)} questions, {len(student_answers)} answers")
        
        question_results = []
        total_points_possible = 0
        total_points_earned = 0
        
        try:
            # Grade each question
            for i, (question, answer) in enumerate(zip(questions, student_answers)):
                if progress_callback:
                    progress_callback(i, len(questions), f"Grading question {i+1}")
                
                result = await self._grade_single_question(question, answer, i + 1)
                question_results.append(result)
                
                total_points_possible += result.points_possible
                total_points_earned += result.points_earned
                
                # Rate limiting between questions
                if i < len(questions) - 1:
                    await asyncio.sleep(self.config.batch_delay)
            
            # Calculate overall metrics
            percentage = (total_points_earned / total_points_possible * 100) if total_points_possible > 0 else 0
            letter_grade = self._calculate_letter_grade(percentage)
            
            # Calculate average confidence
            confidences = [r.confidence for r in question_results if r.confidence > 0]
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0
            
            # Determine if manual review needed
            needs_review = (avg_confidence < self.config.manual_review_threshold or 
                          any(r.needs_review for r in question_results))
            
            # Generate overall feedback
            overall_feedback = await self._generate_overall_feedback(
                question_results, percentage, len(questions)
            )
            
            grading_duration = time.time() - start_time
            
            result = AssessmentResult(
                assessment_id=assessment_id,
                student_id=student_id,
                total_questions=len(questions),
                total_points_possible=total_points_possible,
                total_points_earned=total_points_earned,
                percentage=round(percentage, 2),
                letter_grade=letter_grade,
                question_results=question_results,
                overall_feedback=overall_feedback,
                ai_confidence=round(avg_confidence, 3),
                needs_manual_review=needs_review,
                grading_duration=grading_duration,
                graded_at=datetime.utcnow(),
                model_used=self.config.model,
                status=GradingStatus.COMPLETED
            )
            
            if progress_callback:
                progress_callback(len(questions), len(questions), "Grading completed")
            
            logger.info(f"Assessment graded successfully: {percentage:.1f}% in {grading_duration:.2f}s")
            return result
            
        except Exception as e:
            logger.error(f"Assessment grading failed: {str(e)}")
            # Return partial result if some questions were graded
            if question_results:
                return self._create_partial_result(
                    assessment_id, student_id, question_results, str(e), time.time() - start_time
                )
            raise
    
    async def _grade_single_question(self, question: Dict, answer: str, question_num: int) -> QuestionResult:
        """Grade a single question with comprehensive error handling"""
        
        start_time = time.time()
        question_id = str(question.get('id', question_num))
        question_type = self._parse_question_type(question.get('type', 'short_answer'))
        points_possible = float(question.get('points', 1))
        
        logger.debug(f"Grading Q{question_num}: {question_type.value}")
        
        try:
            # Check cache first
            if self.cache:
                cached_result = self.cache.get(
                    question.get('question', ''), answer, question_type.value
                )
                if cached_result:
                    cached_result['question_id'] = question_id
                    cached_result['grading_time'] = time.time() - start_time
                    return QuestionResult(**cached_result)
            
            # Grade based on question type
            if question_type == QuestionType.MULTIPLE_CHOICE:
                result = await self._grade_multiple_choice(question, answer, points_possible)
            elif question_type == QuestionType.TRUE_FALSE:
                result = await self._grade_true_false(question, answer, points_possible)
            elif question_type == QuestionType.FILL_BLANK:
                result = await self._grade_fill_blank(question, answer, points_possible)
            else:
                # Use AI for subjective questions
                result = await self._grade_with_ai(question, answer, points_possible, question_type)
            
            # Finalize result
            result.question_id = question_id
            result.question_type = question_type
            result.grading_time = time.time() - start_time
            result.percentage = (result.points_earned / result.points_possible * 100) if result.points_possible > 0 else 0
            result.is_correct = result.percentage >= 70  # Consider 70%+ as correct
            result.needs_review = result.confidence < self.config.manual_review_threshold
            
            # Cache result
            if self.cache and not result.error_message:
                self.cache.set(
                    question.get('question', ''), answer, question_type.value, asdict(result)
                )
            
            return result
            
        except Exception as e:
            logger.error(f"Error grading question {question_num}: {str(e)}")
            return QuestionResult(
                question_id=question_id,
                question_type=question_type,
                student_answer=answer,
                points_possible=points_possible,
                points_earned=0,
                confidence=0,
                feedback="An error occurred while grading this question.",
                explanation=f"Grading error: {str(e)}",
                grading_time=time.time() - start_time,
                needs_review=True,
                error_message=str(e)
            )
    
    async def _grade_multiple_choice(self, question: Dict, answer: str, points: float) -> QuestionResult:
        """Grade multiple choice with sophisticated matching"""
        
        correct_answer = str(question.get('correct_answer', '')).strip().upper()
        student_answer = str(answer).strip().upper()
        
        # Handle different answer formats (A, a, 1, "Option A", etc.)
        student_normalized = self._normalize_mc_answer(student_answer)
        correct_normalized = self._normalize_mc_answer(correct_answer)
        
        is_correct = student_normalized == correct_normalized
        points_earned = points if is_correct else 0
        
        # Generate detailed feedback
        choices = question.get('choices', [])
        explanation = f"The correct answer is {correct_answer}"
        if choices and correct_normalized:
            try:
                idx = ord(correct_normalized) - ord('A')
                if 0 <= idx < len(choices):
                    explanation += f": {choices[idx]}"
            except (ValueError, IndexError):
                pass
        
        feedback = "Correct! Well done." if is_correct else f"Incorrect. {explanation}"
        
        return QuestionResult(
            student_answer=answer,
            correct_answer=correct_answer,
            points_possible=points,
            points_earned=points_earned,
            confidence=0.95,
            feedback=feedback,
            explanation=explanation
        )
    
    async def _grade_true_false(self, question: Dict, answer: str, points: float) -> QuestionResult:
        """Grade true/false with flexible answer recognition"""
        
        correct_answer = str(question.get('correct_answer', '')).lower().strip()
        student_answer = str(answer).lower().strip()
        
        # Comprehensive answer normalization
        true_values = {'true', 't', 'yes', 'y', '1', 'correct', 'right'}
        false_values = {'false', 'f', 'no', 'n', '0', 'incorrect', 'wrong'}
        
        student_normalized = None
        if any(val in student_answer for val in true_values):
            student_normalized = 'true'
        elif any(val in student_answer for val in false_values):
            student_normalized = 'false'
        
        correct_normalized = None
        if any(val in correct_answer for val in true_values):
            correct_normalized = 'true'
        elif any(val in correct_answer for val in false_values):
            correct_normalized = 'false'
        
        if student_normalized is None or correct_normalized is None:
            return QuestionResult(
                student_answer=answer,
                correct_answer=correct_answer,
                points_possible=points,
                points_earned=0,
                confidence=0.5,
                feedback="Could not determine if your answer is true or false.",
                explanation="Please answer with 'True' or 'False'",
                needs_review=True
            )
        
        is_correct = student_normalized == correct_normalized
        points_earned = points if is_correct else 0
        
        feedback = f"Correct! The answer is {correct_normalized.title()}." if is_correct else \
                  f"Incorrect. The correct answer is {correct_normalized.title()}."
        
        return QuestionResult(
            student_answer=answer,
            correct_answer=correct_answer,
            points_possible=points,
            points_earned=points_earned,
            confidence=0.95,
            feedback=feedback,
            explanation=f"The statement is {correct_normalized}."
        )
    
    async def _grade_fill_blank(self, question: Dict, answer: str, points: float) -> QuestionResult:
        """Grade fill-in-blank with fuzzy matching"""
        
        correct_answers = question.get('correct_answer', [])
        if isinstance(correct_answers, str):
            correct_answers = [correct_answers]
        
        student_answer_clean = answer.strip().lower()
        
        # Check for exact matches
        for correct in correct_answers:
            if student_answer_clean == correct.strip().lower():
                return QuestionResult(
                    student_answer=answer,
                    correct_answer=correct,
                    points_possible=points,
                    points_earned=points,
                    confidence=0.95,
                    feedback="Correct!",
                    explanation=f"Your answer matches: {correct}"
                )
        
        # Check for partial matches (for partial credit)
        best_match_ratio = 0
        best_match = correct_answers[0] if correct_answers else ""
        
        for correct in correct_answers:
            ratio = self._calculate_similarity(student_answer_clean, correct.lower())
            if ratio > best_match_ratio:
                best_match_ratio = ratio
                best_match = correct
        
        # Award partial credit for close matches
        if best_match_ratio >= 0.8:
            partial_points = points * 0.8
            feedback = f"Close! Your answer is similar to the expected answer."
        elif best_match_ratio >= 0.6:
            partial_points = points * 0.5
            feedback = f"Partially correct. Your answer has some similarity to the expected answer."
        else:
            partial_points = 0
            feedback = f"Incorrect. Expected: {best_match}"
        
        return QuestionResult(
            student_answer=answer,
            correct_answer=best_match,
            points_possible=points,
            points_earned=partial_points,
            confidence=0.8,
            feedback=feedback,
            explanation=f"Expected answer: {best_match} (similarity: {best_match_ratio:.1%})"
        )
    
    async def _grade_with_ai(self, question: Dict, answer: str, points: float, question_type: QuestionType) -> QuestionResult:
        """Grade using AI with robust error handling and retries"""
        
        if not answer.strip():
            return QuestionResult(
                student_answer=answer,
                points_possible=points,
                points_earned=0,
                confidence=1.0,
                feedback="No answer provided.",
                explanation="Please provide an answer to receive credit."
            )
        
        prompt = self._build_prompt(question, answer, points, question_type)
        
        for attempt in range(self.config.max_retries):
            try:
                await self.rate_limiter.wait_if_needed()
                
                response = await asyncio.wait_for(
                    self.client.chat.completions.create(
                        model=self.config.model,
                        messages=[
                            {"role": "system", "content": self._get_system_prompt()},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=self.config.temperature,
                        max_tokens=self.config.max_tokens
                    ),
                    timeout=self.config.timeout
                )
                
                result = self._parse_ai_response(
                    response.choices[0].message.content, answer, points
                )
                
                return result
                
            except asyncio.TimeoutError:
                logger.warning(f"AI grading timeout (attempt {attempt + 1})")
                if attempt == self.config.max_retries - 1:
                    raise Exception("AI grading timed out after multiple attempts")
                
            except Exception as e:
                logger.warning(f"AI grading error (attempt {attempt + 1}): {str(e)}")
                if attempt == self.config.max_retries - 1:
                    return self._create_fallback_result(answer, points, str(e))
                
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
    
    def _parse_ai_response(self, response: str, student_answer: str, max_points: float) -> QuestionResult:
        """Parse AI response with multiple fallback strategies"""
        
        try:
            # Try to extract JSON
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                result_data = json.loads(json_match.group(0))
            else:
                result_data = json.loads(response)
            
            # Validate and clean data
            points_earned = max(0, min(max_points, float(result_data.get('points_earned', 0))))
            confidence = max(0.0, min(1.0, float(result_data.get('confidence', 0.7))))
            
            return QuestionResult(
                student_answer=student_answer,
                points_possible=max_points,
                points_earned=points_earned,
                confidence=confidence,
                feedback=result_data.get('feedback', 'AI grading completed'),
                explanation=result_data.get('explanation', result_data.get('ai_explanation', '')),
                rubric_breakdown=result_data.get('rubric_breakdown')
            )
            
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            logger.warning(f"Failed to parse AI response as JSON: {e}")
            return self._parse_text_response(response, student_answer, max_points)
    
    def _parse_text_response(self, response: str, student_answer: str, max_points: float) -> QuestionResult:
        """Fallback parsing for non-JSON responses"""
        
        # Extract numerical score
        score_patterns = [
            r'points?[:\s]*(\d+(?:\.\d+)?)',
            r'score[:\s]*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)[/\s]*(?:out of|of)\s*\d+'
        ]
        
        points_earned = 0
        for pattern in score_patterns:
            match = re.search(pattern, response.lower())
            if match:
                points_earned = min(max_points, float(match.group(1)))
                break
        
        # Extract confidence
        confidence_match = re.search(r'confidence[:\s]*(\d+(?:\.\d+)?)', response.lower())
        confidence = float(confidence_match.group(1)) if confidence_match else 0.7
        if confidence > 1.0:
            confidence = confidence / 100  # Convert percentage to decimal
        
        # Use first 300 characters as feedback
        feedback = response[:300] + "..." if len(response) > 300 else response
        
        return QuestionResult(
            student_answer=student_answer,
            points_possible=max_points,
            points_earned=points_earned,
            confidence=confidence,
            feedback=feedback,
            explanation="Parsed from AI response",
            needs_review=True
        )
    
    def _create_fallback_result(self, student_answer: str, points: float, error: str) -> QuestionResult:
        """Create fallback result when AI grading fails"""
        
        # Basic heuristics for emergency grading
        word_count = len(student_answer.split())
        
        if word_count >= 20:
            fallback_score = points * 0.6  # Give 60% for substantial attempt
            feedback = "Substantial answer provided. Manual review recommended."
        elif word_count >= 5:
            fallback_score = points * 0.4  # Give 40% for basic attempt
            feedback = "Basic answer provided. Manual review recommended."
        else:
            fallback_score = 0
            feedback = "Minimal answer provided."
        
        return QuestionResult(
            student_answer=student_answer,
            points_possible=points,
            points_earned=fallback_score,
            confidence=0.3,
            feedback=f"{feedback} (AI grading failed: {error})",
            explanation="Fallback grading applied due to technical issues",
            needs_review=True,
            error_message=error
        )
    
    async def _generate_overall_feedback(self, results: List[QuestionResult], percentage: float, total_questions: int) -> str:
        """Generate comprehensive overall feedback"""
        
        correct_count = sum(1 for r in results if r.is_correct)
        avg_confidence = sum(r.confidence for r in results) / len(results)
        
        feedback_parts = []
        
        # Performance summary
        if percentage >= 90:
            feedback_parts.append("Outstanding performance! You demonstrate excellent mastery of the material.")
        elif percentage >= 80:
            feedback_parts.append("Good work! You show solid understanding with room for minor improvements.")
        elif percentage >= 70:
            feedback_parts.append("Satisfactory performance. You understand the basics but should review key concepts.")
        elif percentage >= 60:
            feedback_parts.append("Below expectations. Significant review of the material is recommended.")
        else:
            feedback_parts.append("Substantial gaps in understanding. Please seek additional help and review thoroughly.")
        
        # Detailed breakdown
        feedback_parts.extend([
            f"\nPerformance Summary:",
            f"• Questions answered correctly: {correct_count}/{total_questions}",
            f"• Overall score: {percentage:.1f}%",
            f"• AI grading confidence: {avg_confidence:.1%}"
        ])
        
        # Question type analysis
        type_performance = {}
        for result in results:
            q_type = result.question_type.value
            if q_type not in type_performance:
                type_performance[q_type] = {'correct': 0, 'total': 0}
            type_performance[q_type]['total'] += 1
            if result.is_correct:
                type_performance[q_type]['correct'] += 1
        
        if len(type_performance) > 1:
            feedback_parts.append(f"\nPerformance by Question Type:")
            for q_type, stats in type_performance.items():
                pct = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
                feedback_parts.append(f"• {q_type.replace('_', ' ').title()}: {stats['correct']}/{stats['total']} ({pct:.0f}%)")
        
        # Study recommendations
        weak_areas = [r for r in results if not r.is_correct]
        if weak_areas:
            feedback_parts.append(f"\nRecommendations:")
            feedback_parts.append("• Review the questions you missed and understand the reasoning")
            feedback_parts.append("• Focus on concepts where you scored below 70%")
            if percentage < 70:
                feedback_parts.append("• Consider seeking additional help from your instructor")
                feedback_parts.append("• Form study groups to discuss challenging concepts")
        
        return "\n".join(feedback_parts)
    
    def _normalize_mc_answer(self, answer: str) -> str:
        """Normalize multiple choice answers to standard format"""
        if not answer:
            return ""
        
        answer = answer.strip().upper()
        
        # Extract letter from various formats
        letter_match = re.search(r'[A-Z]', answer)
        if letter_match:
            return letter_match.group(0)
        
        # Handle numeric answers (1->A, 2->B, etc.)
        number_match = re.search(r'\d+', answer)
        if number_match:
            num = int(number_match.group(0))
            if 1 <= num <= 26:
                return chr(ord('A') + num - 1)
        
        return answer
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity ratio between two strings"""
        if not text1 or not text2:
            return 0.0
        
        # Simple word-based similarity
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def _parse_question_type(self, type_str: str) -> QuestionType:
        """Parse question type from string"""
        type_mapping = {
            'multiple_choice': QuestionType.MULTIPLE_CHOICE,
            'multiple-choice': QuestionType.MULTIPLE_CHOICE,
            'mc': QuestionType.MULTIPLE_CHOICE,
            'true_false': QuestionType.TRUE_FALSE,
            'true-false': QuestionType.TRUE_FALSE,
            'tf': QuestionType.TRUE_FALSE,
            'boolean': QuestionType.TRUE_FALSE,
            'short_answer': QuestionType.SHORT_ANSWER,
            'short-answer': QuestionType.SHORT_ANSWER,
            'sa': QuestionType.SHORT_ANSWER,
            'essay': QuestionType.ESSAY,
            'long_answer': QuestionType.ESSAY,
            'paragraph': QuestionType.ESSAY,
            'fill_blank': QuestionType.FILL_BLANK,
            'fill-blank': QuestionType.FILL_BLANK,
            'fill_in_blank': QuestionType.FILL_BLANK
        }
        
        return type_mapping.get(type_str.lower(), QuestionType.SHORT_ANSWER)
    
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
    
    def _get_system_prompt(self) -> str:
        """Get system prompt for AI grading"""
        return """You are an expert teacher grading student work. Be fair, constructive, and detailed in your feedback.

Always respond with valid JSON in this format:
{
    "points_earned": [number between 0 and max points, can be decimal for partial credit],
    "confidence": [number between 0.0 and 1.0 indicating your confidence in this grade],
    "feedback": "[specific, constructive feedback for the student]",
    "explanation": "[detailed explanation of why you gave this score]",
    "rubric_breakdown": {optional object with criteria and scores}
}

Focus on being educational and constructive. Identify what the student did well and areas for improvement."""
    
    def _build_prompt(self, question: Dict, answer: str, points: float, question_type: QuestionType) -> str:
        """Build appropriate grading prompt based on question type"""
        
        base_info = f"""
Question: {question.get('question', '')}
Student Answer: {answer}
Points Possible: {points}
Question Type: {question_type.value}
"""
        
        if question_type == QuestionType.SHORT_ANSWER:
            return f"""{base_info}
Expected Answer/Key Points: {question.get('correct_answer', 'Use your expertise')}
Rubric: {question.get('rubric', 'Accuracy, completeness, clarity')}

Grade this short answer considering partial credit for partially correct responses.
Look for key concepts, accuracy, and understanding demonstrated."""
            
        elif question_type == QuestionType.ESSAY:
            return f"""{base_info}
Rubric: {question.get('rubric', 'Content knowledge (40%), Organization (30%), Clarity (20%), Evidence/Examples (10%)')}
Word Limit: {question.get('word_limit', 'No specific limit')}

Evaluate this essay response considering:
- Understanding of the topic and accuracy of content
- Logical organization and structure
- Clarity of writing and communication
- Use of relevant examples or evidence
- Grammar and mechanics (minor consideration)

Provide detailed feedback on strengths and areas for improvement."""
            
        else:  # Generic subjective question
            return f"""{base_info}
Expected Answer: {question.get('correct_answer', 'Use your expertise to evaluate')}

Grade this response considering the student's understanding, effort, and accuracy.
Provide specific feedback on what they did well and how they can improve."""
    
    def _initialize_prompts(self) -> Dict[str, str]:
        """Initialize prompt templates for different grading scenarios"""
        return {
            'retry_prompt': "The previous response was not in valid JSON format. Please provide the grading result in valid JSON only.",
            'fallback_prompt': "Please provide a simple numerical score and brief feedback for this answer.",
        }
    
    def _create_partial_result(self, assessment_id: str, student_id: str, 
                             question_results: List[QuestionResult], error: str, duration: float) -> AssessmentResult:
        """Create partial result when grading fails partway through"""
        
        total_possible = sum(r.points_possible for r in question_results)
        total_earned = sum(r.points_earned for r in question_results)
        percentage = (total_earned / total_possible * 100) if total_possible > 0 else 0
        
        return AssessmentResult(
            assessment_id=assessment_id,
            student_id=student_id,
            total_questions=len(question_results),
            total_points_possible=total_possible,
            total_points_earned=total_earned,
            percentage=percentage,
            letter_grade=self._calculate_letter_grade(percentage),
            question_results=question_results,
            overall_feedback=f"Partial grading completed. {len(question_results)} questions graded before error: {error}",
            ai_confidence=0.5,
            needs_manual_review=True,
            grading_duration=duration,
            graded_at=datetime.utcnow(),
            model_used=self.config.model,
            status=GradingStatus.FAILED
        )

# Utility functions and additional services

class BatchGradingService:
    """Service for processing multiple assessments efficiently"""
    
    def __init__(self, grading_engine: AIGradingEngine):
        self.engine = grading_engine
        self.active_jobs: Dict[str, Dict] = {}
    
    async def grade_batch(self, 
                         batch_id: str,
                         assessments: List[Dict],
                         progress_callback: Optional[callable] = None) -> Dict[str, Any]:
        """Grade multiple assessments in batch"""
        
        start_time = time.time()
        results = []
        successful = 0
        failed = 0
        
        self.active_jobs[batch_id] = {
            'status': 'in_progress',
            'total': len(assessments),
            'completed': 0,
            'started_at': datetime.utcnow()
        }
        
        try:
            for i, assessment_data in enumerate(assessments):
                try:
                    if progress_callback:
                        progress_callback(i, len(assessments), f"Processing assessment {i+1}")
                    
                    result = await self.engine.grade_assessment(
                        questions=assessment_data['questions'],
                        student_answers=assessment_data['answers'],
                        student_id=assessment_data['student_id'],
                        assessment_id=assessment_data['assessment_id']
                    )
                    
                    results.append({
                        'assessment_id': assessment_data['assessment_id'],
                        'student_id': assessment_data['student_id'],
                        'success': True,
                        'result': asdict(result)
                    })
                    successful += 1
                    
                except Exception as e:
                    logger.error(f"Failed to grade assessment {assessment_data.get('assessment_id')}: {e}")
                    results.append({
                        'assessment_id': assessment_data.get('assessment_id'),
                        'student_id': assessment_data.get('student_id'),
                        'success': False,
                        'error': str(e)
                    })
                    failed += 1
                
                self.active_jobs[batch_id]['completed'] = i + 1
                
                # Brief pause between assessments
                if i < len(assessments) - 1:
                    await asyncio.sleep(0.2)
            
            duration = time.time() - start_time
            
            self.active_jobs[batch_id].update({
                'status': 'completed',
                'completed_at': datetime.utcnow(),
                'duration': duration
            })
            
            return {
                'batch_id': batch_id,
                'total_assessments': len(assessments),
                'successful': successful,
                'failed': failed,
                'duration': duration,
                'results': results,
                'summary': {
                    'success_rate': successful / len(assessments) * 100 if assessments else 0,
                    'average_time_per_assessment': duration / len(assessments) if assessments else 0
                }
            }
            
        except Exception as e:
            self.active_jobs[batch_id]['status'] = 'failed'
            self.active_jobs[batch_id]['error'] = str(e)
            raise
    
    def get_batch_status(self, batch_id: str) -> Optional[Dict]:
        """Get status of a batch grading job"""
        return self.active_jobs.get(batch_id)

class GradingAnalytics:
    """Analytics service for grading performance and insights"""
    
    def __init__(self):
        self.grading_history: List[Dict] = []
    
    def record_grading(self, result: AssessmentResult):
        """Record grading result for analytics"""
        self.grading_history.append({
            'timestamp': result.graded_at,
            'assessment_id': result.assessment_id,
            'student_id': result.student_id,
            'percentage': result.percentage,
            'ai_confidence': result.ai_confidence,
            'needs_review': result.needs_manual_review,
            'duration': result.grading_duration,
            'model_used': result.model_used
        })
    
    def get_grading_stats(self, days: int = 30) -> Dict[str, Any]:
        """Get grading statistics for the last N days"""
        cutoff = datetime.utcnow() - timedelta(days=days)
        recent_gradings = [
            g for g in self.grading_history 
            if g['timestamp'] >= cutoff
        ]
        
        if not recent_gradings:
            return {'message': 'No grading data available'}
        
        percentages = [g['percentage'] for g in recent_gradings]
        confidences = [g['ai_confidence'] for g in recent_gradings]
        durations = [g['duration'] for g in recent_gradings]
        
        return {
            'period_days': days,
            'total_gradings': len(recent_gradings),
            'average_score': sum(percentages) / len(percentages),
            'average_confidence': sum(confidences) / len(confidences),
            'average_duration': sum(durations) / len(durations),
            'manual_review_rate': sum(1 for g in recent_gradings if g['needs_review']) / len(recent_gradings) * 100,
            'score_distribution': self._calculate_score_distribution(percentages),
            'model_usage': self._calculate_model_usage(recent_gradings)
        }
    
    def _calculate_score_distribution(self, scores: List[float]) -> Dict[str, int]:
        """Calculate score distribution by grade ranges"""
        distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        
        for score in scores:
            if score >= 90:
                distribution['A'] += 1
            elif score >= 80:
                distribution['B'] += 1
            elif score >= 70:
                distribution['C'] += 1
            elif score >= 60:
                distribution['D'] += 1
            else:
                distribution['F'] += 1
        
        return distribution
    
    def _calculate_model_usage(self, gradings: List[Dict]) -> Dict[str, int]:
        """Calculate usage statistics by model"""
        usage = {}
        for grading in gradings:
            model = grading.get('model_used', 'unknown')
            usage[model] = usage.get(model, 0) + 1
        return usage

# Factory function for easy initialization
def create_grading_engine(api_key: str, **kwargs) -> AIGradingEngine:
    """Factory function to create a configured grading engine"""
    
    config = GradingConfig(
        api_key=api_key,
        model=kwargs.get('model', 'gpt-4'),
        temperature=kwargs.get('temperature', 0.2),
        max_tokens=kwargs.get('max_tokens', 1000),
        timeout=kwargs.get('timeout', 30),
        max_retries=kwargs.get('max_retries', 3),
        batch_delay=kwargs.get('batch_delay', 0.5),
        manual_review_threshold=kwargs.get('manual_review_threshold', 0.7),
        enable_caching=kwargs.get('enable_caching', True),
        cache_ttl=kwargs.get('cache_ttl', 3600)
    )
    
    return AIGradingEngine(config)

# Example usage
if __name__ == "__main__":
    import asyncio
    import os
    
    async def example_usage():
        # Initialize grading engine
        engine = create_grading_engine(
            api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-4",
            enable_caching=True
        )
        
        # Example questions and answers
        questions = [
            {
                "id": 1,
                "type": "multiple_choice",
                "question": "What is the capital of France?",
                "correct_answer": "A",
                "choices": ["Paris", "London", "Berlin", "Madrid"],
                "points": 1
            },
            {
                "id": 2,
                "type": "short_answer",
                "question": "Explain the process of photosynthesis.",
                "correct_answer": "Photosynthesis is the process by which plants convert light energy into chemical energy using chlorophyll.",
                "points": 5
            }
        ]
        
        answers = ["A", "Photosynthesis is when plants make food from sunlight and carbon dioxide."]
        
        # Grade assessment
        try:
            result = await engine.grade_assessment(
                questions=questions,
                student_answers=answers,
                student_id="student_123",
                assessment_id="assessment_456"
            )
            
            print(f"Grading completed: {result.percentage}% ({result.letter_grade})")
            print(f"Needs review: {result.needs_manual_review}")
            
        except Exception as e:
            print(f"Grading failed: {e}")
    
    # Run example
    # asyncio.run(example_usage())