#!/usr/bin/env python3
"""
Database migration script for IntelliGrade
Run this to set up your database tables
"""

from sqlalchemy import create_engine
from models import Base
from config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def migrate_database():
    """Create all database tables"""
    try:
        # DEBUG: Print the actual URL being used
        print(f"🔍 DEBUG: Using database URL: {settings.database_url}")
        
        engine = create_engine(settings.database_url)
        
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database migration completed successfully!")
        
        return True
    except Exception as e:
        logger.error(f"❌ Database migration failed: {e}")
        return False

if __name__ == "__main__":
    migrate_database()