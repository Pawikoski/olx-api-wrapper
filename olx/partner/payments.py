from .olx import Olx
from .models import Billing, PrepaidInvoice, PostpaidInvoice
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
        response = self._get(endpoint, params=params)
        return self._process_response(Billing, response, "data", return_list=True)

    def get_prepaid_invoices(
        self, page: int = None, limit: int = None
    ) -> List[PrepaidInvoice]:
        endpoint = self.endpoints["payments"]["get_prepaid_invoices"]
        params = dict()
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        response = self._get(endpoint, params=params)
        return self._process_response(
            PrepaidInvoice, response, "data", return_list=True
        )

    def get_postpaid_invoices(
        self, page: int = None, limit: int = None
    ) -> List[PostpaidInvoice]:
        endpoint = self.endpoints["payments"]["get_postpaid_invoices"]
        params = dict()
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit
        response = self._get(endpoint, params=params)
        return self._process_response(
            PostpaidInvoice, response, "data", return_list=True
        )
