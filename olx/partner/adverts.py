from .olx import Olx
from .models import Advert
from typing import List, Literal


class Adverts(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_user_adverts(
        self,
        offset: int = None,
        limit: int = None,
        external_id: str = None,
        category_ids: str = None,
    ) -> List[Advert]:
        endpoint = self.endpoints["adverts"]["get_user_adverts"]
        params = dict()
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit
        if external_id:
            params["external_id"] = external_id
        if category_ids:
            params["category_ids"] = category_ids
        response = self._get(endpoint, params=params)
        return self._process_response(Advert, response, "data", return_list=True)

    def build_payload_for_create_or_update(
        self,
        title: str,
        description: str,
        category_id: str,
        advertiser_type: Literal["private", "business"],
        contact: dict,  # models.AdvertContact
        location: dict,  # models.AdvertLocation
        attributes: List[dict],  # models.AdvertAttribute
        price: dict,  # models.AdvertPrice
        images: List[dict] = None,  # models.AdvertImage
        salary: dict = None,  # models.AdvertSalary
        external_url: str = None,
        external_id: str = None,
        courier: bool = None,
    ):
        payload = {
            "title": title,
            "description": description,
            "category_id": category_id,
            "advertiser_type": advertiser_type,
            "contact": contact,
            "price": price,
            "location": location,
            "attributes": attributes,
        }
        if images:
            payload["images"] = images
        if salary:
            payload["salary"] = salary
        if external_url:
            payload["external_url"] = external_url
        if external_id:
            payload["external_id"] = external_id
        if courier:
            payload["courier"] = courier

        return payload

    def create_advert(self, *args, **kwargs) -> Advert:
        endpoint = self.endpoints["adverts"]["create_advert"]
        payload = self.build_payload_for_create_or_update(*args, **kwargs)
        response = self._post(endpoint, json=payload)
        return self._process_response(Advert, response)

    def get_advert(self, advert_id) -> Advert:
        endpoint = self.endpoints["adverts"]["get_advert"].format(id=advert_id)
        response = self._get(endpoint)
        return self._process_response(Advert, response)

    def update_advert(self, advert_id, *args, **kwargs) -> Advert:
        endpoint = self.endpoints["adverts"]["update_advert"].format(id=advert_id)
        payload = self.build_payload_for_create_or_update(*args, **kwargs)
        response = self._put(endpoint, json=payload)
        return self._process_response(Advert, response, "data")

    def delete_advert(self, advert_id: int) -> None:
        endpoint = self.endpoints["adverts"]["delete_advert"].format(id=advert_id)
        self._delete(endpoint, wanted_status=204)
        # TODO: return

    def take_action_on_advert(
        self,
        advert_id: int,
        command: Literal["activate", "deactivate", "finish", "refresh"],
        is_success: bool = None,
    ):
        endpoint = self.endpoints["adverts"]["take_action_on_advert"].format(
            id=advert_id
        )
        payload = {"command": command}
        if command == "deactivate":
            assert is_success is not None
            payload["is_success"] = is_success
        self._post(endpoint, json=payload, wanted_status=204)

        # TODO: return

    def activate_advert(self, advert_id: int):
        return self.take_action_on_advert(advert_id, "activate")

    def deactivate_advert(self, advert_id: int, is_success: bool):
        return self.take_action_on_advert(advert_id, "deactivate", is_success)

    def finish_advert(self, advert_id: int):
        return self.take_action_on_advert(advert_id, "finish")

    def refresh_advert(self, advert_id: int):
        return self.take_action_on_advert(advert_id, "refresh")
