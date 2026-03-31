from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books", json={
        "title": "Test",
        "author": "Me",
        "description": "Test",
        "status": "available",
        "year": 2024
    })
    assert response.status_code == 201

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200