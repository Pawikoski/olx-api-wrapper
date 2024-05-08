from .olx import Olx
from .models import Billing, PrepaidInvoice, PostpaidInvoice
from dacite import from_dict
from typing import List


class Payments(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_billing(self, page: int = None, limit: int = None) -> List[Billing]:
        endpoint = self.endpoints["payments"]["get_billing"]
        params = dict()
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(Billing, obj) for obj in data]

    def get_prepaid_invoices(
        self, page: int = None, limit: int = None
    ) -> List[PrepaidInvoice]:
        endpoint = self.endpoints["payments"]["get_prepaid_invoices"]
        params = dict()
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(PrepaidInvoice, obj) for obj in data]

    def get_postpaid_invoices(
        self, page: int = None, limit: int = None
    ) -> List[PostpaidInvoice]:
        endpoint = self.endpoints["payments"]["get_postpaid_invoices"]
        params = dict()
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(PostpaidInvoice, obj) for obj in data]
