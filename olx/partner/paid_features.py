from .olx import Olx
from .models import PaidFeature, ActivePaidFeature
from typing import List, Literal


class PaidFeatures(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_available_paid_features(self) -> List[PaidFeature]:
        endpoint = self.endpoints["paid_features"]["get_available_paid_features"]
        response = self._get(endpoint)
        return self._process_response(PaidFeature, response, "data", return_list=True)

    def get_active_paid_features(self, advert_id) -> List[ActivePaidFeature]:
        endpoint = self.endpoints["paid_features"]["get_active_paid_features"].format(
            advert_id=advert_id
        )
        response = self._get(endpoint)
        return self._process_response(
            ActivePaidFeature, response, "data", return_list=True
        )

    def purchase_paid_feature(
        self, advert_id: int, payment_method: Literal["account", "postpaid"], code: str
    ):
        endpoint = self.endpoints["paid_features"]["purchase_paid_feature"].format(
            id=advert_id
        )
        payload = {"payment_method": payment_method, "code": code}
        self._post(endpoint, wanted_status=204, json=payload)

        # TODO: return
