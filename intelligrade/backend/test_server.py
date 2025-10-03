# Simple test endpoint without database dependencies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form
import uvicorn

app = FastAPI()

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.options("/api/assessments/upload")
async def upload_options():
    return JSONResponse(
        content={"message": "CORS preflight"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.post("/api/assessments/upload")
async def upload_assessment(
    file: UploadFile = File(...),
    student_name: str = Form(...),
    subject: str = Form(...),
    total_points: int = Form(...),
    assessment_type: str = Form(...),
):
    print(f"📁 Received file: {file.filename}")
    print(f"👤 Student: {student_name}")
    print(f"📚 Subject: {subject}")
    
    # Simple mock response
    response_data = {
        "success": True,
        "message": "Assessment processed successfully",
        "student_name": student_name,
        "results": {
            "studentName": student_name,
            "percentage": 85,
            "pointsEarned": 85,
            "totalPoints": total_points,
            "feedback": {
                "strengths": ["Good work!"],
                "weaknesses": ["Room for improvement"],
                "recommendations": ["Keep studying"]
            }
        }
    }
    
    return JSONResponse(
        content=response_data,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return JSONResponse(
        content={"message": "Simple test server working!", "timestamp": "2024-01-15"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

if __name__ == "__main__":
    print("🚀 Simple Test Server Starting on port 8000")
    uvicorn.run("test_server:app", host="0.0.0.0", port=8000, reload=True)