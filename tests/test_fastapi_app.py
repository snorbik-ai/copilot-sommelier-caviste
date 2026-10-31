from fastapi.testclient import TestClient
from copilot_sommelier_caviste.entrypoints.fastapi_router import app

def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "UP"
    assert data["agent_id"] == "copilot-sommelier-caviste"

def test_handshake_endpoint():
    client = TestClient(app)
    response = client.get("/api/v1/copilot/handshake")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "READY"
