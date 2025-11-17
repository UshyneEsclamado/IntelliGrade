"""
IntelliGrade Backend Server
Run this file to start the FastAPI backend server
FILE LOCATION: backend/run.py
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Starting IntelliGrade Backend Server...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔄 Auto-reload enabled for development")
    print("-" * 50)
    
    # FIXED: Changed from "app.main:app" to just "main:app"
    uvicorn.run(
        "main:app",  # ← This is the fix!
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )