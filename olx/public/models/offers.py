from __future__ import annotations

from dataclasses import dataclass
from numbers import Number
from typing import List, Literal, Optional

from moneyed import Money


@dataclass
class Promotion:
    highlighted: bool
    urgent: bool
    top_ad: bool
    options: List
    b2c_ad_page: bool
    premium_ad_page: bool


@dataclass
class Value:
    label: Optional[str]
    value: Optional[Number]
    type: Optional[str]
    arranged: Optional[bool]
    budget: Optional[bool]
    currency: Optional[str]
    negotiable: Optional[bool]
    converted_value: Optional[Number]
    previous_value: Optional[Number]
    converted_previous_value: Optional[Number]
    converted_currency: Optional[str]
    previous_label: Optional[str]
    key: Optional[str | list]


@dataclass
class Param:
    key: str
    name: str
    type: str
    value: Value


@dataclass
class User:
    id: int
    created: str
    other_ads_enabled: bool
    name: str
    logo: Optional[str]
    logo_ad_page: Optional[str]
    social_network_account_type: Optional[str]
    photo: Optional[str]
    banner_mobile: str
    banner_desktop: str
    company_name: str
    about: str
    b2c_business_page: bool
    is_online: bool
    last_seen: str
    seller_type: None
    uuid: str


@dataclass
class Contact:
    name: str
    phone: bool
    chat: bool
    negotiation: bool
    courier: bool


@dataclass
class Map:
    zoom: int
    lat: float
    lon: float
    radius: int
    show_detailed: bool


@dataclass
class City:
    id: int
    name: str
    normalized_name: str


@dataclass
class District:
    id: int
    name: str


@dataclass
class Region:
    id: int
    name: str
    normalized_name: str


@dataclass
class Location:
    city: City
    district: Optional[District]
    region: Region


@dataclass
class Category:
    id: int
    type: str


@dataclass
class Rock:
    offer_id: Optional[str]
    active: bool
    mode: str


@dataclass
class Delivery:
    rock: Rock


@dataclass
class Safedeal:
    weight: int
    weight_grams: int
    status: str
    safedeal_blocked: bool
    allowed_quantity: List


@dataclass
class Shop:
    subdomain: Optional[str]


@dataclass
class Partner:
    code: str


@dataclass
class Photo:
    id: int
    filename: str
    rotation: int
    width: int
    height: int
    link: str


@dataclass
class Offer:
    id: int
    url: str
    title: str
    last_refresh_time: str
    created_time: str
    valid_to_time: str
    pushup_time: Optional[str]
    description: str
    promotion: Promotion
    params: List[Param]
    key_params: List
    business: bool
    user: User
    status: str
    contact: Contact
    map: Map
    location: Location
    photos: List[Photo]
    partner: Optional[Partner]
    category: Category
    delivery: Delivery
    safedeal: Safedeal
    shop: Shop
    offer_type: Literal["offer"]

    @property
    def price(self) -> Optional[float]:
        for param in self.params:
            if param.key == "price":
                value = param.value.value
                currency = param.value.currency
                return Money(value, currency)
        return None


@dataclass
class Targeting:
    env: str
    lang: str
    account: Optional[str]
    dfp_user_id: Optional[str]
    user_status: Optional[str]
    cat_l0_id: Optional[str]
    cat_l1_id: Optional[str]
    cat_l0: Optional[str]
    cat_l0_path: Optional[str]
    cat_l1: Optional[str]
    cat_l1_path: Optional[str]
    cat_l2: Optional[str]
    cat_l0_name: Optional[str]
    cat_l1_name: Optional[str]
    cat_id: Optional[str]
    private_business: str
    offer_seek: str
    view: str
    search_engine_input: str
    page: str
    segment: List
    app_version: str


@dataclass
class Config:
    targeting: Targeting


@dataclass
class Adverts:
    places: None
    config: Config


@dataclass
class Source:
    organic: List[int]


@dataclass
class Metadata:
    total_elements: int
    visible_total_count: int
    promoted: List
    search_id: str
    adverts: Optional[Adverts]
    source: Source


@dataclass
class Self:
    href: str


@dataclass
class Next:
    href: str


@dataclass
class First:
    href: str


@dataclass
class Links:
    self: Self
    next: Optional[Next]
    first: Optional[First]


@dataclass
class FetchOffersResponse:
    data: List[Offer]
    metadata: Metadata
    links: Links


@dataclass
class SingleOfferResponse:
    data: Offer
    links: Links


@dataclass
class SuggestedMetadata:
    campaign_source: Optional[dict]
    sources: dict


@dataclass
class SuggestedResponse:
    data: List[Offer]
    metadata: SuggestedMetadata
