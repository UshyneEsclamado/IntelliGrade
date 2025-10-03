#!/usr/bin/env python3
"""
IntelliGrade Backend Startup Script
This script ensures all dependencies are met and starts the server
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        "fastapi",
        "uvicorn", 
        "python-multipart",
        "supabase",
        "python-dotenv",
        "pydantic"
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✅ {package}")
        except ImportError:
            missing.append(package)
            print(f"❌ {package}")
    
    if missing:
        print(f"\n🔧 Installing missing packages: {', '.join(missing)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
        print("✅ All dependencies installed!")
    
    return True

def check_environment():
    """Check if environment variables are set"""
    from dotenv import load_dotenv
    load_dotenv()
    
    required_env = ["SUPABASE_URL", "SUPABASE_ANON_KEY"]
    missing_env = []
    
    for env_var in required_env:
        value = os.getenv(env_var)
        if value:
            print(f"✅ {env_var}: {value[:20]}...")
        else:
            missing_env.append(env_var)
            print(f"❌ {env_var}: Missing")
    
    if missing_env:
        print(f"\n⚠️ Missing environment variables: {', '.join(missing_env)}")
        print("Please check your .env file")
        return False
    
    return True

def test_database_connection():
    """Test Supabase database connection"""
    try:
        from supabase import create_client
        from dotenv import load_dotenv
        
        load_dotenv()
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_ANON_KEY")
        
        client = create_client(url, key)
        result = client.table("assessments").select("id").limit(1).execute()
        
        print(f"✅ Database connection successful")
        print(f"📊 Found {len(result.data)} test records")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def cleanup_files():
    """Clean up old/duplicate files"""
    backend_dir = Path(__file__).parent
    
    # Files to clean up
    cleanup_files = [
        "main.py",
        "main_clean.py", 
        "main_fixed.py",
        "routes/assessments.py",
        "routes/assessments_fixed.py"
    ]
    
    for file_path in cleanup_files:
        full_path = backend_dir / file_path
        if full_path.exists():
            try:
                full_path.unlink()
                print(f"🗑️ Removed: {file_path}")
            except Exception as e:
                print(f"⚠️ Could not remove {file_path}: {e}")

def start_server():
    """Start the FastAPI server"""
    print("\n🚀 Starting IntelliGrade API Server...")
    
    # Rename files to correct names
    backend_dir = Path(__file__).parent
    
    # Use the final main file
    main_final = backend_dir / "main_final.py"
    main_py = backend_dir / "main.py"
    
    if main_final.exists():
        if main_py.exists():
            main_py.unlink()
        main_final.rename(main_py)
        print("✅ Main file updated")
    
    # Use the clean assessments file
    routes_dir = backend_dir / "routes"
    routes_dir.mkdir(exist_ok=True)
    
    assessments_clean = routes_dir / "assessments_clean.py"
    assessments_py = routes_dir / "assessments.py"
    
    if assessments_clean.exists():
        if assessments_py.exists():
            assessments_py.unlink()
        assessments_clean.rename(assessments_py)
        print("✅ Routes file updated")
    
    # Start the server
    try:
        import uvicorn
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        return False

def main():
    """Main startup function"""
    print("🔧 IntelliGrade Backend Startup Check")
    print("=" * 50)
    
    # Step 1: Check dependencies
    print("\n📦 Checking Dependencies...")
    if not check_dependencies():
        return False
    
    # Step 2: Check environment
    print("\n🔧 Checking Environment...")
    if not check_environment():
        return False
    
    # Step 3: Test database
    print("\n🗄️ Testing Database Connection...")
    if not test_database_connection():
        print("⚠️ Database connection failed, but server can still start")
    
    # Step 4: Clean up old files
    print("\n🧹 Cleaning up old files...")
    cleanup_files()
    
    # Step 5: Start server
    start_server()

if __name__ == "__main__":
    main()