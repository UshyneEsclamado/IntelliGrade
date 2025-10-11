"""
IntelliGrade Backend Server
Run this file to start the FastAPI backend server
"""

import uvicorn
from app.main import app

if __name__ == "__main__":
    print("🚀 Starting IntelliGrade Backend Server...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔄 Auto-reload enabled for development")
    print("-" * 50)
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )