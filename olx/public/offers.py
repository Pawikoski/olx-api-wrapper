from .olx_public import OlxPublic
from .models.offers.offers import FetchOffersResponse, SuggestedResponse
from .models.offers.metadata import BreadcrumbResponse
from dacite import from_dict
from typing import Literal


class Offers(OlxPublic):
    def __init__(self) -> None:
        super().__init__()

    def offers(
        self,
        category_id: int = None,
        offset: int = 0,
        limit: int = 40,
        sort_by: Literal["created_at:desc", "created_at:asc"] = "created_at:desc",
        filters: list = [],
        user_id: int = None,
    ):
        endpoint = "/api/v1/offers/"
        params = {
            "offset": offset,
            "limit": limit,
            "sort_by": sort_by,
        }
        for filter_name in filters:
            params[f"filter_enum_{filter_name}[0]"] = filters[filter_name]
        if category_id:
            params["category_id"] = category_id
        if user_id:
            params["user_id"] = user_id
        response = self.get(endpoint, params=params)
        return from_dict(FetchOffersResponse, response.json())

    def suggested(self, offer_id: int):
        endpoint = f"/api/v1/offers/{offer_id}/suggested/"
        response = self.get(endpoint)
        return from_dict(SuggestedResponse, response.json())


class OffersMetadata(OlxPublic):
    def __init__(self) -> None:
        super().__init__()

    def breadcrumbs(self, category_id: int = None, offer_id: int = None):
        assert category_id or offer_id, "Provide category_id or offer_id argument"
        assert not (
            category_id and offer_id
        ), "Provide only one argument: category_id or offer_id"

        params = dict()
        if category_id:
            endpoint = "/api/v1/offers/metadata/breadcrumbs/"
            if category_id:
                params["category_id"] = category_id
        else:
            endpoint = f"/api/v1/offers/{offer_id}/breadcrumbs/"
        response = self.get(endpoint, params=params)
        return from_dict(BreadcrumbResponse, response.json())
