import pytest
import responses
from utils.api_client import APIClient

@pytest.fixture
def client(base_url):
    return APIClient(base_url)

@responses.activate
def test_get_users_success(client):
    responses.add(
        responses.GET,
        f"{client.base_url}/users",
        json={"data": [{"id": 1, "name": "John Doe"}]},
        status=200,
    )

    resp = client.get_users()
    assert resp.status_code == 200
    assert resp.json()["data"][0]["name"] == "John Doe"

@responses.activate
def test_create_user_success(client):
    responses.add(
        responses.POST,
        f"{client.base_url}/users",
        json={"id": 123, "name": "morpheus", "job": "leader"},
        status=201,
    )

    resp = client.create_user("morpheus", "leader")
    assert resp.status_code == 201
    assert resp.json()["job"] == "leader"
