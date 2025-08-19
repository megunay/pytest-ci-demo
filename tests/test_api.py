import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def client():
    return APIClient()

def test_get_users_success(client):
    resp = client.get_users()
    assert resp.status_code == 200
    data = resp.json()
    assert "data" in data
    assert isinstance(data["data"], list)

def test_get_single_user_success(client):
    resp = client.get_user(2)
    assert resp.status_code == 200
    data = resp.json()
    assert data["data"]["id"] == 2

def test_create_user_success(client):
    resp = client.create_user("morpheus", "leader")
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    assert "id" in data
