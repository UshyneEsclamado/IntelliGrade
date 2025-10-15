"""
Enhanced Assessment endpoints with proper answer key comparison
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import re
import io
from typing import Dict, Any, Optional, List
import logging
import json

# Add docx support (with fallback)
try:
    from docx import Document
    DOCX_AVAILABLE = True
    print("✅ python-docx available")
except ImportError:
    DOCX_AVAILABLE = False
    print("⚠️ python-docx not available - using fallback text extraction")

router = APIRouter()

# === CORE FUNCTIONS ===

def normalize_answer(answer: str) -> str:
    """Normalize answer to standard format"""
    answer = answer.upper().strip()
    
    # Handle True/False variations
    if answer in ['T', 'TRUE']:
        return 'TRUE'
    elif answer in ['F', 'FALSE']:
        return 'FALSE'
    
    # Handle multiple choice
    if answer in ['A', 'B', 'C', 'D', 'E']:
        return answer
    
    return answer

def determine_question_type(answer: str, section_hint: str = "") -> str:
    """Determine if question is true-false or multiple choice"""
    if answer in ['TRUE', 'FALSE']:
        return 'true-false'
    elif answer in ['A', 'B', 'C', 'D', 'E']:
        return 'multiple-choice'
    elif section_hint:
        return section_hint
    else:
        return 'multiple-choice'

def extract_question_and_answer_flexible(line: str, section_type: str, question_counter: int) -> Optional[Dict[str, Any]]:
    """Extract question number and answer from a single line - handles ALL formats"""
    
    line = line.strip()
    if not line:
        return None
    
    # Format patterns to try (in order of preference)
    patterns = [
        # PATTERN 1: "1.	Question text  T" - Tab and multiple spaces
        r'^(\d+)\.\s*(.+?)\s+([A-E]|T|F|TRUE|FALSE|True|False)\s*$',
        
        # PATTERN 2: "T 1. Question text" or "B 1. Question text" (Answer at start)
        r'^([A-E]|T|F|TRUE|FALSE|True|False)\s+(\d+)\.?\s*(.*)$',
        
        # PATTERN 3: "Answer: B" format
        r'^(?:(\d+)\.?\s*(.+?)\s*)?Answer\s*:\s*([A-E]|T|F|TRUE|FALSE|True|False)\s*$',
        
        # PATTERN 4: Just "1. A" or "Q1: B"
        r'^(?:Q\s*)?(\d+)[\.\:\)]\s*([A-E]|T|F|TRUE|FALSE|True|False)\s*$',
        
        # PATTERN 5: Just "A" or "True"
        r'^([A-E]|TRUE|FALSE|True|False|T|F)\s*$'
    ]
    
    for pattern_idx, pattern in enumerate(patterns):
        match = re.match(pattern, line, re.IGNORECASE)
        if match:
            groups = match.groups()
            
            if pattern_idx == 0:  # "1. Question text T"
                question_num = int(groups[0])
                question_text = groups[1].strip()
                answer = normalize_answer(groups[2])
                
            elif pattern_idx == 1:  # "T 1. Question text"
                answer = normalize_answer(groups[0])
                question_num = int(groups[1])
                question_text = groups[2].strip() if groups[2] else f"Question {question_num}"
                
            elif pattern_idx == 2:  # "Answer: B"
                if groups[0]:
                    question_num = int(groups[0])
                    question_text = groups[1].strip() if groups[1] else f"Question {question_num}"
                else:
                    question_num = question_counter
                    question_text = f"Question {question_num}"
                answer = normalize_answer(groups[2])
                
            elif pattern_idx == 3:  # "1. A"
                question_num = int(groups[0])
                answer = normalize_answer(groups[1])
                question_text = f"Question {question_num}"
                
            elif pattern_idx == 4:  # Just "A"
                question_num = question_counter
                answer = normalize_answer(groups[0])
                question_text = f"Question {question_num}"
            
            q_type = determine_question_type(answer, section_type)
            
            return {
                "question_number": question_num,
                "answer": answer,
                "type": q_type,
                "question_text": question_text
            }
    
    return None

def parse_answer_key_flexible(text_content: str) -> Dict[str, Any]:
    """Parse answer key from text content - supports ALL flexible formats"""
    questions = []
    lines = text_content.strip().split('\n')
    
    print(f"\n{'='*60}")
    print(f"🔍 PARSING STARTED")
    print(f"{'='*60}")
    print(f"📄 Total lines to parse: {len(lines)}")
    
    current_section = "unknown"
    question_counter = 1
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip section headers
        if any(header in line.lower() for header in ['true or false', 'multiple choice', 'grade', 'assessment', 't or f', 'mcq']):
            if any(tf in line.lower() for tf in ['true or false', 't or f', 'true/false']):
                current_section = "true-false"
                question_counter = 1
                print(f"📍 Section detected: TRUE/FALSE")
            elif any(mc in line.lower() for mc in ['multiple choice', 'mcq', 'multiple-choice']):
                current_section = "multiple-choice"
                question_counter = 1
                print(f"📍 Section detected: MULTIPLE CHOICE")
            continue
            
        # Skip option lines (a), b), c), d)
        if re.match(r'^\s*[a-e][\.\)]\s+', line, re.IGNORECASE):
            continue
            
        # Extract question and answer
        extracted = extract_question_and_answer_flexible(line, current_section, question_counter)
        
        if extracted:
            questions.append({
                "id": extracted["question_number"],
                "type": extracted["type"],
                "answer": extracted["answer"],
                "correctAnswer": extracted["answer"],
                "points": 1,
                "text": extracted.get("question_text", f"Question {extracted['question_number']}")
            })
            question_counter += 1
            print(f"✅ Q{extracted['question_number']} = '{extracted['answer']}' ({extracted['type']})")
    
    print(f"\n{'='*60}")
    print(f"📊 PARSING COMPLETED")
    print(f"✅ Total questions parsed: {len(questions)}")
    print(f"{'='*60}\n")
    
    return {
        "questions": questions,
        "format_type": "flexible_mixed"
    }

async def extract_text_from_file(file: UploadFile) -> str:
    """Extract text from uploaded file"""
    try:
        content = await file.read()
        
        if file.filename.endswith('.txt'):
            return content.decode('utf-8')
        elif file.filename.endswith('.docx'):
            if DOCX_AVAILABLE:
                try:
                    doc = Document(io.BytesIO(content))
                    text_content = ""
                    for paragraph in doc.paragraphs:
                        text_content += paragraph.text + "\n"
                    return text_content
                except Exception as e:
                    print(f"⚠️ python-docx failed: {e}, using fallback")
                    return content.decode('utf-8', errors='ignore')
            else:
                return content.decode('utf-8', errors='ignore')
        else:
            return content.decode('utf-8', errors='ignore')
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not extract text from file: {str(e)}")

def compare_answers(student_answers: List[Dict], answer_key: Dict[int, str], points_per_question: int) -> Dict[str, Any]:
    """
    Compare student answers with answer key and calculate results
    """
    correct_count = 0
    incorrect_count = 0
    question_results = []
    missed_topics = []
    
    print(f"\n{'='*60}")
    print(f"🔍 ANSWER COMPARISON STARTED")
    print(f"{'='*60}")
    print(f"📝 Student answers: {len(student_answers)}")
    print(f"🔑 Answer key entries: {len(answer_key)}")
    
    for student_answer in student_answers:
        q_num = student_answer["id"]
        student_resp = normalize_answer(student_answer["answer"])
        correct_resp = normalize_answer(answer_key.get(q_num, ""))
        
        is_correct = student_resp == correct_resp
        
        print(f"Q{q_num}: Student='{student_resp}' vs Correct='{correct_resp}' → {'✅ CORRECT' if is_correct else '❌ WRONG'}")
        
        if is_correct:
            correct_count += 1
        else:
            incorrect_count += 1
            missed_topics.append(f"Question {q_num}")
            
        question_results.append({
            "question": q_num,
            "student_answer": student_resp,
            "correct_answer": correct_resp,
            "correct": is_correct,
            "points_earned": points_per_question if is_correct else 0,
            "points_possible": points_per_question
        })
    
    total_questions = len(student_answers)
    percentage = round((correct_count / total_questions) * 100) if total_questions > 0 else 0
    
    print(f"\n📊 COMPARISON RESULTS:")
    print(f"   ✅ Correct: {correct_count}/{total_questions}")
    print(f"   ❌ Incorrect: {incorrect_count}/{total_questions}")
    print(f"   📈 Percentage: {percentage}%")
    print(f"{'='*60}\n")
    
    return {
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "total_questions": total_questions,
        "percentage": percentage,
        "question_results": question_results,
        "missed_topics": missed_topics
    }

def generate_ai_feedback(comparison_results: Dict[str, Any], subject: str, assessment_title: str) -> Dict[str, Any]:
    """
    Generate AI-style feedback based on comparison results
    """
    percentage = comparison_results["percentage"]
    correct = comparison_results["correct_count"]
    total = comparison_results["total_questions"]
    
    # Generate strengths
    strengths = []
    if percentage >= 90:
        strengths.append("Excellent mastery of the subject matter")
        strengths.append("Consistently accurate responses across all question types")
        strengths.append("Strong analytical and critical thinking skills demonstrated")
    elif percentage >= 80:
        strengths.append("Very good understanding of core concepts")
        strengths.append("Solid performance with minor areas for improvement")
        strengths.append(f"Successfully answered {correct} out of {total} questions")
    elif percentage >= 70:
        strengths.append("Good grasp of fundamental concepts")
        strengths.append("Shows consistent effort and engagement")
        strengths.append("Demonstrates understanding of key topics")
    elif percentage >= 60:
        strengths.append("Basic understanding of core material")
        strengths.append(f"Successfully answered {correct} questions correctly")
    else:
        strengths.append("Shows engagement with the material")
        strengths.append("Opportunity for significant improvement identified")
    
    # Generate weaknesses
    weaknesses = []
    if percentage < 90:
        incorrect = comparison_results["incorrect_count"]
        weaknesses.append(f"Needs improvement on {incorrect} question(s)")
        
        if percentage < 70:
            weaknesses.append("Gaps in understanding of fundamental concepts")
            weaknesses.append("May benefit from additional study time and practice")
        
        if comparison_results["missed_topics"]:
            weaknesses.append(f"Review needed for: {', '.join(comparison_results['missed_topics'][:3])}")
    
    # Generate recommendations
    recommendations = []
    recommendations.append(f"Review the {subject} material covered in {assessment_title}")
    recommendations.append("Study the questions answered incorrectly and understand why")
    recommendations.append("Practice similar problems to reinforce learning")
    
    if percentage < 80:
        recommendations.append("Consider scheduling a review session with the instructor")
        recommendations.append("Form a study group with classmates to discuss challenging topics")
    
    if percentage >= 90:
        recommendations.append("Excellent work! Continue with this level of preparation")
    
    # Detailed analysis
    performance_level = "outstanding" if percentage >= 90 else "very good" if percentage >= 80 else "satisfactory" if percentage >= 70 else "needs improvement"
    
    detailed_analysis = f"""
