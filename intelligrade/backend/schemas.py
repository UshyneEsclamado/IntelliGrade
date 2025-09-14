from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Message schemas
class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    receiver_id: int

class Message(MessageBase):
    id: int
    conversation_id: int
    sender_id: int
    receiver_id: int
    is_read: bool
    created_at: datetime
    sender: User
    receiver: User
    
    class Config:
        from_attributes = True

# Conversation schemas
class ConversationBase(BaseModel):
    pass

class Conversation(ConversationBase):
    id: int
    user1_id: int
    user2_id: int
    last_message_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    user1: User
    user2: User
    last_message: Optional[Message]
    messages: List[Message] = []
    
    class Config:
        from_attributes = True

# WebSocket message schemas
class WSMessage(BaseModel):
    type: str  # 'message', 'typing', 'read_receipt'
    conversation_id: Optional[int] = None
    content: Optional[str] = None
    receiver_id: Optional[int] = None

class WSResponse(BaseModel):
    type: str
    data: dict