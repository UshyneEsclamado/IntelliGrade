from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["auth"])

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirmRequest(BaseModel):
    token: str
    new_password: str

@router.post("/forgot-password")
def forgot_password(request: PasswordResetRequest):
    return {"message": "Demo mode: If your email exists in our system, a reset link would be sent."}

@router.post("/reset-password")
def reset_password(request: PasswordResetConfirmRequest):
    if request.token == "demo-token-123":
        return {"message": "Demo mode: Password has been reset successfully."}
    else:
        return {"error": "Demo mode: Use token 'demo-token-123' for testing."}