Assessment Performance Analysis:

The student demonstrated {performance_level} performance on this {subject} assessment titled "{assessment_title}". 
They correctly answered {correct} out of {total} questions ({percentage}%), showing {"strong" if percentage >= 80 else "adequate" if percentage >= 60 else "developing"} 
understanding of the material.

{"The student shows excellent command of the subject matter and should continue with their current study approach." if percentage >= 90 else
 "The student shows good understanding but has room for improvement in certain areas." if percentage >= 70 else
 "The student would benefit from additional review and practice of the core concepts."}

{"Key areas of strength include consistent accuracy across question types." if percentage >= 80 else 
 "Focus should be placed on reviewing missed questions and understanding the underlying concepts."}
    """.strip()
    
    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations,
        "detailedAnalysis": detailed_analysis,
        "performanceLevel": performance_level
    }

# === API ENDPOINTS ===

@router.post("/check-with-answer-key")
async def check_with_answer_key(
    file: UploadFile = File(...),
    student_name: str = Form(None),
    assessment_title: str = Form(...),
    subject: str = Form(...),
    num_questions: int = Form(...),
    points_per_question: int = Form(...),
    total_points: int = Form(...),
    assessment_type: str = Form(...),
    answer_key_file: UploadFile = File(None),
    answer_key_data: str = Form(None)
):
    """
    Check student assessment against answer key with detailed comparison
    """
    try:
        print(f"\n🚀 STARTING ASSESSMENT CHECK")
        print(f"{'='*60}")
        print(f"👤 Student: {student_name or 'Auto-detected'}")
        print(f"📚 Subject: {subject}")
        print(f"📝 Assessment: {assessment_title}")
        print(f"❓ Questions: {num_questions}")
        print(f"💯 Points per question: {points_per_question}")
        print(f"{'='*60}\n")
        
        # Step 1: Extract student answers
        print("📄 Step 1: Extracting student answers...")
        student_text = await extract_text_from_file(file)
        student_result = parse_answer_key_flexible(student_text)
        student_answers = student_result["questions"]
        
        if not student_answers:
            raise HTTPException(
                status_code=400, 
                detail="No answers found in the uploaded file. Please ensure the file contains student responses."
            )
        
        print(f"✅ Extracted {len(student_answers)} student answers\n")
        
        # Step 2: Get answer key
        print("🔑 Step 2: Loading answer key...")
        if answer_key_file:
            print("   Using uploaded answer key file...")
            answer_key_text = await extract_text_from_file(answer_key_file)
            answer_key_result = parse_answer_key_flexible(answer_key_text)
            correct_answers = {q["id"]: q["answer"] for q in answer_key_result["questions"]}
        elif answer_key_data:
            print("   Using manual answer key data...")
            answer_key_questions = json.loads(answer_key_data)
            correct_answers = {q["id"]: q["correctAnswer"] for q in answer_key_questions}
        else:
            raise HTTPException(status_code=400, detail="No answer key provided")
        
        print(f"✅ Loaded answer key with {len(correct_answers)} answers\n")
        
        # Step 3: Compare answers
        print("🔄 Step 3: Comparing student answers with answer key...")
        comparison_results = compare_answers(student_answers, correct_answers, points_per_question)
        
        # Step 4: Generate AI feedback
        print("🤖 Step 4: Generating AI feedback...")
        ai_feedback = generate_ai_feedback(comparison_results, subject, assessment_title)
        
        # Step 5: Prepare final results
        print("📊 Step 5: Preparing final results...")
        
        results = {
            "studentName": student_name or "Student",
            "assessmentTitle": assessment_title,
            "subject": subject,
            "percentage": comparison_results["percentage"],
            "pointsEarned": comparison_results["correct_count"] * points_per_question,
            "totalPoints": total_points,
            "correctAnswers": comparison_results["correct_count"],
            "totalQuestions": comparison_results["total_questions"],
            "feedback": ai_feedback,
            "questionBreakdown": [
                {
                    "isCorrect": qr["correct"],
                    "pointsEarned": qr["points_earned"],
                    "pointsPossible": qr["points_possible"],
                    "feedback": f"{'✅ Correct! ' if qr['correct'] else '❌ Incorrect. '}"
                              f"Student answered: {qr['student_answer']}, Correct answer: {qr['correct_answer']}"
                }
                for qr in comparison_results["question_results"]
            ]
        }
        
        print(f"\n{'='*60}")
        print(f"✅ ASSESSMENT CHECK COMPLETED")
        print(f"{'='*60}")
        print(f"📈 Final Score: {results['percentage']}%")
        print(f"💯 Points: {results['pointsEarned']}/{results['totalPoints']}")
        print(f"✅ Correct: {results['correctAnswers']}/{results['totalQuestions']}")
        print(f"{'='*60}\n")
        
        return JSONResponse({
            "success": True,
            "student_name": student_name or "Student",
            "correct_answers": comparison_results["correct_count"],
            "total_questions": comparison_results["total_questions"],
            "percentage": comparison_results["percentage"],
            "question_results": comparison_results["question_results"],
            "results": results,
            "processing_method": "Rule-based Answer Key Comparison",
            "message": "Assessment graded successfully!"
        })
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"\n❌ ERROR in assessment check: {e}\n")
        raise HTTPException(status_code=500, detail=f"Failed to check assessment: {str(e)}")

@router.post("/process-answer-key")
async def process_answer_key(file: UploadFile = File(...)):
    """Process uploaded answer key file"""
    try:
        print(f"🔍 Processing answer key: {file.filename}")
        
        text_content = await extract_text_from_file(file)
        
        if not text_content.strip():
            raise HTTPException(status_code=400, detail="No text content found in file")
        
        result = parse_answer_key_flexible(text_content)
        
        if not result["questions"]:
            raise HTTPException(status_code=400, detail="No questions found in the uploaded file")
        
        return JSONResponse({
            "success": True,
            "questions": result["questions"],
            "format_detected": result["format_type"],
            "total_questions": len(result["questions"]),
            "message": f"Successfully processed {len(result['questions'])} questions"
        })
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process answer key: {str(e)}")

@router.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):
    """Analyze uploaded file to detect content type"""
    try:
        text_content = await extract_text_from_file(file)
        
        if not text_content.strip():
            return JSONResponse({
                "success": True,
                "hasAnswers": False,
                "questions": [],
                "message": "Empty file uploaded"
            })
        
        try:
            result = parse_answer_key_flexible(text_content)
            has_answers = len(result["questions"]) > 0
            questions = result["questions"]
        except:
            has_answers = True
            questions = []
        
        return JSONResponse({
            "success": True,
            "hasAnswers": has_answers,
            "questions": questions,
            "message": "File analyzed successfully"
        })
        
    except Exception as e:
        print(f"⚠️ Analysis error (non-fatal): {e}")
        return JSONResponse({
            "success": True,
            "hasAnswers": True,
            "questions": [],
            "message": "File uploaded successfully"
        })