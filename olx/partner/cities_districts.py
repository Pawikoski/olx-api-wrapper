from .olx import Olx
from .models import Region, City, District, Location
from dacite import from_dict
from typing import List


class CitiesDistricts(Olx):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def list_of_country_regions(self) -> List[Region]:
        endpoint = self.endpoints["cities_and_districts"]["list_of_country_regions"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return [from_dict(Region, obj) for obj in data]

    def get_region(self, region_id: int) -> Region:
        endpoint = self.endpoints["cities_and_districts"]["get_region"].format(
            id=region_id
        )
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(Region, data)

    def get_cities(self, offset: int = None, limit: int = None) -> List[City]:
        endpoint = self.endpoints["cities_and_districts"]["get_cities"]
        params = dict()
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit
        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(City, obj) for obj in data]

    def get_city(self, city_id: int) -> City:
        endpoint = self.endpoints["cities_and_districts"]["get_city"].format(id=city_id)
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(City, data)

    def get_city_districts(self, city_id) -> List[District]:
        endpoint = self.endpoints["cities_and_districts"]["get_city_districts"].format(
            id=city_id
        )
        response = self.get(endpoint)
        data = response.json()["data"]
        return [from_dict(District, obj) for obj in data]

    def get_districts(self) -> List[District]:
        endpoint = self.endpoints["cities_and_districts"]["get_districts"]
        response = self.get(endpoint)
        data = response.json()["data"]
        return [from_dict(District, obj) for obj in data]

    def get_district(self, district_id) -> District:
        endpoint = self.endpoints["cities_and_districts"]["get_district"].format(
            id=district_id
        )
        response = self.get(endpoint)
        data = response.json()["data"]
        return from_dict(District, data)

    def get_locations(self, lat, lon):
        endpoint = self.endpoints["cities_and_districts"]["get_locations"]
        params = {"latitude": lat, "longitude": lon}
        response = self.get(endpoint, params=params)
        data = response.json()["data"]
        return [from_dict(Location, obj) for obj in data]
