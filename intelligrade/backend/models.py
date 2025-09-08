# backend/app/models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    template = Column(String)  # Template type (e.g., multiple-choice)
    content = Column(Text)  # Store content as plain text or JSON
