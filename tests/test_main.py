from fastapi.testclient import TestClient
from personal_api.main import app

client = TestClient(app)