import requests


class Olx:
    def __init__(self, access_token: str = None) -> None:
        self.url = "https://www.olx.pl"
        self.endpoints = {
            "auth": "/api/open/oauth/token/",
            "users": {
                "me": "/api/partner/users/me",
                "get_user": "/api/partner/users/{id}",
                "account_balance": "/api/partner/users/me/account-balance",
                "payment_methods": "/api/partner/users/me/payment-methods",
            },
        }
        self.default_scope = "read write v2"
        self.headers = {"Version": "2.0"}

        if access_token:
            self.headers["Authorization"] = "Bearer " + access_token

    def get(self, endpoint, wanted_status=200, **kwargs):
        response = requests.get(url=self.url + endpoint, headers=self.headers, **kwargs)
        if response.status_code != wanted_status:
            print(response)
            print("ERROR")  # TODO:
            return None
        return response
