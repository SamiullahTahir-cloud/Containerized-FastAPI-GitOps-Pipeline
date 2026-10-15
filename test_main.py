from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "GitOps Pipeline Deployed via Render", "status": "success"}

def test_read_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.1", "environment": "production"}
