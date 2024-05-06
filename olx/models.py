from dataclasses import dataclass
from typing import Any, List, Optional, Literal
from numbers import Number


@dataclass
class AuthResponse:
    access_token: str
    expires_in: int
    token_type: str
    scope: str
    refresh_token: Optional[str]


@dataclass
class UsersMe:
    id: int
    email: str
    status: str
    name: str
    phone: Optional[str]
    phone_login: Optional[int]
    created_at: str
    last_login_at: str
    avatar: Optional[str]
    is_business: bool


@dataclass
class UsersGetUser:
    id: int
    name: str
    avatar: Optional[str]


@dataclass
class UsersAccountBalance:
    sum: float
    wallet: float
    bonus: float
    refund: float
    currency: Optional[str]


# Cities & Districts
@dataclass
class Region:
    id: int
    name: str


@dataclass
class City:
    id: int
    region_id: int
    name: str
    county: str
    municipality: str
    latitude: float
    longitude: float


@dataclass
class District:
    id: int
    city_id: int
    name: str
    latitude: float
    longitude: float


@dataclass
class Location:
    city: City
    district: Optional[District]


# Languages & Currencies
@dataclass
class Language:
    code: str
    is_default: bool


@dataclass
class Currency:
    code: str
    label: str
    is_default: bool


# Categories & Attributes
@dataclass
class Category:
    id: int
    name: str
    parent_id: int
    photos_limit: int
    is_leaf: bool


@dataclass
class CategoryAttributeValidation:
    type: str
    required: bool
    numeric: bool
    min: Any
    max: Any
    allow_multiple_values: bool


@dataclass
class CategoryAttribute:
    code: str
    label: str
    unit: Optional[str]
    validation: CategoryAttributeValidation
    values: List[Any]


@dataclass
class CategoryPath:
    id: int | str
    name: str


@dataclass
class CategorySuggestion:
    id: int | str
    name: str
    path: List[CategoryPath]


# Threads & Messages
@dataclass
class Thread:
    id: int
    advert_id: int
    interlocutor_id: int
    total_count: int
    unread_count: int
    created_at: str
    is_favourite: bool


@dataclass
class MessageAttachment:
    name: str
    url: str


@dataclass
class Message:
    id: int
    thread_id: int
    created_at: str
    type: str
    text: str
    attachments: Optional[List[MessageAttachment]]
    is_read: bool
    phone: str
    cvs: List[Any]


# Paid features
@dataclass
class PaidFeature:
    code: str
    type: str
    duration: Optional[int]
    name: str


@dataclass
class ActivePaidFeature(PaidFeature):
    valid_to: str


# Adverts
@dataclass
class AdvertContact:
    name: str
    phone: Optional[str]


@dataclass
class AdvertLocation:
    city_id: int
    district_id: Optional[int]
    latitude: Optional[str]
    longitude: Optional[str]


@dataclass
class AdvertPrice:
    value: Number | str
    currency: str
    negotiable: bool
    trade: bool
    budget: bool


@dataclass
class AdvertSalary:
    value_from: Number
    value_to: Number
    currency: str
    negotiable: bool
    type: Literal["monthly", "hourly"]


@dataclass
class AdvertAttribute:
    code: str
    value: Optional[str]
    values: Optional[List[str]]


@dataclass
class AdvertImage:
    url: str


@dataclass
class Advert:
    id: int
    status: Literal[
        "new",
        "active",
        "limited",
        "removed_by_user",
        "outdated",
        "unconfirmed",
        "unpaid",
        "moderated",
        "blocked",
        "disabled",
        "removed_by_moderator",
    ]
    url: str
    created_at: str
    activated_at: str
    valid_to: str
    title: str
    description: str
    category_id: Optional[int]
    advertiser_type: Literal["private", "business"]
    external_id: Optional[str]
    external_url: Optional[str]
    contact: AdvertContact
    location: AdvertLocation
    images: List[AdvertImage]
    price: Optional[AdvertPrice]
    salary: Optional[AdvertSalary]
    attributes: Optional[List[AdvertAttribute]]
    courier: Optional[bool]
