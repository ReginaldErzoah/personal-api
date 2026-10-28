from fastapi.testclient import TestClient
from personal_api.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client("/health")

    assert response.status_code == 200
    