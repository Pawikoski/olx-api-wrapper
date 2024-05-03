from dataclasses import dataclass


@dataclass
class AuthResponse:
    access_token: str
    expires_in: int
    token_type: str
    scope: str
    refresh_token: str | None = None
