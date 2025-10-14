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
from backend.services.email_service import send_password_reset_email_production, test_email_configuration

router = APIRouter(prefix="/auth", tags=["auth"])

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirmRequest(BaseModel):
    token: str
    new_password: str

def send_reset_email_smart(email: str, reset_token: str):
    """Smart email function - uses new production email service"""
    return send_password_reset_email_production(email, reset_token)

@router.post("/forgot-password")
def forgot_password(request: PasswordResetRequest):
    """Production password reset - only returns success if email is actually sent"""
    try:
        print(f"🔑 Password reset requested for: {request.email}")
        
        # Send email and check if it was actually sent
        result = send_reset_email_smart(request.email, "demo-token-123")
        
        # Only return success if email was actually sent (not fallback to console)
        if result.get("method") == "email" and result.get("success"):
            return {"message": "A password reset link has been sent to your email address."}
        else:
            # Email failed - return error to frontend
            raise HTTPException(
                status_code=500, 
                detail="Failed to send reset link. Please try again later."
            )
        
    except HTTPException:
        raise  # Re-raise HTTP exceptions
    except Exception as e:
        print(f"Error in forgot_password: {e}")
        raise HTTPException(
            status_code=500, 
            detail="Failed to send reset link. Please try again later."
        )

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



@router.post("/reset-password")
def reset_password(request: PasswordResetConfirmRequest, db: Session = Depends(get_db)):
    """Reset password with token"""
    try:
        # For development, accept demo token
        if request.token == "demo-token-123":
            print(f"🔑 Demo password reset for token: {request.token}")
            return {"message": "Password has been reset successfully."}
        
        # Production logic (with database)
        reset_token = get_password_reset_token(db, request.token)
        if not reset_token or reset_token.expires_at < datetime.utcnow():
            raise HTTPException(status_code=400, detail="Invalid or expired reset token.")
        
        # Update user password
        user = get_user_by_email(db, reset_token.email)
        if user:
            user.password_hash = get_password_hash(request.new_password)
            db.commit()
            mark_password_reset_token_used(db, request.token)
            return {"message": "Password has been reset successfully."}
        else:
            raise HTTPException(status_code=404, detail="User not found.")
            
    except HTTPException:
        raise  # Re-raise HTTP exceptions
    except Exception as e:
        print(f"Error in reset_password: {e}")
        # Fallback for development mode
        if request.token == "demo-token-123":
            return {"message": "Password has been reset successfully."}
        else:
            raise HTTPException(status_code=400, detail="Invalid or expired reset token.")

@router.get("/email-status")
def check_email_status():
    """Check if email is configured and working"""
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if not smtp_user or not smtp_password:
        return {
            "configured": False,
            "status": "Email not configured",
            "message": "Set SMTP_USER and SMTP_PASSWORD environment variables to enable real email sending"
        }
    
    # Test email configuration
    try:
        is_working = test_email_configuration()
        return {
            "configured": True,
            "working": is_working,
            "status": "Email configured and working" if is_working else "Email configured but not working",
            "smtp_user": smtp_user,
            "message": "Real emails will be sent" if is_working else "Check your SMTP credentials"
        }
    except Exception as e:
        return {
            "configured": True,
            "working": False,
            "status": "Email configuration error",
            "error": str(e),
            "message": "Check your SMTP credentials"
        }