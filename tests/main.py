from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Student Management API is running"}

def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_invalid_route():
    response = client.get("/invalid")
    assert response.status_code == 404
