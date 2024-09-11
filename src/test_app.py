from .app import app
from fastapi.testing import TestingClient

client = TestingClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is Running"}