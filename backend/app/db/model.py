# backend/app/db/models.py
from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from app.db.database import Base

class Claim(Base):
    __tablename__ = "claims"
    
    id = Column(Integer, primary_key=True)
    patient_name = Column(String(100))
    claim_amount = Column(Float)
    diagnosis = Column(String(50))
    date_of_service = Column(Date)
    is_valid = Column(Boolean)
    flags = Column(String(200))  # JSON list as string