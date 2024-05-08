import requests
from .olx import Olx
from dacite import from_dict
from .models import AuthResponse


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

    def authenticate(self, code: str = None):
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

        endpoint = self.endpoints["auth"]
        response = requests.post(self.url + endpoint, json=data)

        # TODO: Handle errors

        data = from_dict(AuthResponse, response.json())

        self.access_token = data.access_token
        self.expires_in = data.expires_in
