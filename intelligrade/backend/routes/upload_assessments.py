# routes/upload_assessments.py - COMPLETE FIXED VERSION WITH ACCURATE POINTS CALCULATION
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional, List
import json
import time
import re
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

# ⭐ CRITICAL: Load .env FIRST
load_dotenv()

# Import OpenAI AFTER loading .env
try:
    from openai import OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    if OPENAI_API_KEY and OPENAI_API_KEY.strip():
        client = OpenAI(api_key=OPENAI_API_KEY)
        AI_ENABLED = True
        print(f"✅ OpenAI initialized successfully with key: {OPENAI_API_KEY[:20]}...")
    else:
        client = None
        AI_ENABLED = False
        print("⚠️ WARNING: OPENAI_API_KEY not found in .env file!")
except ImportError:
    AI_ENABLED = False
    client = None
    print("⚠️ WARNING: OpenAI package not installed!")
except Exception as e:
    AI_ENABLED = False
    client = None
    print(f"⚠️ OpenAI initialization error: {e}")

# Import database and models
from database import get_db
from models import AnswerKey, UploadedAssessment, GradingResult
from services.file_processing import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt

router = APIRouter()

# Configuration
OPENAI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"🤖 AI Status: {'ENABLED ✅' if AI_ENABLED else 'DISABLED ❌'}")
if AI_ENABLED:
    logger.info(f"📡 Using OpenAI Model: {OPENAI_MODEL}")


