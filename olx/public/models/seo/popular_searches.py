from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Search:
    label: str
    href: str


@dataclass
class Data:
    searches: List[Search]


@dataclass
class PopularSearchesResponse:
    data: Data
