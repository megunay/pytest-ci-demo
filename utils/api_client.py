import requests

class APIClient:
    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url

    def get_users(self, page=1):
        return requests.get(f"{self.base_url}/users", params={"page": page})

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return requests.post(f"{self.base_url}/users", json=payload)
