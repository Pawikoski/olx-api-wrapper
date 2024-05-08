from dataclasses import dataclass


@dataclass
class Offers:
    title: str
    description: str


@dataclass
class OffersResponse:
    data: Offers
