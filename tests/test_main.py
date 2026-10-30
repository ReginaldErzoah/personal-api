from fastapi.testclient import TestClient

from personal_api.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message" : "Welcome to my Personal CV API"
        }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status" : "healthy"
        }


def test_profile_endpoint():
    response = client.get("/profile")

    assert response.status_code == 200
    assert response.json()["name"] == "Reginald Erzoah"
    assert response.json()["profession"] == "Data Professional"


def test_skills_endpoint():
    response = client.get("/skills")
    
    assert response.status_code == 200

    skills = response.json()
    assert isinstance(skills, list)
    assert skills[0]["name"] == "Python"


def test_skills_by_name_insensitive():
    response = client.get("/skills/python")

    assert response.status_code == 200

    assert response.json()["name"] == "Python"


def test_projects_endpoint():
    response = client.get("/projects")

    assert response.status_code == 200

    projects = response.json()
    assert isinstance(projects, list)


def test_projects_by_id():
    response = client.get("/projects/by_id/1")

    assert response.status_code == 200


def test_certifications_endpoint():
    response = client.get("/certifications")

    assert response.status_code == 200

    certifications = response.json()

    assert isinstance(certifications, list)
    assert certifications[0]["name"] == "Machine Learning Specialization"


def test_certifications_by_id():
    