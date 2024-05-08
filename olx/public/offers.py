from .olx_public import OlxPublic
from .models.offers.fetch_offers import FetchOffersResponse
from .models.offers.metadata import BreadcrumbResponse
from dacite import from_dict
from typing import Literal


class Offers(OlxPublic):
    def __init__(self) -> None:
        super().__init__()

    def fetch_offers(
        self,
        category_id: int = None,
        offset: int = 0,
        limit: int = 40,
        sort_by: Literal["created_at:desc", "created_at:asc"] = "created_at:desc",
        filters: list = [],
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
        response = self.get(endpoint, params=params)
        return from_dict(FetchOffersResponse, response.json())


class OffersMetadata(OlxPublic):
    def __init__(self) -> None:
        super().__init__()

    def breadcrumbs(self, category_id: int = None):
        endpoint = "/api/v1/offers/metadata/breadcrumbs/"
        params = dict()
        if category_id:
            params["category_id"] = category_id
        response = self.get(endpoint, params=params)
        return from_dict(BreadcrumbResponse, response.json())
