from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Filter:
    type: str
    label: str
    unit: Any
    scope: Optional[str]
    values: list
    options: list


@dataclass
class Currency:
    code: str
    symbol: str
    is_default: bool
    prioritized_categories: list


@dataclass
class Distance:
    value: int
    is_default: bool


@dataclass
class FiltersMetadata:
    currencies: List[Currency]
    distances: List[Distance]


@dataclass
class FiltersResponse:
    data: dict
    metadata: FiltersMetadata
