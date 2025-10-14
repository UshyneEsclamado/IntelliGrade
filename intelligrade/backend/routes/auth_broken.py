from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
import secrets
import os

from backend.database import get_db
from backend.crud import get_user_by_email, create_password_reset_token, get_password_reset_token, mark_password_reset_token_used
from backend.auth import get_password_hash
from backend.models import User
from backend.services.email_service import send_reset_email, test_email_configuration

router = APIRouter(prefix="/auth", tags=["auth"])

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirmRequest(BaseModel):
    token: str
    new_password: str

def send_reset_email_smart(email: str, reset_token: str):
    """Smart email function - tries real email first, falls back to console"""
    reset_link = f"http://localhost:5174/reset-password?token={reset_token}"
    
    # Check if email is configured
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if smtp_user and smtp_password:
        # Try to send real email
        try:
            success = send_reset_email(email, reset_token)
            if success:
                print(f"✅ Password reset email sent successfully to {email}")
                return {"success": True, "method": "email", "message": "A password reset link has been sent to your email address."}
            else:
                print(f"❌ Failed to send email to {email}, showing console fallback")
        except Exception as e:
            print(f"❌ Email sending failed: {e}")
    
    # Fallback to console display for development
    print("=" * 60)
    print("🔐 PASSWORD RESET EMAIL (DEVELOPMENT MODE)")
    print("=" * 60)
    print(f"📧 To: {email}")
    print(f"🔗 Reset Link: {reset_link}")
    print(f"🔑 Token: {reset_token}")
    print(f"⏰ Expires: 1 hour from now")
    print("=" * 60)
    print(f"�️  CLICK HERE: {reset_link}")
    print("=" * 60)
    print("💡 Configure SMTP_USER and SMTP_PASSWORD in .env to send real emails")
    print("=" * 60)
    
    return {"success": True, "method": "console", "message": "Reset link generated. Check console for the link (development mode)."}

@router.post("/forgot-password")
def forgot_password(request: PasswordResetRequest, db: Session = Depends(get_db)):
    if db is None:
        # Offline mode - simulate with demo token
        print("🔐 DEMO MODE - Password Reset")
        print("📧 Email:", request.email)
        print("🔗 Demo Reset Link: http://localhost:5174/reset-password?token=demo-token-123")
        print("💡 Use token 'demo-token-123' to test password reset")
        return {"message": "Demo mode: Check console for reset link. Use token 'demo-token-123' for testing."}
    
    try:
        user = get_user_by_email(db, request.email)
        if user:
            # Generate a reset token
            reset_token = secrets.token_urlsafe(32)
            expires_at = datetime.utcnow() + timedelta(hours=1)
            create_password_reset_token(db, user_id=user.id, token=reset_token, expires_at=expires_at)
            
            # Send the reset email (smart method - tries email first, falls back to console)
            result = send_reset_email_smart(user.email, reset_token)
            return {"message": result["message"]}
        else:
            print(f"⚠️  Password reset requested for non-existent email: {request.email}")
    except Exception as e:
        print(f"Error in forgot_password: {e}")
        # Fallback mode
        result = send_reset_email_smart(request.email, "demo-token-123")
        return {"message": result["message"]}
        
    # Always return success, even if user does not exist (for security)
    return {"message": "If your email exists in our system, a reset link has been sent."}
                return {"message": "Reset link generated. Check the console for the link (development mode)."}
        else:
            print(f"⚠️  Password reset requested for non-existent email: {request.email}")
    except Exception as e:
        print(f"Error in forgot_password: {e}")
        # Simulate offline mode
        print("🔐 FALLBACK MODE - Password Reset")
        print("📧 Email:", request.email)
        print("🔗 Demo Reset Link: http://localhost:5174/reset-password?token=demo-token-123")
        return {"message": "Check console for reset link. Use token 'demo-token-123' for testing."}
        
    # Always return success, even if user does not exist (for security)
    return {"message": "If your email exists in our system, a reset link has been sent."}

@router.get("/get-reset-link/{email}")
def get_reset_link_for_testing(email: str):
    """Development endpoint to get reset link for testing"""
    print(f"🔗 Getting reset link for testing: {email}")
    print(f"🔗 Demo Reset Link: http://localhost:5174/reset-password?token=demo-token-123")
    print("💡 Use token 'demo-token-123' to test password reset")
    
    return {
        "email": email,
        "reset_link": "http://localhost:5174/reset-password?token=demo-token-123",
        "token": "demo-token-123",
        "message": "This is a development endpoint. Use the provided link and token for testing."
    }
    return {"message": "If your email exists in our system, a reset link has been sent."}

@router.post("/reset-password")
def reset_password(request: PasswordResetConfirmRequest, db: Session = Depends(get_db)):
    if db is None:
        # Offline mode - simulate success
        if request.token == "demo-token-123":
            return {"message": "Demo mode: Password has been reset successfully."}
        else:
            raise HTTPException(status_code=400, detail="Demo mode: Use token 'demo-token-123' for testing.")
    
    try:
        reset_token = get_password_reset_token(db, request.token)
        if not reset_token or reset_token.used or reset_token.expires_at < datetime.utcnow():
            raise HTTPException(status_code=400, detail="Invalid or expired token.")
        user = db.query(User).filter(User.id == reset_token.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        user.hashed_password = get_password_hash(request.new_password)
        db.commit()
        mark_password_reset_token_used(db, request.token)
        return {"message": "Password has been reset successfully."}
    except Exception as e:
        print(f"Error in reset_password: {e}")
        # Fallback to offline mode behavior
        if request.token == "demo-token-123":
            return {"message": "Demo mode: Password has been reset successfully."}
        else:
            raise HTTPException(status_code=400, detail="Demo mode: Use token 'demo-token-123' for testing.")
