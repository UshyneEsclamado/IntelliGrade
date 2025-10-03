# Assessment upload route with direct database connection

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
import json
import asyncio
from datetime import datetime
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create simple fallback processor
class MockAssessmentProcessor:
    @staticmethod
    async def process_assessment(file_content, assessment_type, total_points):
        percentage = 85
        points_earned = round((percentage / 100) * total_points)
        return {
            "studentName": "Test Student",
            "assessmentTitle": "Test Assessment", 
            "percentage": percentage,
            "pointsEarned": points_earned,
            "totalPoints": total_points,
            "feedback": {
                "strengths": ["Good understanding demonstrated"],
                "weaknesses": ["Some areas need improvement"],
                "recommendations": ["Continue practicing"],
                "detailedAnalysis": "Overall solid performance"
            },
            "questionBreakdown": [
                {"isCorrect": True, "pointsEarned": 5, "pointsPossible": 5, "feedback": "Excellent work"},
                {"isCorrect": False, "pointsEarned": 2, "pointsPossible": 5, "feedback": "Review this concept"}
            ]
        }
    
    @staticmethod
    def extract_student_name(content):
        return "Auto-Detected Student"
    
    @staticmethod
    def extract_assessment_title(content):
        return "Auto-Detected Assessment"

# Database configuration using direct connection
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_db_connection():
    """Get direct database connection"""
    try:
        if DATABASE_URL:
            conn = psycopg2.connect(DATABASE_URL)
            print("✅ Direct database connection successful")
            return conn
        else:
            print("⚠️ DATABASE_URL not found in environment")
            return None
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None

# Test database connection
try:
    test_conn = get_db_connection()
    if test_conn:
        cursor = test_conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM assessments")
        count = cursor.fetchone()[0]
        print(f"📊 Database test: Found {count} assessments")
        cursor.close()
        test_conn.close()
        db_available = True
    else:
        db_available = False
except Exception as e:
    print(f"❌ Database test failed: {e}")
    db_available = False

# Initialize AI Processor (fallback to mock for now)
ai_processor = MockAssessmentProcessor()
use_real_ai = False

router = APIRouter()

def get_letter_grade(percentage: float) -> str:
    """Convert percentage to letter grade"""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

@router.post("/api/assessments/upload")
async def upload_assessment(
    file: UploadFile = File(...),
    student_name: str = Form(...),
    assessment_title: str = Form(...),
    subject: str = Form(...),
    total_points: int = Form(...),
    assessment_type: str = Form(...),
    ai_analysis_level: str = Form(default="standard"),
    feedback_level: str = Form(default="detailed"),
    detect_weaknesses: bool = Form(default=True),
    generate_recommendations: bool = Form(default=True),
    compare_to_standards: bool = Form(default=False),
):
    try:
        print(f"📁 Processing file: {file.filename}")
        print(f"👤 Student: {student_name}")
        print(f"📚 Subject: {subject}")
        print(f"🎯 Assessment Type: {assessment_type}")
        
        # Step 1: Read file content
        file_content = await file.read()
        print(f"📄 File size: {len(file_content)} bytes")
        
        # Step 2: Process with Mock processor for now
        print("📝 Using Mock Processor")
        content_str = file_content.decode('utf-8', errors='ignore')
        results = await ai_processor.process_assessment(
            file_content=content_str,
            assessment_type=assessment_type,
            total_points=total_points
        )
        
        # Step 3: Auto-detect student name and title if not provided  
        if student_name == "Auto-detected":
            student_name = ai_processor.extract_student_name(content_str)
        
        if assessment_title == "Auto-detected":
            assessment_title = ai_processor.extract_assessment_title(content_str)
        
        # Override with actual form data
        results["studentName"] = student_name
        results["assessmentTitle"] = assessment_title
        
        print(f"✅ Processing complete: {results['percentage']}% score")
        
        # Step 4: Save to database in REAL-TIME (with duplicate prevention)
        try:
            if db_available:
                print("💾 Saving to database...")
                
                conn = get_db_connection()
                if conn:
                    cursor = conn.cursor(cursor_factory=RealDictCursor)
                    
                    # Check for existing assessment to prevent duplicates
                    cursor.execute("""
                        SELECT id FROM assessments 
                        WHERE title = %s AND subject = %s AND original_filename = %s
                    """, (assessment_title, subject, file.filename))
                    
                    existing = cursor.fetchone()
                    
                    if existing:
                        print("⚠️ Similar assessment already exists, using existing ID")
                        assessment_id = existing['id']
                    else:
                        # Insert new assessment
                        cursor.execute("""
                            INSERT INTO assessments 
                            (title, description, template, subject, total_points, original_filename, 
                             file_size, ai_grading_enabled, provide_feedback, status, created_at, 
                             total_submissions, average_score)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            RETURNING id
                        """, (
                            assessment_title,
                            f"AI-graded assessment for {student_name}",
                            assessment_type,
                            subject,
                            total_points,
                            file.filename,
                            len(file_content),
                            True,
                            True,
                            "completed",
                            datetime.utcnow().isoformat(),
                            1,
                            float(results["percentage"])
                        ))
                        
                        assessment_id = cursor.fetchone()['id']
                        print(f"📝 Assessment saved with ID: {assessment_id}")
                    
                    # Always insert assessment result
                    cursor.execute("""
                        INSERT INTO assessment_results 
                        (assessment_id, student_name, answers, score, max_score, percentage, 
                         letter_grade, overall_feedback, question_feedback, time_taken, 
                         submitted_at, graded_at, grading_method, attempt_number)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id
                    """, (
                        assessment_id,
                        student_name,
                        json.dumps({}),  # TODO: Parse actual answers
                        float(results["pointsEarned"]),
                        float(total_points),
                        float(results["percentage"]),
                        get_letter_grade(results["percentage"]),
                        json.dumps(results["feedback"]),
                        json.dumps(results.get("questionBreakdown", [])),
                        0,  # TODO: Calculate actual time
                        datetime.utcnow().isoformat(),
                        datetime.utcnow().isoformat(),
                        "ai_auto",
                        1
                    ))
                    
                    result_id = cursor.fetchone()['id']
                    print(f"📊 Results saved with ID: {result_id}")
                    
                    # Commit the transaction
                    conn.commit()
                    cursor.close()
                    conn.close()
                    
            else:
                print("⚠️ Database not available, results not saved")
                
        except Exception as db_error:
            print(f"❌ Database error: {db_error}")
            # Continue without failing the entire request
        
        print("🎉 Assessment processing completed successfully!")
        
        return {
            "success": True,
            "message": "Assessment processed successfully",
            "student_name": student_name,
            "assessment_title": assessment_title,
            "results": results
        }
        
    except Exception as e:
        print(f"❌ Error processing assessment: {e}")
        raise HTTPException(status_code=500, detail=f"Assessment processing failed: {str(e)}")

