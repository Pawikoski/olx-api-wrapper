from .olx import Olx
from .models import AuthenticatedUser, User, UsersAccountBalance
from typing import List


class Users(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_authenticated_user(self) -> AuthenticatedUser:
        endpoint = self.endpoints["users"]["get_authenticated_user"]
        response = self._get(endpoint)
        return self._process_response(AuthenticatedUser, response, "data")

    def get_user(self, user_id: int) -> User:
        endpoint = self.endpoints["users"]["get_user"].format(id=user_id)
        response = self._get(endpoint)
        return self._process_response(User, response, "data")

    def account_balance(self) -> UsersAccountBalance:
        endpoint = self.endpoints["users"]["account_balance"]
        response = self._get(endpoint)
        return self._process_response(UsersAccountBalance, response, "data")

    def payment_methods(self) -> List[str]:
        endpoint = self.endpoints["users"]["payment_methods"]
        response = self._get(endpoint)
        return self._process_response(List[str], response, "data")
