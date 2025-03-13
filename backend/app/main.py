# backend/app/main.py
from fastapi import FastAPI, UploadFile, File
from app.api import claims_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Medical Claim Processing System"}

app.include_router(claims_router, prefix="/api/v1")