from sqlalchemy.orm import Session
from sqlalchemy import and_, func, desc, or_
from models import AnswerKey, UploadedAssessment, GradingResult  # FIXED: Remove 'backend.' prefix

# Answer Key CRUD
def create_answer_key(db: Session, answer_key_data: dict):
    """Create a new answer key"""
    answer_key = AnswerKey(**answer_key_data)
    db.add(answer_key)
    db.commit()
    db.refresh(answer_key)
    return answer_key

def get_answer_key(db: Session, answer_key_id: int):
    """Get answer key by ID"""
    return db.query(AnswerKey).filter(AnswerKey.id == answer_key_id).first()

def get_answer_keys(db: Session, skip: int = 0, limit: int = 100):
    """Get all answer keys"""
    return db.query(AnswerKey).filter(AnswerKey.is_active == True).offset(skip).limit(limit).all()

def update_answer_key(db: Session, answer_key_id: int, update_data: dict):
    """Update an answer key"""
    db.query(AnswerKey).filter(AnswerKey.id == answer_key_id).update(update_data)
    db.commit()
    return get_answer_key(db, answer_key_id)

def delete_answer_key(db: Session, answer_key_id: int):
    """Soft delete an answer key"""
    db.query(AnswerKey).filter(AnswerKey.id == answer_key_id).update({"is_active": False})
    db.commit()
    return True

# Uploaded Assessment CRUD
def create_uploaded_assessment(db: Session, assessment_data: dict):
    """Create a new uploaded assessment"""
    uploaded_assessment = UploadedAssessment(**assessment_data)
    db.add(uploaded_assessment)
    db.commit()
    db.refresh(uploaded_assessment)
    return uploaded_assessment

def get_uploaded_assessment(db: Session, assessment_id: int):
    """Get uploaded assessment by ID"""
    return db.query(UploadedAssessment).filter(UploadedAssessment.id == assessment_id).first()

def get_uploaded_assessments(db: Session, skip: int = 0, limit: int = 100):
    """Get all uploaded assessments"""
    return db.query(UploadedAssessment).offset(skip).limit(limit).all()

def update_uploaded_assessment(db: Session, assessment_id: int, update_data: dict):
    """Update an uploaded assessment"""
    db.query(UploadedAssessment).filter(UploadedAssessment.id == assessment_id).update(update_data)
    db.commit()
    return get_uploaded_assessment(db, assessment_id)

# Grading Results CRUD
def create_grading_result(db: Session, result_data: dict):
    """Create or update a grading result"""
    # Check if result already exists for this uploaded assessment
    existing = db.query(GradingResult).filter(
        GradingResult.uploaded_assessment_id == result_data.get("uploaded_assessment_id")
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
        grading_result = GradingResult(**result_data)
        db.add(grading_result)
        db.commit()
        db.refresh(grading_result)
        return grading_result

def get_grading_result(db: Session, result_id: int):
    """Get grading result by ID"""
    return db.query(GradingResult).filter(GradingResult.id == result_id).first()

def get_grading_results(db: Session, uploaded_assessment_id: int = None, skip: int = 0, limit: int = 100):
    """Get grading results, optionally filtered by uploaded_assessment_id"""
    query = db.query(GradingResult)
    
    if uploaded_assessment_id:
        query = query.filter(GradingResult.uploaded_assessment_id == uploaded_assessment_id)
    
    return query.order_by(desc(GradingResult.graded_at)).offset(skip).limit(limit).all()

def get_all_grading_results(db: Session, skip: int = 0, limit: int = 100):
    """Get all grading results"""
    return db.query(GradingResult).order_by(desc(GradingResult.graded_at)).offset(skip).limit(limit).all()

# Analytics and Reporting
def get_assessment_analytics(db: Session, uploaded_assessment_id: int):
    """Get comprehensive analytics for an uploaded assessment"""
    return db.query(GradingResult).filter(
        GradingResult.uploaded_assessment_id == uploaded_assessment_id
    ).first()

def get_student_performance(db: Session, student_name: str):
    """Get all grading results for a specific student"""
    return db.query(GradingResult).filter(
        GradingResult.student_name == student_name
    ).order_by(desc(GradingResult.graded_at)).all()

def get_subject_statistics(db: Session, subject: str):
    """Get statistics for a specific subject"""
    return db.query(
        func.count(GradingResult.id).label('total_assessments'),
        func.avg(GradingResult.percentage).label('average_percentage'),
        func.max(GradingResult.percentage).label('highest_percentage'),
        func.min(GradingResult.percentage).label('lowest_percentage')
    ).filter(GradingResult.subject == subject).first()

def get_recent_assessments(db: Session, limit: int = 10):
    """Get most recent assessments"""
    return db.query(GradingResult).order_by(desc(GradingResult.graded_at)).limit(limit).all()

# Search and Filter
def search_grading_results(db: Session, search_query: str, skip: int = 0, limit: int = 100):
    """Search grading results by student name or assessment title"""
    search_term = f"%{search_query}%"
    return db.query(GradingResult).filter(
        or_(
            GradingResult.student_name.ilike(search_term),
            GradingResult.assessment_title.ilike(search_term)
        )
    ).offset(skip).limit(limit).all()