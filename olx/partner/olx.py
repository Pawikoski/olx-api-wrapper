import requests


class Olx:
    def __init__(self, access_token: str = None, country_code: str = "pl") -> None:
        assert country_code.lower() in ["pl", "bg", "ro", "pt", "ua", "kz"]
        self.url = f"https://www.olx.{country_code}"
        self.endpoints = {
            "auth": "/api/open/oauth/token/",
            "users": {
                "get_authenticated_user": "/api/partner/users/me",
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
            "threads_messages": {
                "get_threads": "/api/partner/threads",
                "get_thread": "/api/partner/threads/{id}",
                "get_messages": "/api/partner/threads/{id}/messages",
                "post_message": "/api/partner/threads/{id}/messages",
                "get_message": "/api/partner/threads/{thread_id}/messages/{message_id}",
                "take_action_on_thread": "/api/partner/threads/{id}/commands",
            },
            "paid_features": {
                "get_available_paid_features": "/api/partner/paid-features",
                "get_active_paid_features": "/api/partner/adverts/{advert_id}/paid-features",
                "purchase_paid_feature": "/api/partner/adverts/{id}",
            },
            "adverts": {
                "get_user_adverts": "/api/partner/adverts",
                "create_advert": "/api/partner/adverts",
                "get_advert": "/api/partner/adverts/{id}",
                "update_advert": "/api/partner/adverts/{id}",
                "delete_advert": "/api/partner/adverts/{id}",
                "take_action_on_advert": "/api/partner/adverts/{id}/commands",
            },
            "advert_statistics": {
                "get_advert_statistics": "/api/partner/adverts/{id}/statistics",
                "clear_statistics": "/api/partner/adverts/{id}/statistics/{statistic_name}",
            },
            "advert_logo": {
                "get_advert_logos": "/api/partner/adverts/{id}/logos",
                "add_logo": "/api/partner/adverts/{id}/logos",
                "delete_logo": "/api/partner/adverts/{id}/logos/{logo_id}",
            },
            "users_business": {
                "get_user_business_data": "/api/partner/user-business/me",
                "update_user_business_data": "/api/partner/user-business/me",
                "get_user_business_logos": "/api/partner/user-business/me/logos",
                "set_user_business_logos": "/api/partner/user-business/me/logos",
                "remove_user_business_logo": "/api/partner/user-business/me/logos/{logo_id}",
                "get_user_business_banners": "/api/partner/user-business/me/banners",
                "set_user_business_banner": "/api/partner/user-business/me/banners",
                "remove_user_business_banner": "/api/partner/user-business/me/banners/{banner_id}",
            },
            "payments": {
                "get_billing": "/api/partner/user/me/billing",
                "get_prepaid_invoices": "/api/partner/user/me/prepaid-invoices",
                "get_postpaid_invoices": "/api/partner/user/me/postpaid-invoices",
            },
        }
        self.default_scope = "read write v2"
        self.headers = {"Version": "2.0", "Content-Type": "application/json"}

        if access_token:
            self.headers["Authorization"] = "Bearer " + access_token

    def get(self, endpoint, wanted_status=200, **kwargs):
        response = requests.get(url=self.url + endpoint, headers=self.headers, **kwargs)
        if response.status_code != wanted_status:
            print(response.json())
            print("ERROR")  # TODO:
            return None
        return response

    def post(self, endpoint, wanted_status=200, **kwargs):
        response = requests.post(
            url=self.url + endpoint, headers=self.headers, **kwargs
        )
        if response.status_code != wanted_status:
            print(response.json())
            print("ERROR")  # TODO:
            return None
        return response

    def put(self, endpoint, wanted_status=200, **kwargs):
        response = requests.put(url=self.url + endpoint, headers=self.headers, **kwargs)
        if response.status_code != wanted_status:
            print(response.json())
            print("ERROR")  # TODO:
            return None
        return response

    def delete(self, endpoint, wanted_status=200, **kwargs):
        response = requests.delete(
            url=self.url + endpoint, headers=self.headers, **kwargs
        )
        if response.status_code != wanted_status:
            print(response.json())
            print("ERROR")  # TODO:
            return None
        return response
