from dataclasses import dataclass
from typing import List


@dataclass
class Seller:
    id: int
    market: str


@dataclass
class ShipmentMethod:
    code: str
    paymentMethods: List[str]


@dataclass
class PaymentMethod:
    code: str


@dataclass
class Listing:
    active: bool
    optIn: bool
    isAvailableForPayAndShip: bool
    seller: Seller
    shipmentMethods: List[ShipmentMethod]
    paymentMethods: List[PaymentMethod]
    activeAndOptIn: bool


@dataclass
class ListingResponse:
    data: Listing
