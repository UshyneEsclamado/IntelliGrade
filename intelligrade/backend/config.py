from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()
import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database - FIXED: Removed "DATABASE_URL=" prefix
    database_url: str = "postgresql://postgres:777thesisDEFENDEDlLOcKtaponsusi!!@db.aheyuzhgllmwntjdaimi.supabase.co:5432/postgres"
    supabase_url: str = "https://aheyuzhgllmwntjdaimi.supabase.co"
    supabase_anon_key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFoZXl1emhnbGxtd250amRhaW1pIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUyMjcwMTQsImV4cCI6MjA3MDgwMzAxNH0.ajUd44jZfcj8TLOxqI0t2Fd75wE8NYQa03BEfuEbwdk"
    supabase_service_key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFoZXl1emhnbGxtd250amRhaW1pIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NTIyNzAxNCwiZXhwIjoyMDcwODAzMDE0fQ._dIfbZHMSE6TvXvLLIJiHu5NPnDvsLIl-b7CqIp20lk"

    # AI Configuration
    openai_api_key: str = "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"
    ai_model: str = "gpt-4"
    ai_temperature: float = 0.3
    max_tokens: int = 1000
    
    # File Upload
    upload_dir: str = "uploads/assessments"
    max_file_size: int = 10485760  # 10MB
    allowed_extensions: str = ".txt,.csv,.json,.docx,.pdf"
    
    # Security - FIXED: Added secret_key with default value
    secret_key: str = "your-super-secret-key-change-this-in-production-intelligrade-2024"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # API
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"
    
    # Grading
    default_ai_confidence_threshold: float = 0.7
    manual_review_threshold: float = 0.5
    batch_grading_delay: float = 0.5
    max_concurrent_gradings: int = 5
    
    # Feedback
    enable_instant_feedback: bool = True
    enable_personalized_feedback: bool = True
    default_learning_style: str = "visual"
    feedback_language: str = "en"
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/intelligrade.log"
    
    class Config:
        env_file = ".env"
        
    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    @property
    def allowed_extensions_list(self) -> List[str]:
        return [ext.strip() for ext in self.allowed_extensions.split(",")]

# Global settings instance
settings = Settings()