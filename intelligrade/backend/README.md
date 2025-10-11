# IntelliGrade Backend Setup Guide

## Quick Start

1. **Navigate to backend directory:**

   ```bash
   cd c:\Users\Administrator\Desktop\INTELLIGRADE\intelligrade\backend
   ```

2. **Install dependencies:**

   ```bash
   pip install fastapi uvicorn python-multipart
   ```

3. **Start the server:**

   ```bash
   python run.py
   ```

4. **Verify server is running:**
   - Open browser: http://localhost:8000
   - Should see: {"message": "IntelliGrade API is running!", "version": "1.0.0"}
   - API docs: http://localhost:8000/docs

## Troubleshooting

### "Failed to fetch" Error

- Make sure backend server is running at http://localhost:8000
- Check if port 8000 is available
- Try restarting the server

### Port Already in Use

```bash
# Kill process on port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

### Module Import Errors

```bash
# Install missing modules
pip install fastapi uvicorn python-multipart
```

## File Structure

```
backend/
├── app/
│   ├── __init__.py          # Python module marker
│   ├── main.py              # FastAPI app with CORS
│   └── api/
│       ├── __init__.py      # Python module marker
│       └── endpoints/
│           ├── __init__.py  # Python module marker
│           └── assessments.py  # API endpoints
├── run.py                   # Server startup script
└── requirements.txt         # Dependencies
```

## Why **init**.py files?

These are required by Python to treat directories as modules. They're not duplicates - each one marks its directory as a Python package.

## No OCR Used

We don't use OCR (Optical Character Recognition). We only process text files (.txt), not images. The system expects text-based answer keys and student responses.
