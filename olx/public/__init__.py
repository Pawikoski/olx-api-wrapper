from typing import List, Literal

import requests
from dacite import from_dict

from olx.public.checkout import Checkout
from olx.public.models.filters import Filter, FiltersResponse
from olx.public.models.metadata import BreadcrumbResponse
from olx.public.models.offers import (
    FetchOffersResponse,
    Offer,
    SingleOfferResponse,
    SuggestedResponse,
)
from olx.public.seo import Seo
from olx.public.utils import reverse_url_to_params
from fake_useragent import UserAgent


class OlxPublic:
    def __init__(self, full_response=False, use_fake_ua=False):
        self.url = "https://www.olx.pl"
        self.headers = {}
        self.full_response = full_response
        self._checkout = Checkout()
        self._seo = Seo(self.public_api_call)
        self.use_fake_ua = use_fake_ua
        self.ua = UserAgent() if use_fake_ua else None

    def public_api_call(
        self, endpoint: str, extra_headers: dict = None, *args, **kwargs
    ):
        url = self.url + endpoint
        headers = self.headers
        if extra_headers:
            headers = {**headers, **extra_headers}

        if self.use_fake_ua and self.ua:
            headers["User-Agent"] = self.ua.random

        return requests.get(url=url, headers=headers, *args, **kwargs)

    def get_offers(
        self,
        url: str = None,
        category_id: int = None,
        offset: int = 0,
        limit: int = 40,
        sort_by: Literal["created_at:desc", "created_at:asc"] = "created_at:desc",
        extra_params: dict = None,
        user_id: int = None,
    ) -> FetchOffersResponse | List[Offer]:
        endpoint = "/api/v1/offers/"
        if url:
            params = reverse_url_to_params(url)
        else:
            params = {
                "offset": offset,
                "limit": limit,
                "sort_by": sort_by,
            }
        if extra_params:
            params = {**params, **extra_params}
        if category_id:
            params["category_id"] = category_id
        if user_id:
            params["user_id"] = user_id
        response = self.public_api_call(endpoint, params=params)
        result = from_dict(FetchOffersResponse, response.json())
        if self.full_response:
            return result
        else:
            return result.data

    def get_offer(self, offer_id: int):
        """Get offer by id

        Args:
            offer_id (int): ID of the offer

        Returns:
            full_response - (SingleOfferResponse): Full response object (models.offers.offers.SingleOfferResponse)
            else (models.offers.offers.Offer): Offer object (models.offers.offers.Offer)
        """
        endpoint = f"/api/v1/offers/{offer_id}/"
        response = self.public_api_call(endpoint)
        return from_dict(SingleOfferResponse, response.json())

    def get_suggested_offers(self, offer_id: int):
        endpoint = f"/api/v1/offers/{offer_id}/suggested/"
        response = self.public_api_call(endpoint)
        return from_dict(SuggestedResponse, response.json())

    def get_offer_filters(self):
        """
        Lists filters for all categories
            Returns:
                data (FiltersResponse)
                data.data is a dict where every data.data[key] is a list of filter objects (List[models.offers.filters.Filter])
        """
        endpoint = "/api/v1/offers/metadata/filters"
        response = self.public_api_call(endpoint)
        data = response.json()
        new_data = dict()
        for filter_name in data["data"]:
            # print(data["data"][filter_name])
            new_data[filter_name] = [
                from_dict(Filter, obj) for obj in data["data"][filter_name]
            ]
        data["data"] = new_data
        return from_dict(FiltersResponse, data)

    def get_breadcrumbs(self, category_id: int = None, offer_id: int = None):
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
        response = self.public_api_call(endpoint, params=params)
        return from_dict(BreadcrumbResponse, response.json())

    # Property accessors for specialized functionality
    @property
    def checkout(self):
        return self._checkout

    @property
    def seo(self):
        return self._seo


# Export OlxPublic as the main entry point
__all__ = ["OlxPublic", "Checkout", "Seo"]
