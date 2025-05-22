import requests
from dacite import from_dict

from olx.public.models.checkout.cost import CostResponse
from olx.public.models.checkout.listing import ListingResponse


class Checkout:
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://pl.ps.prd.eu.olx.org"

    def get(self, endpoint: str, extra_headers: dict = None, *args, **kwargs):
        url = self.url + endpoint
        headers = self.headers
        if extra_headers:
            headers = {**headers, **extra_headers}

        return requests.get(url=url, headers=headers, *args, **kwargs)

    def listing(self, offer_id: int) -> ListingResponse:
        endpoint = f"/checkout/v1/listing/{offer_id}"
        response = self.get(endpoint)
        return from_dict(ListingResponse, response.json())

    def cost(self, offer_id: int) -> CostResponse:
        endpoint = f"/checkout/v1/listing/{offer_id}/cost"
        response = self.get(endpoint)
        return from_dict(CostResponse, response.json())
