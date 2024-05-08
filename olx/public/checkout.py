from .olx_public import OlxPublic
from .models.checkout.listing import ListingResponse
from .models.checkout.cost import CostResponse
from dacite import from_dict


class Checkout(OlxPublic):
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://pl.ps.prd.eu.olx.org"

    def listing(self, offer_id: int) -> ListingResponse:
        endpoint = f"/checkout/v1/listing/{offer_id}"
        response = self.get(endpoint)
        return from_dict(ListingResponse, response.json())

    def cost(self, offer_id: int) -> CostResponse:
        endpoint = f"/checkout/v1/listing/{offer_id}/cost"
        response = self.get(endpoint)
        return from_dict(CostResponse, response.json())
