# routes/upload_assessments.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional
import json
import time
import re
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

# Import OpenAI properly
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    AI_ENABLED = bool(os.getenv("OPENAI_API_KEY"))
except ImportError:
    AI_ENABLED = False
    client = None

# Import database and models
from database import get_db
from models import AnswerKey, UploadedAssessment, GradingResult
from services.file_processing import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt

load_dotenv()

router = APIRouter()

# OpenAI configuration
OPENAI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"🤖 AI Status: {'ENABLED ✅' if AI_ENABLED else 'DISABLED ❌'}")
if AI_ENABLED:
    logger.info(f"📡 Using OpenAI Model: {OPENAI_MODEL}")


def parse_answer_from_line(line: str, line_num: int) -> dict:
    """
    Parse answer from a single line - SUPPORTS ALL FORMATS
    Returns dict with: {'answer': str, 'question_type': str, 'found': bool}
    """
    line_original = line.strip()
    line_upper = line.upper().strip()
    
    # Skip empty lines
    if not line_original:
        return {'answer': None, 'question_type': None, 'found': False}
    
    # SKIP PATTERNS - Lines that should be ignored
    skip_patterns = [
        r'^ANSWER[\s]*KEY',
        r'^ANSWERS?[\s]*:?',
        r'^QUESTION[\s]*\d*',
        r'^NAME[\s]*:',
        r'^DATE[\s]*:',
        r'^SUBJECT[\s]*:',
        r'^INSTRUCTIONS?',
        r'^DIRECTIONS?',
        r'^TOTAL[\s]*POINTS?',
        r'^POINTS?[\s]*:',
        r'^SECTION[\s]*\d*',
        r'^PART[\s]*\d*',
        r'^TRUE[\s]*OR[\s]*FALSE',
        r'^MULTIPLE[\s]*CHOICE',
        r'^CHOOSE[\s]*THE',
        r'^SELECT[\s]*THE',
    ]
    
    for pattern in skip_patterns:
        if re.match(pattern, line_upper):
            return {'answer': None, 'question_type': None, 'found': False}
    
    # === PATTERN 1: Answer at START with optional question number ===
    # Matches: "A", "A)", "A.", "A 1.", "T 8.", "F 9.", "True 5."
    match = re.match(r'^([A-E]|T|F|TRUE|FALSE)[\.\)\s]*(\d+)?', line_upper)
    if match:
        answer = match.group(1)
        # Normalize
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # === PATTERN 2: Number THEN answer ===
    # Matches: "1. A", "1) B", "1: True", "1 - False"
    match = re.match(r'^\d+[\.\)\:\-\s]+([A-E]|T|F|TRUE|FALSE)[\.\)\s]*$', line_upper)
    if match:
        answer = match.group(1)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # === PATTERN 3: Answer: or Ans: format ===
    # Matches: "Answer: A", "Ans: True", "Answer : B"
    match = re.match(r'^(ANSWER|ANS)[\s]*:[\s]*([A-E]|T|F|TRUE|FALSE)', line_upper)
    if match:
        answer = match.group(2)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # === PATTERN 4: Q prefix format ===
    # Matches: "Q1: A", "Q1. True", "Question 1: B"
    match = re.match(r'^Q(UESTION)?[\s]*\d+[\.\:\s]+([A-E]|T|F|TRUE|FALSE)', line_upper)
    if match:
        answer = match.group(2)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # === PATTERN 5: Question number at END ===
    # Matches: "A (1)", "True - 5", "B #8"
    match = re.search(r'^([A-E]|T|F|TRUE|FALSE)[\s\.\)\-]*[\(\#\-\s]*\d+', line_upper)
    if match:
        answer = match.group(1)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # No answer found
    return {'answer': None, 'question_type': None, 'found': False}


def normalize_answer(answer: str, question_type: str) -> str:
    """
    Normalize answers for comparison - CRITICAL FIX FOR SCORING
    Handles all variations of True/False and Multiple Choice answers
    """
    if not answer:
        return ''
    
    # Remove all whitespace and convert to uppercase
    answer = str(answer).strip().upper()
    
    # Handle True/False normalization
    if question_type == 'true-false':
        # All variations of TRUE
        if answer in ['T', 'TRUE', '1', 'YES', 'Y']:
            return 'TRUE'
        # All variations of FALSE
        elif answer in ['F', 'FALSE', '0', 'NO', 'N']:
            return 'FALSE'
    
    # Handle Multiple Choice - just return uppercase letter
    elif question_type == 'multiple-choice':
        # Extract just the letter (A, B, C, D, E)
        match = re.match(r'^([A-E])', answer)
        if match:
            return match.group(1)
    
    return answer