def parse_answer_from_line(line: str, line_num: int) -> dict:
    """⭐ Parse answer with PRIORITY ORDER to avoid duplicates"""
    line_original = line.strip()
    line_upper = line.upper().strip()
    
    if not line_original:
        return {'answer': None, 'question_type': None, 'found': False}
    
    # SKIP PATTERNS - Lines to ignore
    skip_patterns = [
        r'^ANSWER[\s]*KEY',
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
        r'^\d+[\.\)]\s+\w{3,}',  # Skip "1. Which of..." question lines
        r'^[A-E]\)\s+\w{3,}',     # Skip "a) Burning wood" option lines
    ]
    
    for pattern in skip_patterns:
        if re.match(pattern, line_upper):
            return {'answer': None, 'question_type': None, 'found': False}
    
    # ⭐ PRIORITY 1: "Answer:" format (HIGHEST PRIORITY)
    match = re.match(r'^(ANSWER|ANS)[\s]*:[\s]*([A-E]|T|F|TRUE|FALSE)', line_upper)
    if match:
        answer = match.group(2)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # ⭐ PRIORITY 2: **T 5.** or **F 6.** format (answer key format)
    match = re.match(r'^\*?\*?([TF]|TRUE|FALSE)[\s]+\d+\.', line_upper)
    if match:
        answer = match.group(1)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
    
    # ⭐ PRIORITY 3: Single T/F at line start with optional question number
    match = re.match(r'^([TF]|TRUE|FALSE)[\s\.\)]*(\d+)?[\.\s]*$', line_upper)
    if match:
        answer = match.group(1)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
    
    # ⭐ PRIORITY 4: "B 1." format (answer key with question number)
    match = re.match(r'^([A-E])[\s]+\d+\.', line_upper)
    if match:
        answer = match.group(1)
        return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # ⭐ PRIORITY 5: Number THEN answer (e.g., "1. A", "2. B")
    match = re.match(r'^\d+[\.\)\:\-\s]+([A-E]|T|F)[\.\)\s]*$', line_upper)
    if match:
        answer = match.group(1)
        if answer in ['T', 'F']:
            return {'answer': 'True' if answer == 'T' else 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    # PRIORITY 6: Q prefix format
    match = re.match(r'^Q(UESTION)?[\s]*\d+[\.\:\s]+([A-E]|T|F|TRUE|FALSE)', line_upper)
    if match:
        answer = match.group(2)
        if answer in ['T', 'TRUE']:
            return {'answer': 'True', 'question_type': 'true-false', 'found': True}
        elif answer in ['F', 'FALSE']:
            return {'answer': 'False', 'question_type': 'true-false', 'found': True}
        else:
            return {'answer': answer, 'question_type': 'multiple-choice', 'found': True}
    
    return {'answer': None, 'question_type': None, 'found': False}


def normalize_answer(answer: str, question_type: str) -> str:
    """⭐ Normalize answers for comparison"""
    if not answer:
        return ''
    
    answer = str(answer).strip().upper()
    answer = answer.replace('.', '').replace(')', '').replace(':', '').strip()
    
    if question_type == 'true-false':
        if answer in ['T', 'TRUE', '1', 'YES', 'Y', 'CORRECT']:
            return 'TRUE'
        elif answer in ['F', 'FALSE', '0', 'NO', 'N', 'WRONG']:
            return 'FALSE'
        elif answer == 'A':
            logger.warning(f"⚠️ Student used 'A' for T/F → TRUE")
            return 'TRUE'
        elif answer == 'B':
            logger.warning(f"⚠️ Student used 'B' for T/F → FALSE")
            return 'FALSE'
        elif answer == 'C':
            logger.warning(f"⚠️ Student used 'C' for T/F → TRUE")
            return 'TRUE'
        elif answer == 'D':
            logger.warning(f"⚠️ Student used 'D' for T/F → FALSE")
            return 'FALSE'
        else:
            logger.error(f"❌ INVALID T/F: '{answer}' → BLANK")
            return ''
    
    elif question_type == 'multiple-choice':
        match = re.match(r'^([A-E])$', answer)
        if match:
            return match.group(1)
        elif answer in ['T', 'TRUE']:
            logger.warning(f"⚠️ Student used 'TRUE' for MCQ → 'A'")
            return 'A'
        elif answer in ['F', 'FALSE']:
            logger.warning(f"⚠️ Student used 'FALSE' for MCQ → 'B'")
            return 'B'
        else:
            first_char = answer[0] if answer and answer[0] in 'ABCDE' else ''
            if first_char:
                logger.warning(f"⚠️ Extracted '{first_char}' from '{answer}'")
                return first_char
            else:
                logger.error(f"❌ INVALID MCQ: '{answer}' → BLANK")
                return ''
    
    return answer


def extract_student_answers_contextual(text_content: str, answer_key: List[dict], num_questions: int) -> List[str]:
    """⭐ Extract student answers with context"""
    lines = [line.strip() for line in text_content.split("\n") if line.strip()]
    parsed_answers = []
    
    logger.info(f"📋 Processing {len(lines)} lines...")
    logger.info("=" * 80)
    
    for line_num, line in enumerate(lines):
        result = parse_answer_from_line(line, line_num + 1)
        
        if result['found']:
            parsed_answers.append({
                'answer': result['answer'],
                'detected_type': result['question_type'],
                'line': line,
                'line_number': line_num + 1
            })
            logger.info(f"✅ Line {line_num+1}: '{result['answer']}' ({result['question_type']})")
            logger.info(f"   Text: {line[:80]}...")
    
    logger.info("=" * 80)
    logger.info(f"📊 FOUND: {len(parsed_answers)} answers (Expected: {num_questions})")
    
    if len(parsed_answers) > num_questions:
        logger.warning(f"⚠️ Found {len(parsed_answers)} but need {num_questions}!")
        logger.warning(f"⚠️ Using first {num_questions} answers")
    
    logger.info("=" * 80)
    
    student_answers = []
    
    for i in range(num_questions):
        if i < len(answer_key) and i < len(parsed_answers):
            expected_type = answer_key[i].get('type', 'multiple-choice')
            student_ans = parsed_answers[i]['answer']
            detected_type = parsed_answers[i]['detected_type']
            
            if expected_type != detected_type:
                logger.warning(f"⚠️ Q{i+1}: Expected {expected_type}, got {detected_type}")
            
            student_answers.append(student_ans)
        else:
            logger.warning(f"❌ Q{i+1}: NO ANSWER")
            student_answers.append('')
    
    return student_answers


@router.post("/api/assessments/process-answer-key")
async def process_answer_key(file: UploadFile = File(...)):
    """Process answer key file"""
    logger.info(f"📤 Processing answer key: {file.filename}")
    
    try:
        file_content = await file.read()
        file_name = file.filename.lower()

        if file_name.endswith(".pdf"):
            text_content = extract_text_from_pdf(file_content)
        elif file_name.endswith(".docx"):
            text_content = extract_text_from_docx(file_content)
        elif file_name.endswith(".txt"):
            text_content = extract_text_from_txt(file_content)
        else:
            raise HTTPException(status_code=400, detail="Invalid file format")
        
        logger.info(f"📄 Extracted {len(text_content)} characters")
        
        lines = [line.strip() for line in text_content.split("\n") if line.strip()]
        questions = []
        question_counter = 1
        
        for line_num, line in enumerate(lines):
            result = parse_answer_from_line(line, line_num + 1)
            
            if result['found']:
                questions.append({
                    "id": question_counter,
                    "type": result['question_type'],
                    "answer": result['answer'],
                    "correctAnswer": result['answer'],
                    "text": line,
                    "points": 1
                })
                logger.info(f"✅ Q{question_counter}: {result['question_type']} = {result['answer']}")
                question_counter += 1
        
        if not questions:
            raise HTTPException(status_code=400, detail="No valid answers found")
        
        mcq_count = sum(1 for q in questions if q["type"] == "multiple-choice")
        tf_count = sum(1 for q in questions if q["type"] == "true-false")
        
        return JSONResponse(content={
            "success": True,
            "questions": questions,
            "format_detected": "mixed" if mcq_count > 0 and tf_count > 0 else ("multiple-choice" if mcq_count > 0 else "true-false"),
            "total_questions": len(questions),
            "mcq_count": mcq_count,
            "tf_count": tf_count
        })
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
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
    scoring_method: str = Form("uniform"),
    db: Session = Depends(get_db)
):
    """Process assessment with accurate point calculation"""
    
    start_time = time.time()
    logger.info(f"🎯 Processing: {student_name} - {assessment_title}")
    
    try:
        # ⭐ FIXED: Parse answer key data properly
        answer_key = json.loads(answer_key_data)
        logger.info(f"📋 Answer Key Data Received:")
        logger.info(f"   Questions: {len(answer_key)}")
        logger.info(f"   Scoring Method: {scoring_method}")
        logger.info(f"   Total Points (expected): {total_points}")
        
        # ⭐ FIXED: Validate and build points map
        question_points_map = {}
        calculated_total = 0
        
        for q in answer_key:
            q_id = q.get('id', 0)
            q_points = int(q.get('points', points_per_question))  # ⭐ Read individual points
            question_points_map[q_id] = q_points
            calculated_total += q_points
            logger.info(f"   Q{q_id}: {q_points} points")
        
        logger.info(f"   Calculated Total: {calculated_total} points")
        
        # ⭐ FIXED: Use calculated total if it differs from received total
        if calculated_total != total_points:
            logger.warning(f"⚠️ Total mismatch! Using calculated: {calculated_total}")
            total_points = calculated_total
        
        file_content = await file.read()
        file_name = file.filename.lower()

        if file_name.endswith(".pdf"):
            text_content = extract_text_from_pdf(file_content)
        elif file_name.endswith(".docx"):
            text_content = extract_text_from_docx(file_content)
        elif file_name.endswith(".txt"):
            text_content = extract_text_from_txt(file_content)
        else:
            raise HTTPException(status_code=400, detail="Invalid file format")
        
        student_answers = extract_student_answers_contextual(text_content, answer_key, num_questions)
        
        # ⭐ GRADING WITH ACCURATE POINTS
        correct_count = 0
        incorrect_count = 0
        total_score = 0
        question_breakdown = []
        
        logger.info("=" * 80)
        logger.info("🔍 GRADING RESULTS")
        logger.info("=" * 80)
        
        for i, answer_key_item in enumerate(answer_key):
            student_answer = student_answers[i] if i < len(student_answers) else ''
            correct_answer = answer_key_item.get('correctAnswer', '')
            
            # ⭐ FIXED: Read individual points for this question
            question_points = int(answer_key_item.get('points', points_per_question))
            question_type = answer_key_item.get('type', 'multiple-choice')
            question_id = answer_key_item.get('id', i + 1)
            
            student_normalized = normalize_answer(student_answer, question_type)
            correct_normalized = normalize_answer(correct_answer, question_type)
            
            is_correct = (student_normalized == correct_normalized) and student_normalized != ''
            points_earned = question_points if is_correct else 0  # ⭐ Award full question points if correct
            
            status = "✅" if is_correct else "❌"
            logger.info(f"\nQ{question_id} ({question_type}):")
            logger.info(f"  Student: '{student_answer}' → '{student_normalized}'")
            logger.info(f"  Correct: '{correct_answer}' → '{correct_normalized}'")
            logger.info(f"  {status} {points_earned}/{question_points} pts")  # ⭐ Show correct points
            
            if is_correct:
                correct_count += 1
            else:
                incorrect_count += 1
            
            total_score += points_earned
            
            question_breakdown.append({
                'questionNum': question_id,
                'questionType': question_type,
                'studentAnswer': student_answer,
                'correctAnswer': correct_answer,
                'isCorrect': is_correct,
                'pointsEarned': points_earned,  # ⭐ Use correct points
                'pointsPossible': question_points  # ⭐ Use correct points
            })
        
        logger.info("=" * 80)
        percentage = (total_score / total_points * 100) if total_points > 0 else 0
        letter_grade = 'A' if percentage >= 90 else 'B' if percentage >= 80 else 'C' if percentage >= 70 else 'D' if percentage >= 60 else 'F'
        
        logger.info(f"📈 FINAL: {total_score}/{total_points} ({percentage:.1f}%)")  # ⭐ Show correct calculation
        logger.info(f"📊 {correct_count} ✅ | {incorrect_count} ❌")
        logger.info(f"🎓 Grade: {letter_grade}")
        logger.info("=" * 80)
        
        # AI FEEDBACK
        ai_feedback_text = None
        strengths = []
        weaknesses = []
        recommendations = []
        ai_used = False
        ai_error = None
        
        if use_ai_feedback and AI_ENABLED and client:
            try:
                logger.info("🤖 Generating AI feedback...")
                
                response = client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an educational assessment expert. Provide concise, constructive feedback."
                        },
                        {
                            "role": "user", 
                            "content": f"""Analyze this {subject} assessment:

Score: {percentage:.1f}% ({correct_count}/{num_questions} correct)
Points: {total_score}/{total_points}
Letter Grade: {letter_grade}

Provide feedback in this format:

STRENGTHS:
1. [One specific strength]
2. [Another strength]

WEAKNESSES:
1. [One area to improve]
2. [Another area]

RECOMMENDATIONS:
1. [Specific study tip]
2. [Another recommendation]

Keep each point to 1 sentence max."""
                        }
                    ],
                    max_tokens=500,
                    temperature=0.7
                )
                
                ai_feedback_text = response.choices[0].message.content
                ai_used = True
                
                # Parse response
                sections = ai_feedback_text.split('\n\n')
                for section in sections:
                    if 'STRENGTHS:' in section.upper():
                        lines = [l.strip() for l in section.split('\n') if l.strip() and 'STRENGTHS:' not in l.upper()]
                        strengths = [l.lstrip('1234567890. -•') for l in lines if l][:3]
                    elif 'WEAKNESSES:' in section.upper():
                        lines = [l.strip() for l in section.split('\n') if l.strip() and 'WEAKNESSES:' not in l.upper()]
                        weaknesses = [l.lstrip('1234567890. -•') for l in lines if l][:3]
                    elif 'RECOMMENDATIONS:' in section.upper():
                        lines = [l.strip() for l in section.split('\n') if l.strip() and 'RECOMMENDATIONS:' not in l.upper()]
                        recommendations = [l.lstrip('1234567890. -•') for l in lines if l][:3]
                
                # Fallbacks
                if not strengths:
                    strengths = [f"Completed assessment with {correct_count} correct answers", "Demonstrated effort"]
                if not weaknesses:
                    weaknesses = [f"Missed {incorrect_count} questions", "Room for improvement"]
                if not recommendations:
                    recommendations = ["Review incorrect answers", "Practice similar problems"]
                
                logger.info("✅ AI feedback generated!")
                
            except Exception as e:
                logger.error(f"❌ AI Error: {e}")
                ai_used = False
                ai_error = str(e)
                strengths = [f"Answered {correct_count} correctly"]
                weaknesses = [f"Missed {incorrect_count} questions"]
                recommendations = ["Review material and practice"]
        else:
            logger.info("⚠️ AI not used - using rule-based feedback")
            strengths = [f"Answered {correct_count} correctly"]
            weaknesses = [f"Missed {incorrect_count} questions"]
            recommendations = ["Review material"]
        
        # DATABASE SAVE
        database_saved = False
        try:
            answer_key_obj = AnswerKey(
                title=assessment_title, subject=subject, assessment_type=assessment_type,
                num_questions=num_questions, questions_data=answer_key, total_points=total_points,
                original_filename=f"key_{file.filename}", file_size=len(file_content)
            )
            db.add(answer_key_obj)
            db.flush()
            
            uploaded_obj = UploadedAssessment(
                answer_key_id=answer_key_obj.id, original_filename=file.filename,
                file_size=len(file_content), assessment_title=assessment_title,
                subject=subject, assessment_data={"student_answers": student_answers},
                processed_at=datetime.utcnow()
            )
            db.add(uploaded_obj)
            db.flush()
            
            grading_obj = GradingResult(
                uploaded_assessment_id=uploaded_obj.id, answer_key_id=answer_key_obj.id,
                student_name=student_name, assessment_title=assessment_title, subject=subject,
                total_questions=num_questions, correct_answers=correct_count,
                incorrect_answers=incorrect_count, score=float(total_score),
                max_score=float(total_points), percentage=float(percentage),
                letter_grade=letter_grade, question_breakdown=question_breakdown,
                strengths=strengths, weaknesses=weaknesses, recommendations=recommendations,
                detailed_analysis=ai_feedback_text, ai_used=ai_used,
                ai_model=OPENAI_MODEL if ai_used else None,
                processing_time=float(time.time() - start_time)
            )
            db.add(grading_obj)
            db.commit()
            database_saved = True
            logger.info("✅ Saved to database!")
        except Exception as e:
            logger.error(f"❌ DB Error: {e}")
            db.rollback()
        
        return JSONResponse(content={
            'success': True,
            'message': 'Assessment processed successfully!',
            'results': {
                'studentName': student_name,
                'assessmentTitle': assessment_title,
                'subject': subject,
                'percentage': round(percentage, 2),
                'pointsEarned': total_score,  # ⭐ Accurate points
                'totalPoints': total_points,  # ⭐ Accurate total
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
                'aiError': ai_error,
                'databaseSaved': database_saved,
                'processing_time': round(time.time() - start_time, 2)
            }
        })
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))