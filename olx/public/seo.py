from dacite import from_dict

from olx.public.models.seo.offers import OffersResponse
from olx.public.models.seo.popular_searches import PopularSearchesResponse


class Seo:
    def __init__(self, api_call) -> None:
        super().__init__()
        self.public_api_call = api_call

    def popular_searches(
        self,
        category_id: int = None,
        region_id: int = None,
        city_id: int = None,
        offset: int = 0,
        count: int = 10,
    ):
        endpoint = "/api/v1/seo/popular-searches/"
        params = {
            "category_id": category_id,
            "offset": offset,
            "count": count,
        }
        if region_id:
            params["region_id"] = region_id
        if city_id:
            params["city_id"] = city_id
        response = self.public_api_call(
            endpoint, params=params, extra_headers={"accept-language": "pl"}
        )
        return from_dict(PopularSearchesResponse, response.json())

    def offer_seo(self, offer_id: int):
        endpoint = f"/api/v1/seo/offers/{offer_id}/"
        response = self.public_api_call(endpoint)
        return from_dict(OffersResponse, response.json())
