from sqlalchemy.orm import Session
from sqlalchemy import and_, func, desc, or_
from backend.models import User, PasswordResetToken

# Password Reset Token CRUD
def create_password_reset_token(db: Session, user_id: int, token: str, expires_at):
    reset_token = PasswordResetToken(user_id=user_id, token=token, expires_at=expires_at)
    db.add(reset_token)
    db.commit()
    db.refresh(reset_token)
    return reset_token

def get_password_reset_token(db: Session, token: str):
    return db.query(PasswordResetToken).filter(PasswordResetToken.token == token, PasswordResetToken.used == False).first()

def mark_password_reset_token_used(db: Session, token: str):
    reset_token = db.query(PasswordResetToken).filter(PasswordResetToken.token == token).first()
    if reset_token:
        reset_token.used = True
        db.commit()
    return reset_token
from typing import List, Dict, Optional
import json
from datetime import datetime

# Assessment CRUD
def create_assessment(db: Session, assessment_data: dict):
    assessment = Assessment(**assessment_data)
    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    return assessment

def get_assessment(db: Session, assessment_id: int):
    return db.query(Assessment).filter(Assessment.id == assessment_id).first()

def get_assessments_by_teacher(db: Session, teacher_id: int, skip: int = 0, limit: int = 100):
    return db.query(Assessment).filter(
        Assessment.created_by == teacher_id
    ).offset(skip).limit(limit).all()

def update_assessment(db: Session, assessment_id: int, update_data: dict):
    db.query(Assessment).filter(Assessment.id == assessment_id).update(update_data)
    db.commit()
    return get_assessment(db, assessment_id)

# Assessment Results CRUD
def create_assessment_result(db: Session, result_data: dict):
    # Check if result already exists for this student and assessment
    existing = db.query(AssessmentResult).filter(
        and_(
            AssessmentResult.assessment_id == result_data["assessment_id"],
            AssessmentResult.student_id == result_data["student_id"]
        )
    ).first()
    
    if existing:
        # Update existing result
        for key, value in result_data.items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        # Create new result
        result = AssessmentResult(**result_data)
        db.add(result)
        db.commit()
        db.refresh(result)
        return result

def get_student_results(db: Session, student_id: int, assessment_id: int = None):
    query = db.query(AssessmentResult).filter(AssessmentResult.student_id == student_id)
    if assessment_id:
        query = query.filter(AssessmentResult.assessment_id == assessment_id)
    return query.order_by(desc(AssessmentResult.graded_at)).all()

def get_assessment_results(db: Session, assessment_id: int):
    return db.query(AssessmentResult).filter(
        AssessmentResult.assessment_id == assessment_id
    ).order_by(desc(AssessmentResult.percentage)).all()

# Analytics and Reporting
def get_student_performance_summary(db: Session, student_id: int):
    """Get comprehensive performance summary for a student"""
    results = db.query(AssessmentResult).filter(
        AssessmentResult.student_id == student_id
    ).all()
    
    if not results:
        return None
    
    total_assessments = len(results)
    avg_percentage = sum(r.percentage for r in results) / total_assessments
    avg_score = sum(r.score for r in results) / total_assessments
    
    grade_counts = {}
    for result in results:
        grade = result.letter_grade
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    return {
        "student_id": student_id,
        "total_assessments": total_assessments,
        "average_percentage": round(avg_percentage, 2),
        "average_score": round(avg_score, 2),
        "grade_distribution": grade_counts,
        "recent_results": [
            {
                "assessment_id": r.assessment_id,
                "score": r.score,
                "percentage": r.percentage,
                "graded_at": r.graded_at
            }
            for r in sorted(results, key=lambda x: x.graded_at, reverse=True)[:5]
        ]
    }

def get_assessment_analytics(db: Session, assessment_id: int):
    """Get comprehensive analytics for an assessment"""
    return db.query(GradingAnalytics).filter(
        GradingAnalytics.assessment_id == assessment_id
    ).first()

# Feedback CRUD
def create_student_feedback(db: Session, feedback_data: dict):
    feedback = StudentFeedback(**feedback_data)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def get_student_feedback(db: Session, student_id: int, assessment_result_id: int = None):
    query = db.query(StudentFeedback).filter(StudentFeedback.student_id == student_id)
    if assessment_result_id:
        query = query.filter(StudentFeedback.assessment_result_id == assessment_result_id)
    return query.all()

# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: dict):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users_by_role(db: Session, role: str, skip: int = 0, limit: int = 100):
    return db.query(User).filter(User.role == role).offset(skip).limit(limit).all()

def search_users_by_name(db: Session, query: str, skip: int = 0, limit: int = 20):
    """Search users by name (case-insensitive)"""
    search_term = f"%{query.lower()}%"
    return db.query(User).filter(
        func.lower(User.name).like(search_term)
    ).offset(skip).limit(limit).all()

# Conversation CRUD
def get_conversation(db: Session, conversation_id: int):
    return db.query(Conversation).filter(Conversation.id == conversation_id).first()

def get_conversation_by_users(db: Session, user1_id: int, user2_id: int):
    return db.query(Conversation).filter(
        or_(
            and_(Conversation.user1_id == user1_id, Conversation.user2_id == user2_id),
            and_(Conversation.user1_id == user2_id, Conversation.user2_id == user1_id)
        )
    ).first()

def get_conversation_between_users(db: Session, user1_id: int, user2_id: int):
    """Alias for get_conversation_by_users for API compatibility"""
    return get_conversation_by_users(db, user1_id, user2_id)

def create_conversation(db: Session, user1_id: int, user2_id: int):
    conversation = Conversation(user1_id=user1_id, user2_id=user2_id)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

def get_user_conversations(db: Session, user_id: int):
    return db.query(Conversation).filter(
        or_(Conversation.user1_id == user_id, Conversation.user2_id == user_id)
    ).order_by(desc(Conversation.updated_at)).all()

# Message CRUD
def create_message(db: Session, conversation_id: int, sender_id: int, receiver_id: int, content: str):
    message = Message(
        conversation_id=conversation_id,
        sender_id=sender_id,
        receiver_id=receiver_id,
        content=content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    
    # Update conversation's last message and timestamp
    conversation = get_conversation(db, conversation_id)
    conversation.last_message_id = message.id
    conversation.updated_at = datetime.utcnow()
    db.commit()
    
    return message

def get_conversation_messages(db: Session, conversation_id: int, skip: int = 0, limit: int = 50):
    return db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).order_by(Message.created_at).offset(skip).limit(limit).all()

def mark_messages_as_read(db: Session, conversation_id: int, user_id: int):
    db.query(Message).filter(
        and_(
            Message.conversation_id == conversation_id,
            Message.receiver_id == user_id,
            Message.is_read == False
        )
    ).update({Message.is_read: True})
    db.commit()

def get_unread_message_count(db: Session, user_id: int):
    return db.query(Message).filter(
        and_(Message.receiver_id == user_id, Message.is_read == False)
    ).count()
    return query.all()