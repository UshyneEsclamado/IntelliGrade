# backend/app/main.py
from fastapi import FastAPI, File, UploadFile, Form, Depends
from sqlalchemy.orm import Session
from models import Assessment, Base
from database import SessionLocal, engine
import json
from supabase import create_client

# Supabase connection
url = "https://aheyuzhgllmwntjdaimi.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFoZXl1emhnbGxtd250amRhaW1pIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUyMjcwMTQsImV4cCI6MjA3MDgwMzAxNH0.ajUd44jZfcj8TLOxqI0t2Fd75wE8NYQa03BEfuEbwdk"
supabase = create_client(url, key)

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Upload assessment and store it in the database
@app.post("/upload-assessment/")
async def upload_assessment(
    title: str = Form(...),
    template: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    content = await file.read()
    # Store the uploaded assessment in the database
    assessment = Assessment(title=title, template=template, content=content.decode('utf-8'))
    db.add(assessment)
    db.commit()
    db.refresh(assessment)

    return {"message": "Assessment uploaded successfully", "assessment_id": assessment.id}

# Grading function (just an example for multiple-choice)
@app.post("/grade-assessment/{assessment_id}")
async def grade_assessment(assessment_id: int, answers: list, db: Session = Depends(get_db)):
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()

    if not assessment:
        return {"error": "Assessment not found"}

    # Grade the assessment based on the template (e.g., multiple-choice)
    if assessment.template == "multiple-choice":
        return grade_multiple_choice(assessment, answers)
    else:
        return {"error": "Unsupported template type"}

def grade_multiple_choice(assessment, answers):
    # Example grading logic for multiple-choice assessments
    correct_answers = json.loads(assessment.content)  # assuming the content is a JSON with question-answer pairs
    score = sum([1 for i, answer in enumerate(answers) if answer == correct_answers[i]['correct']])

    feedback = f"Your score is {score}/{len(correct_answers)}."
    return {"score": score, "feedback": feedback}

@app.get("/assessment/{id}/results")
async def get_assessment_results(id: int, db: Session = Depends(get_db)):
    # Example: Query the database to get the results for the assessment by ID
    assessment = db.query(Assessment).filter(Assessment.id == id).first()
    
    if not assessment:
        return {"error": "Assessment not found"}
    
    # You can modify this part to actually pull results from the database, for now we use a mock
    results = [
        {"studentName": "Juan Dela Cruz", "score": 18, "feedback": "Excellent!", "answers": [...]},
        {"studentName": "Maria Santos", "score": 15, "feedback": "Good job!", "answers": [...]},
    ]

    return {"title": assessment.title, "maxScore": 20, "results": results}