@router.post("/api/assessments/process-answer-key")
async def process_answer_key(file: UploadFile = File(...)):
    """Process uploaded answer key file and extract questions - SUPPORTS ALL FORMATS"""
    
    logger.info(f"📤 Processing answer key: {file.filename}")
    
    try:
        # Read file content
        file_content = await file.read()
        file_name = file.filename.lower()

        # Extract text based on file type
        if file_name.endswith(".pdf"):
            text_content = extract_text_from_pdf(file_content)
        elif file_name.endswith(".docx"):
            text_content = extract_text_from_docx(file_content)
        elif file_name.endswith(".txt"):
            text_content = extract_text_from_txt(file_content)
        else:
            raise HTTPException(status_code=400, detail="Invalid file format. Only PDF, DOCX, and TXT are allowed.")
        
        logger.info(f"📄 Extracted text length: {len(text_content)} characters")
        logger.info(f"📝 First 300 chars: {text_content[:300]}...")
        
        # Split into lines and process
        lines = [line.strip() for line in text_content.split("\n") if line.strip()]
        questions = []
        question_counter = 1
        
        logger.info(f"📋 Processing {len(lines)} lines...")
        
        for line_num, line in enumerate(lines):
            # Parse the line
            result = parse_answer_from_line(line, line_num + 1)
            
            if result['found']:
                # Create question data
                question_data = {
                    "id": question_counter,
                    "type": result['question_type'],
                    "answer": result['answer'],
                    "correctAnswer": result['answer'],
                    "text": line,
                    "points": 1
                }
                
                questions.append(question_data)
                logger.info(f"✅ Q{question_counter}: {result['question_type']} = {result['answer']} (from: {line[:50]}...)")
                question_counter += 1
            else:
                logger.debug(f"⏭️  Skipped line {line_num+1}: {line[:50]}...")
        
        # Count question types
        mcq_count = sum(1 for q in questions if q["type"] == "multiple-choice")
        tf_count = sum(1 for q in questions if q["type"] == "true-false")
        
        logger.info(f"✅ FINAL RESULT: Parsed {len(questions)} questions total")
        logger.info(f"📊 Breakdown: {mcq_count} MCQ, {tf_count} T/F")
        
        # Show first 5 questions for verification
        for i, q in enumerate(questions[:5]):
            logger.info(f"   Q{q['id']}: {q['type']} = {q['answer']}")
        
        if not questions:
            raise HTTPException(
                status_code=400, 
                detail=f"No valid answers found in the file. Please check the format.\n\nSupported formats:\n• 1. A\n• 1) True\n• A\n• True\n• Answer: B\n• F 8. Question text\n• T 9. Question text\n\nYour file had {len(lines)} lines but no valid answers were detected."
            )
        
        return JSONResponse(content={
            "success": True,
            "questions": questions,
            "format_detected": "mixed" if mcq_count > 0 and tf_count > 0 else ("multiple-choice" if mcq_count > 0 else "true-false"),
            "total_questions": len(questions),
            "mcq_count": mcq_count,
            "tf_count": tf_count,
            "debug_info": {
                "lines_processed": len(lines),
                "questions_found": len(questions),
                "first_3_lines": lines[:3] if len(lines) >= 3 else lines
            }
        })
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error processing answer key: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/assessments/check-with-answer-key")
async def check_assessment_with_answer_key(
    file: UploadFile = File(...),
    answer_key_data: str = Form(...),
    student_name: str = Form("Anonymous"),
    assessment_title: str = Form(...),
    subject: str = Form(...),
    num_questions: int = Form(...),
    total_points: int = Form(...),
    points_per_question: int = Form(...),
    assessment_type: str = Form("mixed"),
    use_ai_feedback: bool = Form(True),
    db: Session = Depends(get_db)
):
    """Process uploaded assessment with AI-powered feedback AND database storage - FIXED SCORING"""
    
    start_time = time.time()
    logger.info(f"🎯 Processing assessment for {student_name} - {assessment_title}")
    logger.info(f"🤖 AI Requested: {use_ai_feedback}, AI Available: {AI_ENABLED}")
    
    try:
        # Parse the answer key from the form data
        answer_key = json.loads(answer_key_data)
        logger.info(f"📝 Answer key has {len(answer_key)} questions")
        
        # Log answer key structure for debugging
        for i, q in enumerate(answer_key[:3]):
            logger.info(f"   Q{i+1}: type={q.get('type')}, answer={q.get('correctAnswer')}")
        
        # Read the file content based on its type
        file_content = await file.read()
        file_name = file.filename.lower()

        # Extract text from file
        if file_name.endswith(".pdf"):
            text_content = extract_text_from_pdf(file_content)
        elif file_name.endswith(".docx"):
            text_content = extract_text_from_docx(file_content)
        elif file_name.endswith(".txt"):
            text_content = extract_text_from_txt(file_content)
        else:
            raise HTTPException(status_code=400, detail="Invalid file format. Only PDF, DOCX, and TXT are allowed.")
        
        logger.info(f"📄 Extracted {len(text_content)} characters from student file")
        
        # Parse student answers from the text content
        student_answers_raw = [line.strip() for line in text_content.split("\n") if line.strip()]
        student_answers = []
        
        for line in student_answers_raw:
            result = parse_answer_from_line(line, 0)
            if result['found']:
                student_answers.append(result['answer'])
        
        # Pad with empty strings if needed
        if len(student_answers) < num_questions:
            student_answers.extend([''] * (num_questions - len(student_answers)))
        
        student_answers = student_answers[:num_questions]
        
        logger.info(f"📊 Parsed {len([a for a in student_answers if a])} student answers")
        
        # === CRITICAL FIX: Grade the assessment with PROPER normalization ===
        correct_count = 0
        incorrect_count = 0
        total_score = 0
        question_breakdown = []
        
        logger.info("🔍 Starting answer comparison...")
        
        for i, answer_key_item in enumerate(answer_key):
            student_answer = student_answers[i] if i < len(student_answers) else ''
            correct_answer = answer_key_item.get('correctAnswer', '')
            question_points = int(answer_key_item.get('points', points_per_question))
            question_type = answer_key_item.get('type', 'multiple-choice')
            
            # ⭐ CRITICAL FIX: Use normalize_answer function
            student_answer_normalized = normalize_answer(student_answer, question_type)
            correct_answer_normalized = normalize_answer(correct_answer, question_type)
            
            is_correct = student_answer_normalized == correct_answer_normalized
            points_earned = question_points if is_correct else 0
            
            # Detailed logging for debugging
            logger.info(f"Q{i+1}: Student='{student_answer}' ({student_answer_normalized}) | Correct='{correct_answer}' ({correct_answer_normalized}) | Match={is_correct}")
            
            if is_correct:
                correct_count += 1
            else:
                incorrect_count += 1
            
            total_score += points_earned
            
            question_breakdown.append({
                'questionNum': i + 1,
                'questionType': question_type,
                'studentAnswer': student_answer,
                'correctAnswer': correct_answer,
                'isCorrect': is_correct,
                'pointsEarned': points_earned,
                'pointsPossible': question_points
            })
        
        percentage = (total_score / total_points * 100) if total_points > 0 else 0
        letter_grade = 'A' if percentage >= 90 else 'B' if percentage >= 80 else 'C' if percentage >= 70 else 'D' if percentage >= 60 else 'F'
        
        logger.info(f"📈 FINAL Score: {total_score}/{total_points} ({percentage:.1f}%) - {correct_count} correct, {incorrect_count} incorrect")
        
        # AI feedback generation (OPTIONAL - works even if OpenAI quota exceeded)
        ai_feedback_text = None
        strengths = []
        weaknesses = []
        recommendations = []
        ai_used = False
        
        if use_ai_feedback and AI_ENABLED and client:
            try:
                logger.info("🤖 Generating AI feedback...")
                response = client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[{
                        "role": "system",
                        "content": "You are an educational assessment expert. Provide constructive feedback in a structured format."
                    }, {
                        "role": "user", 
                        "content": f"""Analyze this assessment:
                        Subject: {subject}
                        Score: {percentage:.1f}% ({correct_count}/{num_questions} correct)
                        
                        Provide feedback in this exact format:
                        
                        STRENGTHS:
                        1. [First strength]
                        2. [Second strength]
                        
                        WEAKNESSES:
                        1. [First weakness]
                        2. [Second weakness]
                        
                        RECOMMENDATIONS:
                        1. [First recommendation]
                        2. [Second recommendation]
                        
                        Keep each point concise (1-2 sentences)."""
                    }],
                    max_tokens=400
                )
                ai_feedback_text = response.choices[0].message.content
                ai_used = True
                
                # Parse AI response into categories
                sections = ai_feedback_text.split('\n\n')
                
                for section in sections:
                    if 'STRENGTHS:' in section.upper():
                        lines = [l.strip() for l in section.split('\n') if l.strip() and not 'STRENGTHS:' in l.upper()]
                        strengths = [l.lstrip('1234567890. ') for l in lines[:2]]
                    elif 'WEAKNESSES:' in section.upper():
                        lines = [l.strip() for l in section.split('\n') if l.strip() and not 'WEAKNESSES:' in l.upper()]
                        weaknesses = [l.lstrip('1234567890. ') for l in lines[:2]]
                    elif 'RECOMMENDATIONS:' in section.upper():
                        lines = [l.strip() for l in section.split('\n') if l.strip() and not 'RECOMMENDATIONS:' in l.upper()]
                        recommendations = [l.lstrip('1234567890. ') for l in lines[:2]]
                
                # Fallback if parsing failed
                if not strengths:
                    strengths = ["Completed the assessment", "Demonstrated effort in answering"]
                if not weaknesses:
                    weaknesses = [f"Missed {incorrect_count} questions", "Room for improvement in understanding"]
                if not recommendations:
                    recommendations = ["Review incorrect answers carefully", "Practice similar problems"]
                
                logger.info("✅ AI feedback generated successfully!")
            except Exception as e:
                logger.error(f"❌ AI Error (Non-critical): {e}")
                ai_feedback_text = f"Assessment completed! Score: {percentage:.1f}%"
                strengths = [f"Answered {correct_count} questions correctly"]
                weaknesses = [f"Missed {incorrect_count} questions"] if incorrect_count > 0 else ["Keep up the good work"]
                recommendations = ["Review incorrect answers"] if incorrect_count > 0 else ["Continue practicing"]
        else:
            logger.warning(f"⚠️ AI not used (scores still accurate): use_ai={use_ai_feedback}, enabled={AI_ENABLED}")
            ai_feedback_text = f"Assessment scored! {correct_count}/{num_questions} correct ({percentage:.1f}%)"
            strengths = [f"Answered {correct_count} questions correctly"]
            weaknesses = [f"Missed {incorrect_count} questions"] if incorrect_count > 0 else ["Keep practicing"]
            recommendations = ["Review incorrect answers and study the material"] if incorrect_count > 0 else ["Great work!"]
        
        # Save to database
        database_saved = False
        uploaded_assessment_id = None
        answer_key_id = None
        
        try:
            logger.info("💾 Saving to database...")
            
            # 1. Create Answer Key
            answer_key_obj = AnswerKey(
                title=assessment_title,
                subject=subject,
                assessment_type=assessment_type,
                num_questions=num_questions,
                questions_data=answer_key,
                total_points=total_points,
                original_filename=f"answer_key_{file.filename}",
                file_size=len(file_content)
            )
            db.add(answer_key_obj)
            db.flush()
            answer_key_id = answer_key_obj.id
            logger.info(f"✅ Answer key saved with ID: {answer_key_id}")
            
            # 2. Create Uploaded Assessment
            uploaded_assessment_obj = UploadedAssessment(
                answer_key_id=answer_key_id,
                original_filename=file.filename,
                file_size=len(file_content),
                assessment_title=assessment_title,
                subject=subject,
                assessment_data={"student_answers": student_answers},
                processed_at=datetime.utcnow()
            )
            db.add(uploaded_assessment_obj)
            db.flush()
            uploaded_assessment_id = uploaded_assessment_obj.id
            logger.info(f"✅ Uploaded assessment saved with ID: {uploaded_assessment_id}")
            
            # 3. Create Grading Result
            grading_result_obj = GradingResult(
                uploaded_assessment_id=uploaded_assessment_id,
                answer_key_id=answer_key_id,
                student_name=student_name,
                assessment_title=assessment_title,
                subject=subject,
                total_questions=num_questions,
                correct_answers=correct_count,
                incorrect_answers=incorrect_count,
                score=float(total_score),
                max_score=float(total_points),
                percentage=float(percentage),
                letter_grade=letter_grade,
                question_breakdown=question_breakdown,
                strengths=strengths,
                weaknesses=weaknesses,
                recommendations=recommendations,
                detailed_analysis=ai_feedback_text,
                ai_used=ai_used,
                ai_model=OPENAI_MODEL if ai_used else None,
                processing_time=float(time.time() - start_time)
            )
            db.add(grading_result_obj)
            
            # Commit all changes
            db.commit()
            database_saved = True
            logger.info(f"✅ ALL DATA SAVED TO DATABASE!")
            
        except Exception as db_error:
            logger.error(f"❌ Database error: {db_error}")
            import traceback
            logger.error(traceback.format_exc())
            db.rollback()
            database_saved = False
        
        processing_time = time.time() - start_time
        
        return JSONResponse(content={
            'success': True,
            'message': 'Assessment processed successfully with accurate scoring!',
            'ai_enabled': ai_used,
            'saved': database_saved,
            'processing_time': round(processing_time, 2),
            'results': {
                'studentName': student_name,
                'assessmentTitle': assessment_title,
                'subject': subject,
                'percentage': round(percentage, 2),
                'pointsEarned': total_score,
                'totalPoints': total_points,
                'correctAnswers': correct_count,
                'incorrectAnswers': incorrect_count,
                'totalQuestions': num_questions,
                'letterGrade': letter_grade,
                'questionBreakdown': question_breakdown,
                'feedback': {
                    'strengths': strengths,
                    'weaknesses': weaknesses,
                    'recommendations': recommendations,
                    'detailedAnalysis': ai_feedback_text
                },
                'aiUsed': ai_used,
                'databaseSaved': database_saved,
                'uploadedAssessmentId': uploaded_assessment_id,
                'answerKeyId': answer_key_id
            }
        })
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Processing error: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))