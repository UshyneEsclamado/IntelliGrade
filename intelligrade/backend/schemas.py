from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# AnswerKey schemas
class AnswerKeyBase(BaseModel):
    title: str
    subject: str
    assessment_type: str
    num_questions: int
    total_points: int
    questions_data: dict  # Assuming this contains the answers

class AnswerKeyCreate(AnswerKeyBase):
    pass

class AnswerKey(AnswerKeyBase):
    id: int
    created_at: datetime
    updated_at: datetime
    usage_count: int
    
    class Config:
        from_attributes = True

# UploadedAssessment schemas
class UploadedAssessmentBase(BaseModel):
    assessment_title: str
    subject: str
    assessment_data: dict  # Store the content (questions, answers, etc.)

class UploadedAssessmentCreate(UploadedAssessmentBase):
    pass

class UploadedAssessment(UploadedAssessmentBase):
    id: int
    answer_key_id: int
    original_filename: str
    file_path: str
    file_size: int
    uploaded_at: datetime
    processed_at: Optional[datetime]
    
    class Config:
        from_attributes = True

# GradingResult schemas
class GradingResultBase(BaseModel):
    student_name: str
    assessment_title: str
    subject: str
    total_questions: int
    correct_answers: int
    incorrect_answers: int
    score: float
    max_score: float
    percentage: float
    letter_grade: str
    question_breakdown: List[dict]  # Breakdown for each question (e.g., correct answer, points earned)
    ai_used: bool
    ai_model: Optional[str]
    ai_confidence: Optional[float]
    processing_time: Optional[float]

class GradingResultCreate(GradingResultBase):
    pass

class GradingResult(GradingResultBase):
    id: int
    uploaded_assessment_id: int
    graded_at: datetime
    reviewed_by: Optional[int]
    reviewed_at: Optional[datetime]
    
    class Config:
        from_attributes = True

