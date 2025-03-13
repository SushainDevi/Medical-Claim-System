# backend/app/api/claims_router.py
from fastapi import APIRouter, UploadFile, File
from app.db.database import SessionLocal
from ai_model.ocr.tesseract import ocr_pipeline
from ai_model.nlp.regex_extractor import FieldExtractor
from ai_model.classifier.rules import FraudDetector
import boto3

router = APIRouter()

# Initialize S3 client
s3 = boto3.client("s3")

@router.post("/upload")
async def upload_claim(file: UploadFile = File(...)):
    # Step 1: Save file to S3
    s3.upload_fileobj(
        file.file,
        "medical-claims-bucket",  # Replace with your S3 bucket name
        file.filename
    )
    
    # Step 2: Process OCR
    text = ocr_pipeline(f"/tmp/{file.filename}")
    extracted = FieldExtractor.extract(text)
    
    # Step 3: Fraud checks
    is_valid, flags = FraudDetector.rule_based_checks(extracted)
    
    # Step 4: Save to DB
    db = SessionLocal()
    # ... (implement database saving logic)
    
    return {
        "extracted_data": extracted,
        "valid": is_valid,
        "flags": flags
    }