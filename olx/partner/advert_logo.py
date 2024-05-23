from .olx import Olx
from .models import AdvertLogoType
from typing import List


class AdvertLogo(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_advert_logos(self, advert_id: int) -> List[AdvertLogoType]:
        endpoint = self.endpoints["advert_logo"]["get_advert_logos"].format(
            id=advert_id
        )
        response = self._get(endpoint)
        return self._process_response(
            AdvertLogoType, response, "data", return_list=True
        )

    def add_logo(self, advert_id: int, url: str) -> AdvertLogoType:
        endpoint = self.endpoints["advert_logo"]["add_logo"].format(id=advert_id)
        payload = {"url": url}
        response = self._post(endpoint, json=payload)
        return self._process_response(AdvertLogo, response)

    def delete_logo(self, advert_id: int, logo_id: int):
        endpoint = self.endpoints["advert_logo"]["delete_logo"].format(
            id=advert_id, logo_id=logo_id
        )
        self._delete(endpoint, wanted_status=204)

        # TODO: return
