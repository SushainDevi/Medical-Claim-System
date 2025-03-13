# ai_model/nlp/regex_extractor.py
import re

class FieldExtractor:
    PATTERNS = {
        "patient_name": r"Patient Name:\s*([A-Za-z\s]+)",
        "claim_amount": r"Claim Amount:\s*\$?(\d+\.\d{2})",
        "diagnosis": r"Diagnosis:\s*([A-Za-z0-9-]+)",
        "date_of_service": r"Date of Service:\s*(\d{2}/\d{2}/\d{4})"
    }

    @staticmethod
    def extract(text):
        results = {}
        for field, pattern in FieldExtractor.PATTERNS.items():
            match = re.search(pattern, text, re.IGNORECASE)
            results[field] = match.group(1) if match else None
        return results