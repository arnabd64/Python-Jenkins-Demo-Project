from .app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    print(app.version)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is Running"}