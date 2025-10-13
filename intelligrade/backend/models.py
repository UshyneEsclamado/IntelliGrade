from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime, timedelta

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:777thesisDEFENDEDlLOcKtaponsusi!!@db.aheyuzhgllmwntjdaimi.supabase.co:5432/postgres"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    print(f"⚠️ Database connection failed: {e}")
    # Create a mock SessionLocal for offline mode
    SessionLocal = None

Base = declarative_base()

# --- Model Classes ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String, unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

class AssessmentResult(Base):
    __tablename__ = "assessment_results"
    id = Column(Integer, primary_key=True, index=True)
    assessment_id = Column(Integer, ForeignKey("assessments.id"))
    student_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer)
    percentage = Column(Integer)
    graded_at = Column(DateTime, default=datetime.utcnow)
    
class StudentFeedback(Base):
    __tablename__ = "student_feedback"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    assessment_id = Column(Integer, ForeignKey("assessments.id"))
    feedback_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    title = Column(String)
    template = Column(String)  # Template type (e.g., multiple-choice)
    content = Column(Text)  # Store content as plain text or JSON
