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
            "cities_and_districts": {
                "list_of_country_regions": "/api/partner/regions",
                "get_region": "/api/partner/regions/{id}",
                "get_cities": "/api/partner/cities",
                "get_city": "/api/partner/cities/{id}",
                "get_city_districts": "/api/partner/cities/{id}/districts",
                "get_districts": "/api/partner/districts",
                "get_district": "/api/partner/districts/{id}",
                "get_locations": "/api/partner/locations",
            },
            "languages_currencies": {
                "get_languages": "/api/partner/languages",
                "get_currencies": "/api/partner/currencies",
            },
            "categories_attributes": {
                "get_categories": "/api/partner/categories",
                "get_category": "/api/partner/categories/{id}",
                "get_category_attributes": "/api/partner/categories/{id}/attributes",
                "get_category_suggestions": "/api/partner/categories/suggestion",
            },
        }
        self.default_scope = "read write v2"
        self.headers = {"Version": "2.0"}

        if access_token:
            self.headers["Authorization"] = "Bearer " + access_token

    def get(self, endpoint, wanted_status=200, **kwargs):
        response = requests.get(url=self.url + endpoint, headers=self.headers, **kwargs)
        if response.status_code != wanted_status:
            print(response.json())
            print("ERROR")  # TODO:
            return None
        return response
