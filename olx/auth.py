import requests
from dacite import from_dict
from models import AuthResponse


class Auth:
    def __init__(self, client_id, client_secret, scope=None) -> None:
        self.url = "https://www.olx.pl"
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = "read write v2"
        if scope and scope != self.scope:
            self.scope = scope

    def authenticate(self, code: str = None):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.scope,
        }
        if code:
            data["grant_type"] = "authorization_code"
            data["code"] = code
        else:
            data["grant_type"] = "client_credentials"

        endpoint = "/api/open/oauth/token/"
        response = requests.post(self.url + endpoint, json=data)
        print(response)
        print(response.text)

        # Handle status codes
        return from_dict(AuthResponse, response.json())


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()
    auth = Auth(
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET"),
    )
    auth.authenticate()
