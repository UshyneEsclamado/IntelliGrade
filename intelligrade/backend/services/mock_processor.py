# Simple test service to verify backend functionality
from typing import Dict, Any
import json
import asyncio
from datetime import datetime

class MockAssessmentProcessor:
    """
    Simple test processor that simulates AI grading for testing
    Replace this with your real AI services once backend is connected
    """
    
    @staticmethod
    async def process_assessment(file_content: str, assessment_type: str, total_points: int) -> Dict[str, Any]:
        """
        Mock processing function - replace with real AI processing
        """
        # Simulate processing delay
        await asyncio.sleep(1)
        
        # Mock results based on assessment type
        if assessment_type == "multiple-choice":
            mock_questions = 10
            correct_answers = 8
        elif assessment_type == "true-false":
            mock_questions = 15
            correct_answers = 12
        else:  # mixed
            mock_questions = 12
            correct_answers = 10
        
        percentage = round((correct_answers / mock_questions) * 100)
        points_earned = round((percentage / 100) * total_points)
        
        return {
            "studentName": "Test Student",  # Will be replaced by real extraction
            "assessmentTitle": "Test Assessment",  # Will be replaced by real extraction
            "percentage": percentage,
            "pointsEarned": points_earned,
            "totalPoints": total_points,
            "feedback": {
                "strengths": [
                    f"Good performance on {assessment_type} questions",
                    "Shows understanding of core concepts",
                    "Consistent answering pattern"
                ],
                "weaknesses": [
                    "Some conceptual gaps identified",
                    "Could improve on complex questions",
                    "Review needed in specific areas"
                ],
                "recommendations": [
                    f"Practice more {assessment_type} questions",
                    "Review missed concepts thoroughly",
                    "Focus on areas with lower scores"
                ],
                "detailedAnalysis": f"The student shows good foundational knowledge in this {assessment_type} assessment with {percentage}% accuracy."
            },
            "questionBreakdown": [
                {"isCorrect": True, "pointsEarned": 5, "pointsPossible": 5, "feedback": "Excellent work on this question."},
                {"isCorrect": False, "pointsEarned": 2, "pointsPossible": 5, "feedback": "Review this concept for better understanding."},
                {"isCorrect": True, "pointsEarned": 5, "pointsPossible": 5, "feedback": "Perfect answer with good reasoning."},
                {"isCorrect": False, "pointsEarned": 0, "pointsPossible": 5, "feedback": "This needs more attention. Study the related material."}
            ]
        }
    
    @staticmethod
    def extract_student_name(content: str) -> str:
        """
        Extract student name from file content
        TODO: Implement real name extraction logic
        """
        # Simple mock - look for "Name:" pattern
        lines = content.split('\n')
        for line in lines:
            if 'name:' in line.lower():
                return line.split(':', 1)[1].strip()
        return "Student Name Not Found"
    
    @staticmethod 
    def extract_assessment_title(content: str) -> str:
        """
        Extract assessment title from file content
        TODO: Implement real title extraction logic
        """
        # Simple mock - use first line or look for "Title:" pattern
        lines = content.split('\n')
        for line in lines:
            if 'title:' in line.lower():
                return line.split(':', 1)[1].strip()
        # Fallback to first non-empty line
        for line in lines:
            if line.strip():
                return line.strip()[:50]  # First 50 chars
        return "Assessment Title Not Found"