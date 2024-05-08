from .olx_public import OlxPublic
from .models.seo.popular_searches import PopularSearchesResponse
from .models.seo.offers import OffersResponse
from dacite import from_dict


class Seo(OlxPublic):
    def __init__(self) -> None:
        super().__init__()

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
        response = self.get(
            endpoint, params=params, extra_headers={"accept-language": "pl"}
        )
        return from_dict(PopularSearchesResponse, response.json())

    def offer_seo(self, offer_id: int):
        endpoint = f"/api/v1/seo/offers/{offer_id}/"
        response = self.get(endpoint)
        return from_dict(OffersResponse, response.json())
