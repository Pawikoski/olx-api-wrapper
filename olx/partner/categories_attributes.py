from .olx import Olx
from .models import Category, CategoryAttribute, CategorySuggestion
from typing import List


class CategoriesAttributes(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_categories(self, parent_id: int = None) -> List[Category]:
        endpoint = self.endpoints["categories_attributes"]["get_categories"]
        params = dict()
        if parent_id:
            params["parent_id"] = parent_id
        response = self._get(endpoint, params=params)
        return self._process_response(Category, response, "data", return_list=True)

    def get_category(self, category_id: int) -> Category:
        endpoint = self.endpoints["categories_attributes"]["get_category"].format(
            id=category_id
        )
        response = self._get(endpoint)
        return self._process_response(Category, response, "data")

    def get_category_attributes(self, category_id: int) -> List[CategoryAttribute]:
        endpoint = self.endpoints["categories_attributes"][
            "get_category_attributes"
        ].format(id=category_id)
        response = self._get(endpoint)
        return self._process_response(
            CategoryAttribute, response, "data", return_list=True
        )

    def get_category_suggestions(self, ad_title: str) -> List[CategorySuggestion]:
        endpoint = self.endpoints["categories_attributes"]["get_category_suggestions"]
        params = {"q": ad_title}
        response = self._get(endpoint, params=params)
        return self._process_response(
            CategorySuggestion, response, "data", return_list=True
        )
