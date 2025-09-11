"""
Validation utilities for IntelliGrade
Provides comprehensive validation for assessments, questions, and user inputs
"""

import re
import json
import logging
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import uuid

logger = logging.getLogger(__name__)

class ValidationUtils:
    def __init__(self):
        # Valid question types
        self.valid_question_types = [
            'multiple_choice', 'multiple-choice', 'mc',
            'true_false', 'true-false', 'tf', 'boolean',
            'short_answer', 'short-answer', 'sa',
            'essay', 'long_answer', 'paragraph',
            'fill_blank', 'fill-blank', 'fill_in_blank'
        ]
        
        # Valid learning styles
        self.valid_learning_styles = ['visual', 'auditory', 'kinesthetic', 'reading_writing']
        
        # Grade boundaries
        self.grade_boundaries = {
            'A+': 97, 'A': 93, 'A-': 90,
            'B+': 87, 'B': 83, 'B-': 80,
            'C+': 77, 'C': 73, 'C-': 70,
            'D+': 67, 'D': 63, 'D-': 60,
            'F': 0
        }
    
    def validate_assessment_data(self, assessment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate complete assessment data structure"""
        
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        # Required fields
        required_fields = ['title', 'questions']
        for field in required_fields:
            if field not in assessment_data:
                validation_result['valid'] = False
                validation_result['errors'].append(f"Missing required field: {field}")
        
        # Validate title
        if 'title' in assessment_data:
            title_validation = self._validate_title(assessment_data['title'])
            if not title_validation['valid']:
                validation_result['errors'].extend(title_validation['errors'])
        
        # Validate questions
        if 'questions' in assessment_data:
            questions_validation = self._validate_questions(assessment_data['questions'])
            validation_result['errors'].extend(questions_validation['errors'])
            validation_result['warnings'].extend(questions_validation['warnings'])
            validation_result['suggestions'].extend(questions_validation['suggestions'])
            
            if not questions_validation['valid']:
                validation_result['valid'] = False
        
        # Validate optional fields
        optional_validations = [
            ('description', self._validate_description),
            ('instructions', self._validate_instructions),
            ('time_limit', self._validate_time_limit),
            ('settings', self._validate_settings)
        ]
        
        for field, validator in optional_validations:
            if field in assessment_data:
                field_validation = validator(assessment_data[field])
                validation_result['warnings'].extend(field_validation.get('warnings', []))
                validation_result['suggestions'].extend(field_validation.get('suggestions', []))
        
        return validation_result
    
    def validate_question(self, question: Dict[str, Any], question_number: int = None) -> Dict[str, Any]:
        """Validate a single question"""
        
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        question_ref = f"Question {question_number}" if question_number else "Question"
        
        # Required fields
        if 'question' not in question or not question.get('question', '').strip():
            validation_result['valid'] = False
            validation_result['errors'].append(f"{question_ref}: Missing question text")
        
        # Validate question text
        if 'question' in question:
            text_validation = self._validate_question_text(question['question'])
            if not text_validation['valid']:
                validation_result['errors'].extend([f"{question_ref}: {error}" for error in text_validation['errors']])
            validation_result['warnings'].extend([f"{question_ref}: {warning}" for warning in text_validation['warnings']])
        
        # Validate question type
        question_type = question.get('type', 'short_answer').lower()
        if question_type not in self.valid_question_types:
            validation_result['warnings'].append(f"{question_ref}: Unknown question type '{question_type}', defaulting to 'short_answer'")
        
        # Type-specific validation
        type_validation = self._validate_question_by_type(question, question_type, question_ref)
        validation_result['errors'].extend(type_validation['errors'])
        validation_result['warnings'].extend(type_validation['warnings'])
        validation_result['suggestions'].extend(type_validation['suggestions'])
        
        if not type_validation['valid']:
            validation_result['valid'] = False
        
        # Validate points
        points_validation = self._validate_points(question.get('points', 1), question_ref)
        validation_result['errors'].extend(points_validation['errors'])
        validation_result['warnings'].extend(points_validation['warnings'])
        
        return validation_result
    
    def validate_student_answers(self, answers: List[str], questions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate student answers against questions"""
        
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Check answer count matches question count
        if len(answers) != len(questions):
            validation_result['valid'] = False
            validation_result['errors'].append(f"Answer count ({len(answers)}) does not match question count ({len(questions)})")
            return validation_result
        
        # Validate each answer
        for i, (answer, question) in enumerate(zip(answers, questions)):
            answer_validation = self._validate_single_answer(answer, question, i + 1)
            validation_result['warnings'].extend(answer_validation['warnings'])
        
        return validation_result
    
    def validate_grading_result(self, grading_result: Dict[str, Any]) -> Dict[str, Any]:
        """Validate AI grading result structure"""
        
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Required fields
        required_fields = [
            'total_points_possible', 'total_points_earned', 'percentage',
            'letter_grade', 'question_results'
        ]
        
        for field in required_fields:
            if field not in grading_result:
                validation_result['valid'] = False
                validation_result['errors'].append(f"Missing required field in grading result: {field}")
        
        # Validate percentage
        if 'percentage' in grading_result:
            percentage = grading_result['percentage']
            if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
                validation_result['valid'] = False
                validation_result['errors'].append("Percentage must be a number between 0 and 100")
        
        # Validate letter grade
        if 'letter_grade' in grading_result:
            letter_grade = grading_result['letter_grade']
            if letter_grade not in self.grade_boundaries:
                validation_result['warnings'].append(f"Unusual letter grade: {letter_grade}")
        
        # Validate question results
        if 'question_results' in grading_result:
            for i, q_result in enumerate(grading_result['question_results']):
                q_validation = self._validate_question_result(q_result, i + 1)
                validation_result['errors'].extend(q_validation['errors'])
                validation_result['warnings'].extend(q_validation['warnings'])
        
        # Validate point totals match
        if all(field in grading_result for field in ['total_points_possible', 'total_points_earned', 'question_results']):
            calculated_possible = sum(q.get('points_possible', 0) for q in grading_result['question_results'])
            calculated_earned = sum(q.get('points_earned', 0) for q in grading_result['question_results'])
            
            if calculated_possible != grading_result['total_points_possible']:
                validation_result['errors'].append("Total points possible doesn't match sum of question points")
            
            if abs(calculated_earned - grading_result['total_points_earned']) > 0.01:  # Allow small floating point differences
                validation_result['errors'].append("Total points earned doesn't match sum of question points")
        
        return validation_result
    
    def sanitize_input(self, input_data: Union[str, Dict, List]) -> Union[str, Dict, List]:
        """Sanitize user input to prevent injection attacks"""
        
        if isinstance(input_data, str):
            # Remove potentially harmful characters and limit length
            sanitized = re.sub(r'[<>{}]', '', input_data)
            return sanitized[:5000]  # Limit length
        
        elif isinstance(input_data, dict):
            return {key: self.sanitize_input(value) for key, value in input_data.items()}
        
        elif isinstance(input_data, list):
            return [self.sanitize_input(item) for item in input_data]
        
        return input_data
    
    def _validate_title(self, title: str) -> Dict[str, Any]:
        """Validate assessment title"""
        
        result = {'valid': True, 'errors': []}
        
        if not title or not title.strip():
            result['valid'] = False
            result['errors'].append("Title cannot be empty")
        elif len(title.strip()) < 3:
            result['valid'] = False
            result['errors'].append("Title must be at least 3 characters long")
        elif len(title) > 200:
            result['valid'] = False
            result['errors'].append("Title cannot exceed 200 characters")
        
        return result
    
    def _validate_description(self, description: str) -> Dict[str, Any]:
        """Validate assessment description"""
        
        result = {'warnings': [], 'suggestions': []}
        
        if description and len(description) > 1000:
            result['warnings'].append("Description is very long (over 1000 characters)")
        
        if not description or len(description.strip()) < 10:
            result['suggestions'].append("Consider adding a detailed description to help students understand the assessment")
        
        return result
    
    def _validate_instructions(self, instructions: str) -> Dict[str, Any]:
        """Validate assessment instructions"""
        
        result = {'warnings': [], 'suggestions': []}
        
        if not instructions or len(instructions.strip()) < 20:
            result['suggestions'].append("Consider adding detailed instructions for students")
        
        return result
    
    def _validate_time_limit(self, time_limit: Any) -> Dict[str, Any]:
        """Validate time limit"""
        
        result = {'warnings': []}
        
        if time_limit is not None:
            if not isinstance(time_limit, (int, float)) or time_limit <= 0:
                result['warnings'].append("Time limit should be a positive number (in minutes)")
            elif time_limit > 480:  # 8 hours
                result['warnings'].append("Time limit seems unusually long (over 8 hours)")
        
        return result
    
    def _validate_settings(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        """Validate assessment settings"""
        
        result = {'warnings': [], 'suggestions': []}
        
        if not isinstance(settings, dict):
            result['warnings'].append("Settings should be a dictionary")
            return result
        
        # Validate specific settings
        if 'shuffle_questions' in settings and not isinstance(settings['shuffle_questions'], bool):
            result['warnings'].append("shuffle_questions should be a boolean value")
        
        if 'allow_backtrack' in settings and not isinstance(settings['allow_backtrack'], bool):
            result['warnings'].append("allow_backtrack should be a boolean value")
        
        return result
    
    def _validate_questions(self, questions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate questions array"""
        
        result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        if not isinstance(questions, list):
            result['valid'] = False
            result['errors'].append("Questions must be provided as a list")
            return result
        
        if not questions:
            result['valid'] = False
            result['errors'].append("Assessment must contain at least one question")
            return result
        
        if len(questions) > 200:
            result['warnings'].append("Assessment has many questions (over 200), consider splitting into multiple assessments")
        
        # Validate each question
        for i, question in enumerate(questions):
            q_validation = self.validate_question(question, i + 1)
            result['errors'].extend(q_validation['errors'])
            result['warnings'].extend(q_validation['warnings'])
            result['suggestions'].extend(q_validation['suggestions'])
            
            if not q_validation['valid']:
                result['valid'] = False
        
        return result
    
    def _validate_question_text(self, text: str) -> Dict[str, Any]:
        """Validate question text"""
        
        result = {'valid': True, 'errors': [], 'warnings': []}
        
        if not text or not text.strip():
            result['valid'] = False
            result['errors'].append("Question text cannot be empty")
        elif len(text.strip()) < 5:
            result['valid'] = False
            result['errors'].append("Question text is too short (minimum 5 characters)")
        elif len(text) > 2000:
            result['warnings'].append("Question text is very long (over 2000 characters)")
        
        # Check for question mark
        if text and not text.strip().endswith('?') and 'choose' not in text.lower() and 'select' not in text.lower():
            result['warnings'].append("Question might be missing a question mark")
        
        return result
    
    def _validate_question_by_type(self, question: Dict[str, Any], question_type: str, question_ref: str) -> Dict[str, Any]:
        """Validate question based on its type"""
        
        result = {'valid': True, 'errors': [], 'warnings': [], 'suggestions': []}
        
        if question_type in ['multiple_choice', 'multiple-choice', 'mc']:
            return self._validate_multiple_choice(question, question_ref)
        elif question_type in ['true_false', 'true-false', 'tf', 'boolean']:
            return self._validate_true_false(question, question_ref)
        elif question_type in ['fill_blank', 'fill-blank', 'fill_in_blank']:
            return self._validate_fill_blank(question, question_ref)
        elif question_type in ['essay', 'long_answer', 'paragraph']:
            return self._validate_essay(question, question_ref)
        else:  # short_answer and others
            return self._validate_short_answer(question, question_ref)
    
    def _validate_multiple_choice(self, question: Dict[str, Any], question_ref: str) -> Dict[str, Any]:
        """Validate multiple choice question"""
        
        result = {'valid': True, 'errors': [], 'warnings': [], 'suggestions': []}
        
        # Check for choices
        if 'choices' not in question:
            result['valid'] = False
            result['errors'].append(f"{question_ref}: Multiple choice questions must have choices")
        else:
            choices = question['choices']
            if not isinstance(choices, list):
                result['valid'] = False
                result['errors'].append(f"{question_ref}: Choices must be a list")
            elif len(choices) < 2:
                result['valid'] = False
                result['errors'].append(f"{question_ref}: Multiple choice questions need at least 2 choices")
            elif len(choices) > 10:
                result['warnings'].append(f"{question_ref}: Many choices (over 10), consider reducing")
            
            # Validate individual choices
            if isinstance(choices, list):
                for i, choice in enumerate(choices):
                    if not choice or not str(choice).strip():
                        result['errors'].append(f"{question_ref}: Choice {i+1} cannot be empty")
        
        # Check for correct answer
        if 'correct_answer' not in question:
            result['errors'].append(f"{question_ref}: Multiple choice questions must specify correct_answer")
        else:
            correct_answer = str(question['correct_answer']).strip().upper()
            if len(correct_answer) != 1 or not correct_answer.isalpha():
                result['warnings'].append(f"{question_ref}: Correct answer should be a single letter (A, B, C, etc.)")
        
        return result
    
    def _validate_true_false(self, question: Dict[str, Any], question_ref: str) -> Dict[str, Any]:
        """Validate true/false question"""
        
        result = {'valid': True, 'errors': [], 'warnings': [], 'suggestions': []}