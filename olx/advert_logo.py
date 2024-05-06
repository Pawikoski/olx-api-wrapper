from .olx import Olx
from .models import AdvertLogoType
from dacite import from_dict
from typing import List


class AdvertLogo(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_advert_logos(self, advert_id: int) -> List[AdvertLogoType]:
        endpoint = self.endpoints["advert_logo"]["get_advert_logos"].format(
            id=advert_id
        )
        response = self.get(endpoint)
        data = response.json()["data"]
        return [from_dict(AdvertLogoType, obj) for obj in data]

    def add_logo(self, advert_id: int, url: str) -> AdvertLogoType:
        endpoint = self.endpoints["advert_logo"]["add_logo"].format(id=advert_id)
        payload = {"url": url}
        response = self.post(endpoint, json=payload)
        data = response.json()
        return from_dict(AdvertLogo, data)

    def delete_logo(self, advert_id: int, logo_id: int):
        endpoint = self.endpoints["advert_logo"]["delete_logo"].format(
            id=advert_id, logo_id=logo_id
        )
        self.delete(endpoint, wanted_status=204)