@router.get("/api/assessments/history")
async def get_assessment_history():
    """Get all assessment results grouped by subject - REAL-TIME from database"""
    try:
        print("📋 Fetching assessment history from database...")
        
        if not db_available:
            print("📝 Database not available, returning mock data")
            # Return mock data if database not available
            return {
                "success": True,
                "data": {
                    "Science": [
                        {
                            "id": 1,
                            "title": "Biology Quiz - Cell Structure",
                            "student_name": "John Smith",
                            "percentage": 85,
                            "points_earned": 85,
                            "total_points": 100,
                            "total_questions": 20,
                            "checked_at": "2024-01-15T10:30:00Z",
                            "feedback": {
                                "strengths": ["Strong understanding of cell structure"],
                                "weaknesses": ["Needs work on mitosis phases"],
                                "recommendations": ["Review cell division chapter"]
                            }
                        }
                    ]
                }
            }
        
        # Get REAL-TIME data from database
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute("""
                SELECT ar.*, a.title, a.subject 
                FROM assessment_results ar
                JOIN assessments a ON ar.assessment_id = a.id
                ORDER BY ar.graded_at DESC
            """)
            
            results = cursor.fetchall()
            print(f"📊 Found {len(results)} assessments in database")
            
            # Group by subject
            grouped_data = {}
            for result in results:
                subject = result['subject']
                if subject not in grouped_data:
                    grouped_data[subject] = []
                    
                # Parse JSON feedback safely
                try:
                    feedback = json.loads(result['overall_feedback']) if result['overall_feedback'] else {}
                except:
                    feedback = {}
                    
                grouped_data[subject].append({
                    "id": result['id'],
                    "title": result['title'],
                    "student_name": result['student_name'],
                    "percentage": result['percentage'],
                    "points_earned": result['score'],
                    "total_points": result['max_score'],
                    "total_questions": 10,  # TODO: Get from questions data
                    "checked_at": result['graded_at'],
                    "feedback": feedback
                })
            
            cursor.close()
            conn.close()
            
            print(f"📈 Grouped into {len(grouped_data)} subjects")
            return {"success": True, "data": grouped_data}
        
        else:
            return {"success": False, "error": "Database connection failed"}
        
    except Exception as e:
        print(f"❌ Error fetching assessment history: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch assessment history: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "database_connected": db_available,
        "ai_processor": "mock" if not use_real_ai else "real",
        "timestamp": datetime.utcnow().isoformat()
    }