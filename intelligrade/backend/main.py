"""
IntelliGrade AI Assessment System - Main FastAPI Application
Complete implementation with all features integrated
"""

import os
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
import json
import asyncio

# FastAPI imports
from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form, status, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
import uvicorn

# Database imports
from sqlalchemy.orm import Session
from database import get_db

# Local imports
from config import settings
from auth import get_current_user, create_access_token, verify_password, get_password_hash
from ai_grading_engine import ai_grading_engine
from file_processor import file_processor
from utils.feedback_generator import FeedbackGenerator
from utils.analytics import GradingAnalytics
from utils.validators import ValidationUtils
import crud
import models
import schemas

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(settings.log_file, mode='a'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Create upload directories
os.makedirs(settings.upload_dir, exist_ok=True)
os.makedirs(os.path.dirname(settings.log_file), exist_ok=True)

# Initialize FastAPI app
app = FastAPI(
    title="IntelliGrade AI Assessment System",
    description="AI-powered assessment grading and feedback system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Initialize utilities
security = HTTPBearer()
feedback_generator = FeedbackGenerator()
analytics = GradingAnalytics()
validator = ValidationUtils()

# WebSocket Connection Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        self.active_connections[user_id] = websocket
    
    def disconnect(self, user_id: int):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
    
    async def send_personal_message(self, message: str, user_id: int):
        if user_id in self.active_connections:
            websocket = self.active_connections[user_id]
            await websocket.send_text(message)
    
    async def send_message_to_conversation(self, message: dict, conversation_id: int, sender_id: int, db: Session):
        # Get conversation participants
        conversation = crud.get_conversation(db, conversation_id)
        if conversation:
            recipient_id = conversation.user2_id if conversation.user1_id == sender_id else conversation.user1_id
            
            # Send to recipient if online
            if recipient_id in self.active_connections:
                await self.send_personal_message(json.dumps(message), recipient_id)

manager = ConnectionManager()

# Pydantic models for API
class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "teacher"

class AssessmentCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    instructions: Optional[str] = ""
    time_limit: Optional[int] = None
    questions: List[Dict[str, Any]]
    settings: Optional[Dict[str, Any]] = {}

class StudentSubmission(BaseModel):
    student_id: int
    student_answers: List[str]
    submission_time: Optional[datetime] = None

class GradingRequest(BaseModel):
    assessment_id: int
    student_id: int
    student_answers: List[str]
    learning_style: Optional[str] = "visual"

# API Routes

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "IntelliGrade AI Assessment System",
        "version": "1.0.0",
        "status": "active",
        "features": [
            "AI-powered grading",
            "Multiple question types",
            "Personalized feedback",
            "Performance analytics",
            "File upload support"
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        # Test database connection
        from database import engine
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow(),
            "database": "connected",
            "ai_service": "available"
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service unhealthy"
        )

# Authentication endpoints
@app.post("/api/auth/login")
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """User login endpoint"""
    try:
        # In a real implementation, you'd check against your user database
        # For demo purposes, we'll create a simple authentication
        user = db.query(models.User).filter(models.User.username == user_data.username).first()
        
        if not user or not verify_password(user_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        # Create access token
        access_token = create_access_token(data={"sub": user.username})
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username,
            "role": user.role
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login failed"
        )

@app.post("/api/auth/register")
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """User registration endpoint"""
    try:
        # Check if user already exists
        existing_user = db.query(models.User).filter(
            (models.User.username == user_data.username) |
            (models.User.email == user_data.email)
        ).first()
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or email already registered"
            )
        
        # Create new user
        password_hash = get_password_hash(user_data.password)
        new_user = models.User(
            username=user_data.username,
            email=user_data.email,
            password_hash=password_hash,
            role=user_data.role
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        logger.info(f"New user registered: {user_data.username}")
        
        return {
            "message": "User registered successfully",
            "user_id": new_user.id,
            "username": new_user.username
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Registration error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed"
        )

# Assessment endpoints
@app.post("/api/assessments/upload")
async def upload_assessment(
    file: UploadFile = File(...),
    title: Optional[str] = Form(None),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Upload and process assessment file"""
    try:
        # Validate file
        file_content = await file.read()
        temp_file_path = file_processor.save_uploaded_file(file_content, file.filename)
        
        validation_result = file_processor.validate_file(temp_file_path)
        if not validation_result['valid']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid file: {', '.join(validation_result['errors'])}"
            )
        
        # Process the file
        assessment_data = await file_processor.process_uploaded_file(temp_file_path)
        
        # Override title if provided
        if title:
            assessment_data['title'] = title
        
        # Validate assessment data
        validation = validator.validate_assessment_data(assessment_data)
        if not validation['valid']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid assessment data: {', '.join(validation['errors'])}"
            )
        
        # Get user ID
        user = db.query(models.User).filter(models.User.username == current_user).first()
        
        # Create assessment in database
        assessment_data['created_by'] = user.id
        assessment_data['created_at'] = datetime.utcnow()
        assessment_data['questions'] = json.dumps(assessment_data['questions'])
        
        assessment = crud.create_assessment(db, assessment_data)
        
        logger.info(f"Assessment uploaded: {assessment.title} by {current_user}")
        
        return {
            "message": "Assessment uploaded successfully",
            "assessment_id": assessment.id,
            "title": assessment.title,
            "questions_count": len(json.loads(assessment.questions)),
            "total_points": assessment.total_points,
            "validation_warnings": validation.get('warnings', []),
            "suggestions": validation.get('suggestions', [])
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Assessment upload error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Upload failed: {str(e)}"
        )

@app.post("/api/assessments")
async def create_assessment(
    assessment_data: AssessmentCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create new assessment"""
    try:
        # Validate assessment data
        validation = validator.validate_assessment_data(assessment_data.dict())
        if not validation['valid']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid assessment: {', '.join(validation['errors'])}"
            )
        
        # Get user
        user = db.query(models.User).filter(models.User.username == current_user).first()
        
        # Create assessment
        assessment_dict = assessment_data.dict()
        assessment_dict['created_by'] = user.id
        assessment_dict['created_at'] = datetime.utcnow()
        assessment_dict['questions'] = json.dumps(assessment_dict['questions'])
        assessment_dict['total_points'] = sum(q.get('points', 1) for q in assessment_data.questions)
        
        assessment = crud.create_assessment(db, assessment_dict)
        
        logger.info(f"Assessment created: {assessment.title} by {current_user}")
        
        return {
            "message": "Assessment created successfully",
            "assessment_id": assessment.id,
            "title": assessment.title,
            "questions_count": len(assessment_data.questions),
            "total_points": assessment.total_points
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Assessment creation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Assessment creation failed"
        )

@app.get("/api/assessments")
async def list_assessments(
    skip: int = 0,
    limit: int = 100,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List user's assessments"""
    try:
        user = db.query(models.User).filter(models.User.username == current_user).first()
        assessments = crud.get_assessments_by_teacher(db, user.id, skip, limit)
        
        return {
            "assessments": [
                {
                    "id": a.id,
                    "title": a.title,
                    "description": a.description,
                    "questions_count": len(json.loads(a.questions)),
                    "total_points": a.total_points,
                    "created_at": a.created_at,
                    "status": "active"
                }
                for a in assessments
            ],
            "count": len(assessments)
        }
        
    except Exception as e:
        logger.error(f"Error listing assessments: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve assessments"
        )

@app.get("/api/assessments/{assessment_id}")
async def get_assessment(
    assessment_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific assessment details"""
    try:
        assessment = crud.get_assessment(db, assessment_id)
        
        if not assessment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assessment not found"
            )
        
        questions = json.loads(assessment.questions)
        
        return {
            "id": assessment.id,
            "title": assessment.title,
            "description": assessment.description,
            "instructions": assessment.instructions,
            "questions": questions,
            "total_points": assessment.total_points,
            "time_limit": assessment.time_limit,
            "created_at": assessment.created_at,
            "settings": assessment.settings or {}
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving assessment: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve assessment"
        )

# Grading endpoints
@app.post("/api/assessments/{assessment_id}/ai-grade")
async def ai_grade_assessment(
    assessment_id: int,
    grading_request: GradingRequest,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Grade assessment using AI"""
    try:
        # Get assessment
        assessment = crud.get_assessment(db, assessment_id)
        if not assessment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assessment not found"
            )
        
        questions = json.loads(assessment.questions)
        
        # Validate student answers
        validation = validator.validate_student_answers(grading_request.student_answers, questions)
        if not validation['valid']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid answers: {', '.join(validation['errors'])}"
            )
        
        # Grade the assessment
        logger.info(f"Starting AI grading for assessment {assessment_id}, student {grading_request.student_id}")
        
        grading_result = await ai_grading_engine.grade_assessment(
            questions=questions,
            student_answers=grading_request.student_answers,
            student_id=grading_request.student_id,
            assessment_id=assessment_id
        )
        
        # Validate grading result
        result_validation = validator.validate_grading_result(grading_result)
        if not result_validation['valid']:
            logger.warning(f"Grading result validation failed: {result_validation['errors']}")
        
        # Save results to database
        result_data = {
            'assessment_id': assessment_id,
            'student_id': grading_request.student_id,
            'score': grading_result['total_points_earned'],
            'total_points': grading_result['total_points_possible'],
            'percentage': grading_result['percentage'],
            'letter_grade': grading_result['letter_grade'],
            'question_results': json.dumps(grading_result['question_results']),
            'overall_feedback': json.dumps(grading_result['overall_feedback']),
            'ai_confidence': grading_result['ai_confidence'],
            'needs_review': grading_result['needs_manual_review'],
            'graded_at': datetime.utcnow(),
            'grading_model': grading_result['grading_model']
        }
        
        assessment_result = crud.create_assessment_result(db, result_data)
        
        # Generate personalized feedback if enabled
        if settings.enable_personalized_feedback:
            feedback_data = {
                'assessment_result_id': assessment_result.id,
                'student_id': grading_request.student_id,
                'feedback_type': 'comprehensive',
                'feedback_content': json.dumps(grading_result['overall_feedback']),
                'learning_style': grading_request.learning_style,
                'generated_at': datetime.utcnow()
            }
            crud.create_student_feedback(db, feedback_data)
        
        logger.info(f"AI grading completed: {grading_result['percentage']:.1f}% ({grading_result['letter_grade']})")
        
        return {
            "message": "Assessment graded successfully",
            "result_id": assessment_result.id,
            "grading_result": grading_result,
            "validation_warnings": result_validation.get('warnings', [])
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"AI grading error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Grading failed: {str(e)}"
        )

@app.post("/api/assessments/{assessment_id}/batch-grade")
async def batch_grade_assessment(
    assessment_id: int,
    submissions: List[StudentSubmission],
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Grade multiple student submissions in batch"""
    try:
        assessment = crud.get_assessment(db, assessment_id)
        if not assessment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assessment not found"
            )
        
        questions = json.loads(assessment.questions)
        results = []
        
        logger.info(f"Starting batch grading for {len(submissions)} submissions")
        
        # Process submissions with concurrency control
        semaphore = asyncio.Semaphore(settings.max_concurrent_gradings)
        
        async def grade_single_submission(submission: StudentSubmission):
            async with semaphore:
                try:
                    grading_result = await ai_grading_engine.grade_assessment(
                        questions=questions,
                        student_answers=submission.student_answers,
                        student_id=submission.student_id,
                        assessment_id=assessment_id
                    )
                    
                    # Save to database
                    result_data = {
                        'assessment_id': assessment_id,
                        'student_id': submission.student_id,
                        'score': grading_result['total_points_earned'],
                        'total_points': grading_result['total_points_possible'],
                        'percentage': grading_result['percentage'],
                        'letter_grade': grading_result['letter_grade'],
                        'question_results': json.dumps(grading_result['question_results']),
                        'overall_feedback': json.dumps(grading_result['overall_feedback']),
                        'ai_confidence': grading_result['ai_confidence'],
                        'needs_review': grading_result['needs_manual_review'],
                        'graded_at': datetime.utcnow(),
                        'grading_model': grading_result['grading_model']
                    }
                    
                    assessment_result = crud.create_assessment_result(db, result_data)
                    
                    return {
                        'student_id': submission.student_id,
                        'result_id': assessment_result.id,
                        'percentage': grading_result['percentage'],
                        'letter_grade': grading_result['letter_grade'],
                        'status': 'completed'
                    }
                    
                except Exception as e:
                    logger.error(f"Error grading student {submission.student_id}: {e}")
                    return {
                        'student_id': submission.student_id,
                        'status': 'failed',
                        'error': str(e)
                    }
        
        # Grade all submissions concurrently
        tasks = [grade_single_submission(submission) for submission in submissions]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Process results
        successful_grades = [r for r in results if isinstance(r, dict) and r.get('status') == 'completed']
        failed_grades = [r for r in results if isinstance(r, dict) and r.get('status') == 'failed']
        
        logger.info(f"Batch grading completed: {len(successful_grades)} successful, {len(failed_grades)} failed")
        
        return {
            "message": "Batch grading completed",
            "total_submissions": len(submissions),
            "successful_grades": len(successful_grades),
            "failed_grades": len(failed_grades),
            "results": results
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Batch grading error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch grading failed: {str(e)}"
        )

# Results and Analytics endpoints
@app.get("/api/assessments/{assessment_id}/results")
async def get_assessment_results(
    assessment_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all results for an assessment"""
    try:
        results = crud.get_assessment_results(db, assessment_id)
        
        # Calculate statistics
        assessment_stats = analytics.calculate_assessment_statistics([
            {
                'percentage': r.percentage,
                'letter_grade': r.letter_grade,
                'question_results': json.loads(r.question_results) if r.question_results else []
            }
            for r in results
        ])
        
        return {
            "assessment_id": assessment_id,
            "results": [
                {
                    "id": r.id,
                    "student_id": r.student_id,
                    "score": r.score,
                    "total_points": r.total_points,
                    "percentage": r.percentage,
                    "letter_grade": r.letter_grade,
                    "graded_at": r.graded_at,
                    "needs_review": r.needs_review,
                    "ai_confidence": r.ai_confidence
                }
                for r in results
            ],
            "statistics": assessment_stats
        }
        
    except Exception as e:
        logger.error(f"Error retrieving assessment results: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve results"
        )

@app.get("/api/students/{student_id}/results")
async def get_student_results(
    student_id: int,
    assessment_id: Optional[int] = None,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get results for a specific student"""
    try:
        results = crud.get_student_results(db, student_id, assessment_id)
        
        if not results:
            return {
                "student_id": student_id,
                "results": [],
                "message": "No results found"
            }
        
        # Calculate student progress
        student_progress = analytics.calculate_student_progress([
            {
                'percentage': r.percentage,
                'letter_grade': r.letter_grade,
                'graded_at': r.graded_at.isoformat() if r.graded_at else '',
                'question_results': json.loads(r.question_results) if r.question_results else []
            }
            for r in results
        ])
        
        return {
            "student_id": student_id,
            "results": [
                {
                    "id": r.id,
                    "assessment_id": r.assessment_id,
                    "score": r.score,
                    "total_points": r.total_points,
                    "percentage": r.percentage,
                    "letter_grade": r.letter_grade,
                    "graded_at": r.graded_at,
                    "overall_feedback": json.loads(r.overall_feedback) if r.overall_feedback else None
                }
                for r in results
            ],
            "progress_analytics": student_progress
        }
        
    except Exception as e:
        logger.error(f"Error retrieving student results: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve student results"
        )

@app.get("/api/assessments/{assessment_id}/results/{student_id}")
async def get_detailed_result(
    assessment_id: int,
    student_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get detailed result for specific student and assessment"""
    try:
        results = crud.get_student_results(db, student_id, assessment_id)
        
        if not results:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Result not found"
            )
        
        result = results[0]  # Get most recent result
        
        return {
            "result_id": result.id,
            "assessment_id": result.assessment_id,
            "student_id": result.student_id,
            "score": result.score,
            "total_points": result.total_points,
            "percentage": result.percentage,
            "letter_grade": result.letter_grade,
            "question_results": json.loads(result.question_results) if result.question_results else [],
            "overall_feedback": json.loads(result.overall_feedback) if result.overall_feedback else None,
            "ai_confidence": result.ai_confidence,
            "needs_review": result.needs_review,
            "graded_at": result.graded_at,
            "grading_model": result.grading_model
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving detailed result: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve result details"
        )

# Feedback endpoints
@app.get("/api/students/{student_id}/feedback")
async def get_student_feedback(
    student_id: int,
    assessment_result_id: Optional[int] = None,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get feedback for student"""
    try:
        feedback_records = crud.get_student_feedback(db, student_id, assessment_result_id)
        
        return {
            "student_id": student_id,
            "feedback": [
                {
                    "id": f.id,
                    "assessment_result_id": f.assessment_result_id,
                    "feedback_type": f.feedback_type,
                    "feedback_content": json.loads(f.feedback_content) if f.feedback_content else {},
                    "learning_style": f.learning_style,
                    "generated_at": f.generated_at
                }
                for f in feedback_records
            ]
        }
        
    except Exception as e:
        logger.error(f"Error retrieving student feedback: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve feedback"
        )

# Analytics endpoints
@app.get("/api/analytics/class-report")
async def get_class_report(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate comprehensive class analytics report"""
    try:
        # Get user
        user = db.query(models.User).filter(models.User.username == current_user).first()
        
        # Get all assessments by this teacher
        assessments = crud.get_assessments_by_teacher(db, user.id)
        
        # Get all results for these assessments
        all_results = []
        for assessment in assessments:
            results = crud.get_assessment_results(db, assessment.id)
            for result in results:
                all_results.append({
                    'assessment_id': result.assessment_id,
                    'student_id': result.student_id,
                    'percentage': result.percentage,
                    'letter_grade': result.letter_grade,
                    'graded_at': result.graded_at.isoformat() if result.graded_at else '',
                    'question_results': json.loads(result.question_results) if result.question_results else []
                })
        
        # Generate class report
        class_report = analytics.generate_class_report(all_results)
        
        return {
            "report_generated_at": datetime.utcnow(),
            "teacher_id": user.id,
            "assessments_analyzed": len(assessments),
            "class_report": class_report
        }
        
    except Exception as e:
        logger.error(f"Error generating class report: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not generate class report"
        )

# File management endpoints
@app.delete("/api/files/cleanup")
async def cleanup_old_files(
    days: int = 30,
    current_user: str = Depends(get_current_user)
):
    """Clean up old uploaded files"""
    try:
        deleted_count = file_processor.cleanup_old_files(days)
        
        return {
            "message": f"Cleanup completed",
            "files_deleted": deleted_count,
            "days_cutoff": days
        }
        
    except Exception as e:
        logger.error(f"File cleanup error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File cleanup failed"
        )

# Validation endpoints
@app.post("/api/validate/assessment")
async def validate_assessment_data(
    assessment_data: Dict[str, Any],
    current_user: str = Depends(get_current_user)
):
    """Validate assessment data before creation"""
    try:
        # Sanitize input
        clean_data = validator.sanitize_input(assessment_data)
        
        # Validate
        validation_result = validator.validate_assessment_data(clean_data)
        
        return {
            "validation_result": validation_result,
            "is_valid": validation_result['valid'],
            "error_count": len(validation_result.get('errors', [])),
            "warning_count": len(validation_result.get('warnings', [])),
            "suggestion_count": len(validation_result.get('suggestions', []))
        }
        
    except Exception as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Validation failed"
        )

# Messaging API Endpoints

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, db: Session = Depends(get_db)):
    """WebSocket endpoint for real-time messaging"""
    await manager.connect(websocket, user_id)
    try:
        while True:
            # Receive message from WebSocket
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            if message_data.get("type") == "message":
                # Create new message in database
                conversation_id = message_data.get("conversation_id")
                content = message_data.get("content")
                receiver_id = message_data.get("receiver_id")
                
                if conversation_id and content and receiver_id:
                    # Save message to database
                    new_message = crud.create_message(
                        db=db,
                        conversation_id=conversation_id,
                        sender_id=user_id,
                        receiver_id=receiver_id,
                        content=content
                    )
                    
                    # Prepare response message
                    response_message = {
                        "type": "new_message",
                        "message": {
                            "id": new_message.id,
                            "conversation_id": new_message.conversation_id,
                            "sender_id": new_message.sender_id,
                            "receiver_id": new_message.receiver_id,
                            "content": new_message.content,
                            "created_at": new_message.created_at.isoformat(),
                            "is_read": new_message.is_read
                        }
                    }
                    
                    # Send to both sender and receiver
                    await manager.send_message_to_conversation(
                        response_message, conversation_id, user_id, db
                    )
                    # Echo back to sender
                    await manager.send_personal_message(
                        json.dumps(response_message), user_id
                    )
            
            elif message_data.get("type") == "mark_read":
                conversation_id = message_data.get("conversation_id")
                if conversation_id:
                    crud.mark_messages_as_read(db, conversation_id, user_id)
                    
    except WebSocketDisconnect:
        manager.disconnect(user_id)

@app.get("/api/conversations", response_model=List[schemas.Conversation])
async def get_conversations(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all conversations for the current user"""
    user_id = current_user["user_id"]
    conversations = crud.get_user_conversations(db, user_id)
    return conversations

@app.get("/api/conversations/{conversation_id}/messages", response_model=List[schemas.Message])
async def get_conversation_messages(
    conversation_id: int,
    skip: int = 0,
    limit: int = 50,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get messages for a specific conversation"""
    # Verify user is part of the conversation
    conversation = crud.get_conversation(db, conversation_id)
    user_id = current_user["user_id"]
    
    if not conversation or (conversation.user1_id != user_id and conversation.user2_id != user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied to this conversation"
        )
    
    messages = crud.get_conversation_messages(db, conversation_id, skip, limit)
    
    # Mark messages as read
    crud.mark_messages_as_read(db, conversation_id, user_id)
    
    return messages

@app.post("/api/conversations", response_model=schemas.Conversation)
async def create_or_get_conversation(
    participant_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new conversation or get existing one between two users"""
    user_id = current_user["user_id"]
    
    # Check if conversation already exists
    existing_conversation = crud.get_conversation_by_users(db, user_id, participant_id)
    if existing_conversation:
        return existing_conversation
    
    # Create new conversation
    new_conversation = crud.create_conversation(db, user_id, participant_id)
    return new_conversation

@app.post("/api/messages", response_model=schemas.Message)
async def send_message(
    message_data: schemas.MessageCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Send a new message (REST endpoint as fallback)"""
    user_id = current_user["user_id"]
    receiver_id = message_data.receiver_id
    
    # Get or create conversation
    conversation = crud.get_conversation_by_users(db, user_id, receiver_id)
    if not conversation:
        conversation = crud.create_conversation(db, user_id, receiver_id)
    
    # Create message
    new_message = crud.create_message(
        db=db,
        conversation_id=conversation.id,
        sender_id=user_id,
        receiver_id=receiver_id,
        content=message_data.content
    )
    
    # Send real-time notification if receiver is online
    response_message = {
        "type": "new_message",
        "message": {
            "id": new_message.id,
            "conversation_id": new_message.conversation_id,
            "sender_id": new_message.sender_id,
            "receiver_id": new_message.receiver_id,
            "content": new_message.content,
            "created_at": new_message.created_at.isoformat(),
            "is_read": new_message.is_read
        }
    }
    
    await manager.send_personal_message(
        json.dumps(response_message), receiver_id
    )
    
    return new_message

@app.get("/api/users", response_model=List[schemas.User])
async def get_users(
    role: Optional[str] = None,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get list of users (for finding conversation participants)"""
    if role:
        users = crud.get_users_by_role(db, role)
    else:
        users = crud.get_users_by_role(db, "teacher") + crud.get_users_by_role(db, "student")
    
    # Remove current user from list
    user_id = current_user["user_id"]
    users = [user for user in users if user.id != user_id]
    
    return users

@app.get("/api/users/search", response_model=List[schemas.User])
async def search_users(
    query: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Search for users by name"""
    if not query or len(query.strip()) < 2:
        raise HTTPException(
            status_code=400, 
            detail="Search query must be at least 2 characters long"
        )
    
    users = crud.search_users_by_name(db, query.strip())
    
    # Remove current user from results
    user_id = current_user["user_id"]
    users = [user for user in users if user.id != user_id]
    
    return users

@app.post("/api/conversations/create", response_model=schemas.Conversation)
async def create_conversation(
    other_user_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new conversation with another user"""
    user_id = current_user["user_id"]
    
    if user_id == other_user_id:
        raise HTTPException(
            status_code=400,
            detail="Cannot create conversation with yourself"
        )
    
    # Check if conversation already exists
    existing_conversation = crud.get_conversation_between_users(db, user_id, other_user_id)
    if existing_conversation:
        return existing_conversation
    
    # Create new conversation
    conversation = crud.create_conversation(db, user_id, other_user_id)
    return conversation

@app.get("/api/unread-count")
async def get_unread_count(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get count of unread messages for current user"""
    user_id = current_user["user_id"]
    count = crud.get_unread_message_count(db, user_id)
    return {"unread_count": count}

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    logger.warning(f"HTTP {exc.status_code}: {exc.detail} - {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status_code": exc.status_code}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler"""
    logger.error(f"Unhandled exception: {str(exc)} - {request.url}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500}
    )

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Application startup tasks"""
    logger.info("IntelliGrade API starting up...")
    logger.info(f"AI Model: {settings.ai_model}")
    logger.info(f"Upload directory: {settings.upload_dir}")
    logger.info("API is ready to accept requests")

@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown tasks"""
    logger.info("IntelliGrade API shutting down...")

# Main execution
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
        log_level=settings.log_level.lower()
    )