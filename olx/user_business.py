from .olx import Olx
from .models import UserBusinessData
from dacite import from_dict
from typing import List


class UsersBusiness(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_user_business_data(self) -> UserBusinessData:
        endpoint = self.endpoints["users_business"]["get_user_business_data"]
        response = self.get(endpoint)
        data = response.json()
        return from_dict(UserBusinessData, data)
