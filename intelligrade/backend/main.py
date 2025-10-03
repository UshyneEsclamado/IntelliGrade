# Main FastAPI application - CLEAN VERSION
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Import routes
from routes.assessments import router as assessments_router

app = FastAPI(title="IntelliGrade API", version="1.0.0")

# Add CORS middleware for Vue.js frontend  
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(assessments_router)

@app.get("/")
async def root():
    return {"message": "IntelliGrade API is running", "status": "online"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "IntelliGrade API"}

if __name__ == "__main__":
    port = int(os.getenv("API_PORT", 8000))
    host = os.getenv("API_HOST", "0.0.0.0")
    
    print("🚀 IntelliGrade API Starting...")
    print(f"📋 OpenAI API Key: {'✅ Configured' if os.getenv('OPENAI_API_KEY') else '❌ Missing'}")
    print(f"🗄️ Supabase URL: {'✅ Configured' if os.getenv('SUPABASE_URL') else '❌ Missing'}")
    print(f"🌐 Server will start on {host}:{port}")
    
    uvicorn.run(
        "main:app", 
        host=host, 
        port=port, 
        reload=True,
        log_level="info"
    )