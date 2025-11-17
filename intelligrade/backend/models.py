from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, DECIMAL, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

from database import engine

Base = declarative_base()

# ==========================================
# MODELS MATCHING YOUR DATABASE SCHEMA
# ==========================================

class AnswerKey(Base):
    """Answer Keys Table - stores correct answers"""
    __tablename__ = "answer_keys"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    subject = Column(String(100), nullable=False)
    assessment_type = Column(String(50), nullable=False)
    
    original_filename = Column(String(255))
    file_path = Column(String(500))
    file_size = Column(Integer)
    
    num_questions = Column(Integer, nullable=False)
    questions_data = Column(JSON, nullable=False)
    total_points = Column(Integer, nullable=False)
    
    created_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    is_active = Column(Boolean, default=True)
    usage_count = Column(Integer, default=0)
    
    # Relationships
    uploaded_assessments = relationship("UploadedAssessment", back_populates="answer_key")
    grading_results = relationship("GradingResult", back_populates="answer_key")


class UploadedAssessment(Base):
    """Uploaded Assessments Table - stores uploaded assessment details"""
    __tablename__ = "uploaded_assessments"
    
    id = Column(Integer, primary_key=True, index=True)
    answer_key_id = Column(Integer, ForeignKey("answer_keys.id", ondelete="CASCADE"))
    
    original_filename = Column(String(255))
    file_path = Column(String(500))
    file_size = Column(Integer)
    
    assessment_title = Column(String(255), nullable=False)
    subject = Column(String(100), nullable=False)
    
    assessment_data = Column(JSON, nullable=False)
    
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime)
    
    # Relationships
    answer_key = relationship("AnswerKey", back_populates="uploaded_assessments")
    grading_results = relationship("GradingResult", back_populates="uploaded_assessment")


class GradingResult(Base):
    """Grading Results Table - stores graded data"""
    __tablename__ = "grading_results"
    
    id = Column(Integer, primary_key=True, index=True)
    uploaded_assessment_id = Column(Integer, ForeignKey("uploaded_assessments.id", ondelete="CASCADE"))
    answer_key_id = Column(Integer, ForeignKey("answer_keys.id", ondelete="SET NULL"))
    
    student_name = Column(String(255), nullable=False)
    assessment_title = Column(String(255), nullable=False)
    subject = Column(String(100), nullable=False)
    
    total_questions = Column(Integer, nullable=False)
    correct_answers = Column(Integer, nullable=False)
    incorrect_answers = Column(Integer, nullable=False)
    score = Column(DECIMAL(5, 2), nullable=False)
    max_score = Column(DECIMAL(5, 2), nullable=False)
    percentage = Column(DECIMAL(5, 2), nullable=False)
    letter_grade = Column(String(2))
    
    question_breakdown = Column(JSON, nullable=False)
    
    strengths = Column(JSON)
    weaknesses = Column(JSON)
    recommendations = Column(JSON)
    detailed_analysis = Column(Text)
    
    ai_used = Column(Boolean, default=False)
    ai_model = Column(String(50))
    ai_confidence = Column(DECIMAL(3, 2))
    processing_time = Column(DECIMAL(8, 2))
    
    grading_method = Column(String(50), default='rule-based')
    
    graded_at = Column(DateTime, default=datetime.utcnow)
    reviewed_by = Column(Integer)
    reviewed_at = Column(DateTime)
    
    # Relationships
    uploaded_assessment = relationship("UploadedAssessment", back_populates="grading_results")
    answer_key = relationship("AnswerKey", back_populates="grading_results")


# ==========================================
# CREATE TABLES FUNCTION
# ==========================================

def init_db():
    """Initialize database tables - Run this once!"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ All database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

if __name__ == "__main__":
    print("Creating database tables...")
    init_db()