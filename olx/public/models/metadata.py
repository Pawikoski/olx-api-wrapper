from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Breadcrumb:
    label: str
    href: str
    categoryId: Optional[int]


@dataclass
class BreadcrumbData:
    breadcrumbs: List[Breadcrumb]


@dataclass
class BreadcrumbResponse:
    data: BreadcrumbData
