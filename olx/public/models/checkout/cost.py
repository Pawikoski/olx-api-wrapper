from dataclasses import dataclass
from numbers import Number
from typing import List, Literal, Optional


@dataclass
class Price:
    amount: Number
    currency: Literal["PLN"]


@dataclass
class DiscountType:
    type: str


@dataclass
class Disclaimer:
    type: str
    days: int
    price: Price


@dataclass
class Cost:
    type: Literal["ITEM_PRICE", "DELIVERY_PRICE_FROM", "SERVICE_FEE"]
    price: Optional[Price]
    url: Optional[str]
    productId: Optional[str]
    finalPrice: Optional[Price]
    originalPrice: Optional[Price]
    discountType: Optional[DiscountType]
    disclaimer: Optional[Disclaimer]
    rewardDiscountSource: Optional[DiscountType]


@dataclass
class CostData:
    costs: List[Cost]


@dataclass
class CostResponse:
    data: CostData
