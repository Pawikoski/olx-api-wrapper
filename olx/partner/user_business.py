from .olx import Olx
from .models import UserBusinessData


class UsersBusiness(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_user_business_data(self) -> UserBusinessData:
        endpoint = self.endpoints["users_business"]["get_user_business_data"]
        response = self._get(endpoint)
        return self._process_response(UserBusinessData, response)
