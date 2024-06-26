from .olx import Olx
from .models import AdvertStatistic
from typing import Literal


class AdvertsStatistics(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_advert_statistics(self, advert_id: int) -> AdvertStatistic:
        endpoint = self.endpoints["advert_statistics"]["get_advert_statistics"].format(
            id=advert_id
        )
        response = self._get(endpoint)
        return self._process_response(AdvertStatistic, response, "data")

    def clear_statistics(
        self, advert_id: int, statistic_name: Literal["phone-views", "advert-views"]
    ) -> None:
        endpoint = self.endpoints["advert_statistics"]["clear_statistics"].format(
            id=advert_id, statistic_name=statistic_name
        )
        self._delete(endpoint, wanted_status=204)
        # TODO: return
