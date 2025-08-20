import pytest
import responses
from utils.api_client import APIClient


@pytest.fixture
def client():
    return APIClient("https://reqres.in/api")


@responses.activate
def test_get_users_success(client):
    responses.add(
        responses.GET,
        "https://reqres.in/api/users",
        json={"data": [{"id": 1, "name": "John"}]},
        status=200,
    )

    resp = client.get_users()
    assert resp.status_code == 200
    assert resp.json()["data"][0]["name"] == "John"


@responses.activate
def test_get_users_failure(client):
    responses.add(
        responses.GET,
        "https://reqres.in/api/users",
        status=500,
    )

    with pytest.raises(RuntimeError, match="Failed to fetch users"):
        client.get_users()


@responses.activate
def test_create_user_success(client):
    responses.add(
        responses.POST,
        "https://reqres.in/api/users",
        json={"id": "123", "name": "morpheus", "job": "leader"},
        status=201,
    )

    resp = client.create_user("morpheus", "leader")
    assert resp.status_code == 201
    assert resp.json()["job"] == "leader"


@responses.activate
def test_create_user_failure(client):
    responses.add(
        responses.POST,
        "https://reqres.in/api/users",
        status=400,
    )

    with pytest.raises(RuntimeError, match="Failed to create user"):
        client.create_user("neo", "the one")
