import requests


class APIClient:
    """
    A simple API client wrapper around `requests`.

    Attributes:
        base_url (str): The base URL for the API.
        headers (dict): Optional default headers sent with each request.
    """

    def __init__(self, base_url: str, headers: dict | None = None):
        self.base_url = base_url.rstrip("/")  # prevent double slashes
        self.headers = headers or {"Content-Type": "application/json"}

    def get_users(self):
        """
        Fetch all users from the API.

        Returns:
            requests.Response: The HTTP response object.
        """
        url = f"{self.base_url}/users"
        try:
            resp = requests.get(url, headers=self.headers, timeout=5)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch users: {e}") from e

    def create_user(self, name: str, job: str):
        """
        Create a new user in the API.

        Args:
            name (str): The user's name.
            job (str): The user's job title.

        Returns:
            requests.Response: The HTTP response object.
        """
        url = f"{self.base_url}/users"
        payload = {"name": name, "job": job}
        try:
            resp = requests.post(url, json=payload, headers=self.headers, timeout=5)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to create user: {e}") from e
