from .olx import Olx
from .models import Language, Currency
from dacite import from_dict
from typing import List


class LanguagesCurrencies(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_languages(self) -> List[Language]:
        endpoint = self.endpoints["languages_currencies"]["get_languages"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return [from_dict(Language, obj) for obj in data]

    def get_currencies(self) -> List[Currency]:
        endpoint = self.endpoints["languages_currencies"]["get_currencies"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return [from_dict(Currency, obj) for obj in data]
