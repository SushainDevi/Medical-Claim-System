from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_invoice():
    with open("test_invoice.pdf", "rb") as f:
        response = client.post(
            "/api/v1/upload",
            files={"file": ("test_invoice.pdf", f)}
        )
    assert response.status_code == 200
    assert "patient_name" in response.json()["extracted_data"]