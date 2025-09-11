"""
File Processing Module for IntelliGrade
Handles various file formats for assessment uploads
"""

import os
import json
import csv
import pandas as pd
from typing import Dict, List, Any, Optional
import docx
import PyPDF2
import logging
from pathlib import Path
import re
from config import settings

logger = logging.getLogger(__name__)

class FileProcessor:
    def __init__(self):
        self.upload_dir = Path(settings.upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        
        # Supported file extensions
        self.supported_extensions = settings.allowed_extensions_list
        
        # Question type patterns
        self.question_patterns = {
            'multiple_choice': [r'a\)', r'b\)', r'c\)', r'd\)', r'A\)', r'B\)', r'C\)', r'D\)'],
            'true_false': [r'true.*false', r'T.*F', r'correct.*incorrect'],
            'fill_blank': [r'_+', r'\[.*\]', r'\{.*\}']
        }
    
    async def process_uploaded_file(self, file_path: str, file_type: str = None) -> Dict[str, Any]:
        """
        Process an uploaded assessment file
        """
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            # Determine file type from extension
            extension = file_path.suffix.lower()
            
            if extension == '.json':
                return await self._process_json_file(file_path)
            elif extension == '.csv':
                return await self._process_csv_file(file_path)
            elif extension == '.txt':
                return await self._process_text_file(file_path)
            elif extension == '.docx':
                return await self._process_docx_file(file_path)
            elif extension == '.pdf':
                return await self._process_pdf_file(file_path)
            else:
                raise ValueError(f"Unsupported file type: {extension}")
                
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {str(e)}")
            raise
    
    async def _process_json_file(self, file_path: Path) -> Dict[str, Any]:
        """Process JSON assessment file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validate JSON structure
            if 'questions' not in data:
                raise ValueError("JSON file must contain 'questions' array")
            
            # Process questions
            questions = []
            for i, q in enumerate(data['questions']):
                processed_q = self._process_question(q, i + 1)
                questions.append(processed_q)
            
            assessment_data = {
                'title': data.get('title', f'Assessment from {file_path.name}'),
                'description': data.get('description', ''),
                'instructions': data.get('instructions', ''),
                'questions': questions,
                'total_points': sum(q.get('points', 1) for q in questions),
                'time_limit': data.get('time_limit'),
                'settings': data.get('settings', {}),
                'source_file': str(file_path.name),
                'file_type': 'json'
            }
            
            return assessment_data
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error processing JSON file: {str(e)}")
    
    async def _process_csv_file(self, file_path: Path) -> Dict[str, Any]:
        """Process CSV assessment file"""
        try:
            # Try different encodings
            encodings = ['utf-8', 'latin1', 'cp1252']
            df = None
            
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    break
                except UnicodeDecodeError:
                    continue
            
            if df is None:
                raise ValueError("Could not read CSV file with supported encodings")
            
            # Expected columns: question, type, correct_answer, choices, points, rubric
            required_cols = ['question']
            if not all(col in df.columns for col in required_cols):
                raise ValueError(f"CSV must contain columns: {required_cols}")
            
            questions = []
            for i, row in df.iterrows():
                question_data = {
                    'question': str(row['question']).strip(),
                    'type': str(row.get('type', 'short_answer')).lower(),
                    'points': int(row.get('points', 1)) if pd.notna(row.get('points')) else 1
                }
                
                # Add optional fields
                if pd.notna(row.get('correct_answer')):
                    question_data['correct_answer'] = str(row['correct_answer']).strip()
                
                if pd.notna(row.get('choices')):
                    # Parse choices (comma-separated or JSON)
                    choices_str = str(row['choices'])
                    try:
                        question_data['choices'] = json.loads(choices_str)
                    except:
                        question_data['choices'] = [c.strip() for c in choices_str.split(',')]
                
                if pd.notna(row.get('rubric')):
                    question_data['rubric'] = str(row['rubric'])
                
                processed_q = self._process_question(question_data, i + 1)
                questions.append(processed_q)
            
            assessment_data = {
                'title': f'Assessment from {file_path.name}',
                'description': f'Imported from CSV file: {file_path.name}',
                'instructions': 'Answer all questions to the best of your ability.',
                'questions': questions,
                'total_points': sum(q.get('points', 1) for q in questions),
                'source_file': str(file_path.name),
                'file_type': 'csv'
            }
            
            return assessment_data
            
        except Exception as e:
            raise ValueError(f"Error processing CSV file: {str(e)}")
    
    async def _process_text_file(self, file_path: Path) -> Dict[str, Any]:
        """Process plain text assessment file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse questions from text
            questions = self._parse_text_questions(content)
            
            if not questions:
                raise ValueError("No questions found in text file")
            
            assessment_data = {
                'title': f'Assessment from {file_path.name}',
                'description': f'Imported from text file: {file_path.name}',
                'instructions': 'Answer all questions to the best of your ability.',
                'questions': questions,
                'total_points': sum(q.get('points', 1) for q in questions),
                'source_file': str(file_path.name),
                'file_type': 'text'
            }
            
            return assessment_data
            
        except Exception as e:
            raise ValueError(f"Error processing text file: {str(e)}")
    
    async def _process_docx_file(self, file_path: Path) -> Dict[str, Any]:
        """Process Word document assessment file"""
        try:
            doc = docx.Document(file_path)
            
            # Extract text from all paragraphs
            content = ""
            for paragraph in doc.paragraphs:
                content += paragraph.text + "\n"
            
            # Parse questions from text
            questions = self._parse_text_questions(content)
            
            if not questions:
                raise ValueError("No questions found in Word document")
            
            assessment_data = {
                'title': f'Assessment from {file_path.name}',
                'description': f'Imported from Word document: {file_path.name}',
                'instructions': 'Answer all questions to the best of your ability.',
                'questions': questions,
                'total_points': sum(q.get('points', 1) for q in questions),
                'source_file': str(file_path.name),
                'file_type': 'docx'
            }
            
            return assessment_data
            
        except Exception as e:
            raise ValueError(f"Error processing Word document: {str(e)}")
    
    async def _process_pdf_file(self, file_path: Path) -> Dict[str, Any]:
        """Process PDF assessment file"""
        try:
            content = ""
            
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                
                for page in pdf_reader.pages:
                    content += page.extract_text() + "\n"
            
            # Parse questions from text
            questions = self._parse_text_questions(content)
            
            if not questions:
                raise ValueError("No questions found in PDF document")
            
            assessment_data = {
                'title': f'Assessment from {file_path.name}',
                'description': f'Imported from PDF document: {file_path.name}',
                'instructions': 'Answer all questions to the best of your ability.',
                'questions': questions,
                'total_points': sum(q.get('points', 1) for q in questions),
                'source_file': str(file_path.name),
                'file_type': 'pdf'
            }
            
            return assessment_data
            
        except Exception as e:
            raise ValueError(f"Error processing PDF file: {str(e)}")
    
    def _parse_text_questions(self, content: str) -> List[Dict[str, Any]]:
        """Parse questions from plain text content"""
        questions = []
        
        # Split content by question markers
        question_markers = [r'\d+\.', r'Q\d+', r'Question \d+', r'\(\d+\)']
        
        # Try different splitting patterns
        for pattern in question_markers:
            parts = re.split(f'({pattern})', content, flags=re.IGNORECASE)
            
            if len(parts) > 2:  # Found questions
                for i in range(1, len(parts), 2):
                    if i + 1 < len(parts):
                        question_text = parts[i + 1].strip()
                        
                        if question_text:
                            question = self._parse_single_text_question(question_text, len(questions) + 1)
                            questions.append(question)
                break
        
        # If no numbered questions found, try paragraph splitting
        if not questions:
            paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
            
            for i, para in enumerate(paragraphs):
                if '?' in para:  # Likely a question
                    question = self._parse_single_text_question(para, i + 1)
                    questions.append(question)
        
        return questions
    
    def _parse_single_text_question(self, text: str, question_num: int) -> Dict[str, Any]:
        """Parse a single question from text"""
        
        # Clean the text
        text = text.strip()
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            return {
                'question': f'Question {question_num}',
                'type': 'short_answer',
                'points': 1
            }
        
        question_text = lines[0]
        
        # Determine question type based on patterns
        question_type = self._detect_question_type(text)
        
        question_data = {
            'question': question_text,
            'type': question_type,
            'points': 1
        }
        
        # Extract additional information based on type
        if question_type == 'multiple_choice':
            choices = []
            for line in lines[1:]:
                if re.match(r'^[A-Da-d]\)', line):
                    choices.append(line[2:].strip())
            if choices:
                question_data['choices'] = choices
        
        elif question_type == 'true_false':
            # Look for answer key
            for line in lines:
                if 'answer:' in line.lower():
                    answer = line.split(':', 1)[1].strip().lower()
                    if answer in ['true', 'false', 't', 'f']:
                        question_data['correct_answer'] = 'true' if answer.startswith('t') else 'false'
        
        # Look for point values
        point_match = re.search(r'\((\d+)\s*points?\)', text, re.IGNORECASE)
        if point_match:
            question_data['points'] = int(point_match.group(1))
        
        return question_data
    
    def _detect_question_type(self, text: str) -> str:
        """Detect question type from text patterns"""
        
        text_lower = text.lower()
        
        # Multiple choice patterns
        mc_patterns = ['a)', 'b)', 'c)', 'd)', 'a.', 'b.', 'c.', 'd.']
        if any(pattern in text_lower for pattern in mc_patterns):
            return 'multiple_choice'
        
        # True/false patterns
        tf_patterns = ['true or false', 'true/false', 't/f', 'true false']
        if any(pattern in text_lower for pattern in tf_patterns):
            return 'true_false'
        
        # Fill in blank patterns
        if '_' in text or '[' in text and ']' in text:
            return 'fill_blank'
        
        # Essay patterns
        essay_keywords = ['explain', 'describe', 'analyze', 'discuss', 'compare', 'contrast', 'essay']
        if any(keyword in text_lower for keyword in essay_keywords):
            if len(text) > 100:  # Longer questions likely essays
                return 'essay'
        
        # Default to short answer
        return 'short_answer'
    
    def _process_question(self, question_data: Dict, question_num: int) -> Dict[str, Any]:
        """Process and validate a single question"""
        
        processed = {
            'question_number': question_num,
            'question': question_data.get('question', '').strip(),
            'type': question_data.get('type', 'short_answer').lower(),
            'points': max(1, question_data.get('points', 1))
        }
        
        # Add type-specific fields
        if processed['type'] in ['multiple_choice', 'multiple-choice']:
            processed['choices'] = question_data.get('choices', [])
            processed['correct_answer'] = question_data.get('correct_answer', '')
            
        elif processed['type'] in ['true_false', 'true-false']:
            correct_answer = str(question_data.get('correct_answer', '')).lower()
            if correct_answer not in ['true', 'false']:
                correct_answer = 'true'  # Default
            processed['correct_answer'] = correct_answer
            
        elif processed['type'] in ['fill_blank', 'fill-blank']:
            correct_answers = question_data.get('correct_answer', [])
            if isinstance(correct_answers, str):
                correct_answers = [correct_answers]
            processed['correct_answer'] = correct_answers
            
        else:
            # Short answer, essay, etc.
            processed['correct_answer'] = question_data.get('correct_answer', '')
        
        # Add optional fields
        if question_data.get('rubric'):
            processed['rubric'] = question_data['rubric']
        
        if question_data.get('explanation'):
            processed['explanation'] = question_data['explanation']
        
        return processed
    
    def validate_file(self, file_path: str, max_size: int = None) -> Dict[str, Any]:
        """Validate uploaded file"""
        
        file_path = Path(file_path)
        max_size = max_size or settings.max_file_size
        
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Check if file exists
        if not file_path.exists():
            validation_result['valid'] = False
            validation_result['errors'].append('File does not exist')
            return validation_result
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > max_size:
            validation_result['valid'] = False
            validation_result['errors'].append(f'File size ({file_size} bytes) exceeds maximum allowed size ({max_size} bytes)')
        
        # Check file extension
        extension = file_path.suffix.lower()
        if extension not in self.supported_extensions:
            validation_result['valid'] = False
            validation_result['errors'].append(f'File type {extension} is not supported. Supported types: {", ".join(self.supported_extensions)}')
        
        # Check if file is readable
        try:
            with open(file_path, 'rb') as f:
                f.read(1)  # Try to read first byte
        except PermissionError:
            validation_result['valid'] = False
            validation_result['errors'].append('File is not readable (permission denied)')
        except Exception as e:
            validation_result['valid'] = False
            validation_result['errors'].append(f'Error reading file: {str(e)}')
        
        return validation_result
    
    def save_uploaded_file(self, file_content: bytes, filename: str) -> str:
        """Save uploaded file to upload directory"""
        
        # Sanitize filename
        safe_filename = re.sub(r'[^\w\-_\.]', '_', filename)
        
        # Add timestamp to avoid conflicts
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        name, ext = os.path.splitext(safe_filename)
        unique_filename = f"{name}_{timestamp}{ext}"
        
        file_path = self.upload_dir / unique_filename
        
        # Save file
        with open(file_path, 'wb') as f:
            f.write(file_content)
        
        return str(file_path)
    
    def cleanup_old_files(self, days: int = 30):
        """Clean up old uploaded files"""
        
        import time
        cutoff_time = time.time() - (days * 24 * 60 * 60)
        
        deleted_count = 0
        for file_path in self.upload_dir.iterdir():
            if file_path.is_file() and file_path.stat().st_mtime < cutoff_time:
                try:
                    file_path.unlink()
                    deleted_count += 1
                    logger.info(f"Deleted old file: {file_path}")
                except Exception as e:
                    logger.error(f"Error deleting file {file_path}: {e}")
        
        logger.info(f"Cleanup completed. Deleted {deleted_count} old files.")
        return deleted_count

# Singleton instance
file_processor = FileProcessor()