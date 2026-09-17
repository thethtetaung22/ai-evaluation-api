from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_evaluations():
    response = client.post(
        "/evaluations", json={"prompt": "Hi, there!", "model": "gpt-4o"}
    )
    assert response.status_code == 202
    body = response.json()
    assert "id" in body
    assert body["status"] == "queued"


def test_create_evaluations_empty_prompt_is_rejected():
    response = client.post("/evaluations", json={"prompt": "", "model": "gpt-4o"})
    assert response.status_code == 422

