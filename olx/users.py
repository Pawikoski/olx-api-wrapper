from .olx import Olx
from .models import UsersMe, UsersGetUser, UsersAccountBalance
from dacite import from_dict
from typing import List


class Users(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def me(self) -> UsersMe:
        endpoint = self.endpoints["users"]["me"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(UsersMe, data)

    def get_user(self, user_id: int) -> UsersGetUser:
        endpoint = self.endpoints["users"]["get_user"].format(id=user_id)
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(UsersGetUser, data)

    def account_balance(self) -> UsersAccountBalance:
        endpoint = self.endpoints["users"]["account_balance"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(UsersAccountBalance, data)

    def payment_methods(self) -> List[str]:
        endpoint = self.endpoints["users"]["payment_methods"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return data
