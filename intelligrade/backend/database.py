from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os

# Database URL from environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "")

# FIXED: Remove check_same_thread (only for SQLite, not PostgreSQL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create the SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """Yield a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()