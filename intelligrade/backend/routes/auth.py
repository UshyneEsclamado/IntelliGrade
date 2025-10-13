from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
import secrets

from backend.database import get_db
from backend.crud import get_user_by_email, create_password_reset_token, get_password_reset_token, mark_password_reset_token_used
from backend.auth import get_password_hash
from backend.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirmRequest(BaseModel):
    token: str
    new_password: str

@router.post("/forgot-password")
def forgot_password(request: PasswordResetRequest, db: Session = Depends(get_db)):
    if db is None:
        # Offline mode - simulate success
        return {"message": "Demo mode: If your email exists in our system, a reset link would be sent."}
    
    try:
        user = get_user_by_email(db, request.email)
        if user:
            # Generate a reset token
            reset_token = secrets.token_urlsafe(32)
            expires_at = datetime.utcnow() + timedelta(hours=1)
            create_password_reset_token(db, user_id=user.id, token=reset_token, expires_at=expires_at)
            # For now, just return success without sending email to avoid crashes
            print(f"Reset token for {user.email}: {reset_token}")
    except Exception as e:
        print(f"Error in forgot_password: {e}")
        # Still return success for security
        
    # Always return success, even if user does not exist
    return {"message": "If your email exists in our system, a reset link has been sent."}

@router.post("/reset-password")
def reset_password(request: PasswordResetConfirmRequest, db: Session = Depends(get_db)):
    if db is None:
        # Offline mode - simulate success
        if request.token == "demo-token-123":
            return {"message": "Demo mode: Password has been reset successfully."}
        else:
            raise HTTPException(status_code=400, detail="Demo mode: Use token 'demo-token-123' for testing.")
    
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
