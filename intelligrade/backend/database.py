from sqlalchemy.orm import Session

def get_db():
    from .models import SessionLocal
    if SessionLocal is None:
        # Return a mock session for offline mode
        yield None
        return
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()