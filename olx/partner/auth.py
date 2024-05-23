import requests
from .models import AuthResponse, ErrorResponse
from .olx import Olx


class Auth(Olx):
    def __init__(self, client_id, client_secret, custom_scope=None) -> None:
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.current_scope = self.default_scope
        if custom_scope and custom_scope != self.default_scope:
            self.current_scope = custom_scope
        self._access_token = None
        self.expires_in = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, acces_token: str):
        self._access_token = acces_token

    def process_auth(self, request_data: dict) -> AuthResponse:
        endpoint = self.endpoints["auth"]
        response = requests.post(
            self.url + endpoint, json=request_data, headers=self.headers
        )

        data = self._process_response(AuthResponse, response.json())
        if type(data) is ErrorResponse:
            return data

        self.access_token = data.access_token
        self.expires_in = data.expires_in

        return data

    def authenticate(self, code: str = None) -> AuthResponse:
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.current_scope,
        }
        if code:
            data["grant_type"] = "authorization_code"
            data["code"] = code
        else:
            data["grant_type"] = "client_credentials"

        return self.process_auth(request_data=data)

    def refresh(self, refresh_token: str):
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
        }
        return self.process_auth(request_data=data)
