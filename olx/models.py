from dataclasses import dataclass
from typing import Optional


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
