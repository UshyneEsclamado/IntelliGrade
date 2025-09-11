from sqlalchemy.orm import Session
from sqlalchemy import and_, func, desc
from models import Assessment, AssessmentResult, StudentFeedback, GradingAnalytics
from typing import List, Dict, Optional
import json

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