# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use your actual Supabase URL directly
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:777thesisDEFENDEDlLOcKtaponsusi!!@db.aheyuzhgllmwntjdaimi.supabase.co:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()