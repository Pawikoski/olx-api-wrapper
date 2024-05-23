from .olx import Olx
from .models import Language, Currency
from typing import List


class LanguagesCurrencies(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_languages(self) -> List[Language]:
        endpoint = self.endpoints["languages_currencies"]["get_languages"]
        response = self._get(endpoint)
        return self._process_response(Language, response, "data", return_list=True)

    def get_currencies(self) -> List[Currency]:
        endpoint = self.endpoints["languages_currencies"]["get_currencies"]
        response = self._get(endpoint)
        return self._process_response(Currency, response, "data", return_list=True)
