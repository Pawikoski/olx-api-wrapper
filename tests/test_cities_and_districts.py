import unittest
from unittest.mock import Mock, patch
from olx import CitiesDistricts
from olx.models import City, Region, District, Location
from dacite import from_dict


class TestCitiesAndDistricts(unittest.TestCase):
    def setUp(self):
        self.cities_and_districts = CitiesDistricts()
        self.mock_get = patch.object(self.cities_and_districts, "get").start()

    def tearDown(self):
        self.mock_get.stop()

    def _mock_response(self, data):
        mock_response = Mock()
        mock_response.json.return_value = {"data": data}
        return mock_response

    def test_list_of_country_regions(self):
        mock_data = [{"id": 1, "name": "Wielkopolskie"}]
        self.mock_get.return_value = self._mock_response(mock_data)
        country_regions = self.cities_and_districts.list_of_country_regions()

        self.assertIsInstance(country_regions[0], Region)
        self.assertListEqual(
            country_regions, [from_dict(Region, obj) for obj in mock_data]
        )

    def test_get_region(self):
        mock_data = {"id": 1, "name": "Wielkopolskie"}
        self.mock_get.return_value = self._mock_response(mock_data)

        region = self.cities_and_districts.get_region(region_id=1)

        self.assertIsInstance(region, Region)
        self.assertEqual(region.id, 1)
        self.assertEqual(region.name, "Wielkopolskie")

    def test_get_cities(self):
        mock_data = [
            {
                "id": 627,
                "region_id": 123,
                "name": "Aleksandrów Kujawski",
                "county": "aleksandrowski",
                "municipality": "Aleksandrów Kujawski",
                "latitude": 52.86653,
                "longitude": 18.69801,
            }
        ]
        self.mock_get.return_value = self._mock_response(mock_data)

        cities = self.cities_and_districts.get_cities()
        self.assertIsInstance(cities, list)
        self.assertGreater(len(cities), 0)
        single_city = cities[0]
        self.assertIsInstance(single_city, City)
        self.assertEqual(single_city.id, 627)
        self.assertEqual(single_city.region_id, 123)
        self.assertEqual(single_city.name, "Aleksandrów Kujawski")
        self.assertEqual(single_city.county, "aleksandrowski")
        self.assertEqual(single_city.municipality, "Aleksandrów Kujawski")
        self.assertEqual(single_city.latitude, 52.86653)
        self.assertEqual(single_city.longitude, 18.69801)

    def test_get_city(self):
        mock_data = {
            "id": 627,
            "region_id": 123,
            "name": "Aleksandrów Kujawski",
            "county": "aleksandrowski",
            "municipality": "Aleksandrów Kujawski",
            "latitude": 52.86653,
            "longitude": 18.69801,
        }

        self.mock_get.return_value = self._mock_response(mock_data)

        city = self.cities_and_districts.get_city(city_id=627)
        self.assertIsInstance(city, City)
        self.assertEqual(city.id, 627)
        self.assertEqual(city.region_id, 123)
        self.assertEqual(city.name, "Aleksandrów Kujawski")
        self.assertEqual(city.county, "aleksandrowski")
        self.assertEqual(city.municipality, "Aleksandrów Kujawski")
        self.assertEqual(city.latitude, 52.86653)
        self.assertEqual(city.longitude, 18.69801)

    def test_get_city_districts(self):
        mock_data = [
            {
                "id": 97,
                "city_id": 5659,
                "name": "Aniołki",
                "latitude": 54.36306,
                "longitude": 18.63193,
            }
        ]

        self.mock_get.return_value = self._mock_response(mock_data)

        city_districts = self.cities_and_districts.get_city_districts(city_id=5659)
        self.assertIsInstance(city_districts, list)
        self.assertGreater(len(city_districts), 0)
        single_city_district = city_districts[0]
        self.assertIsInstance(single_city_district, District)
        self.assertEqual(single_city_district.id, 97)
        self.assertEqual(single_city_district.city_id, 5659)
        self.assertEqual(single_city_district.name, "Aniołki")
        self.assertEqual(single_city_district.latitude, 54.36306)
        self.assertEqual(single_city_district.longitude, 18.63193)

    def test_get_districts(self):
        mock_data = [
            {
                "id": 97,
                "city_id": 5659,
                "name": "Aniołki",
                "latitude": 54.36306,
                "longitude": 18.63193,
            }
        ]

        self.mock_get.return_value = self._mock_response(mock_data)

        districts = self.cities_and_districts.get_districts()
        self.assertIsInstance(districts, list)
        self.assertGreater(len(districts), 0)
        single_district = districts[0]
        self.assertIsInstance(single_district, District)
        self.assertEqual(single_district.id, 97)
        self.assertEqual(single_district.city_id, 5659)
        self.assertEqual(single_district.name, "Aniołki")
        self.assertEqual(single_district.latitude, 54.36306)
        self.assertEqual(single_district.longitude, 18.63193)

    def test_get_district(self):
        mock_data = {
            "id": 97,
            "city_id": 5659,
            "name": "Aniołki",
            "latitude": 54.36306,
            "longitude": 18.63193,
        }

        self.mock_get.return_value = self._mock_response(mock_data)

        district = self.cities_and_districts.get_district(district_id=97)
        self.assertIsInstance(district, District)
        self.assertEqual(district.id, 97)
        self.assertEqual(district.city_id, 5659)
        self.assertEqual(district.name, "Aniołki")
        self.assertEqual(district.latitude, 54.36306)
        self.assertEqual(district.longitude, 18.63193)

    def test_get_locations(self):
        mock_data = [
            {
                "city": {
                    "id": 627,
                    "region_id": 123,
                    "name": "Aleksandrów Kujawski",
                    "county": "aleksandrowski",
                    "municipality": "Aleksandrów Kujawski",
                    "latitude": 52.86653,
                    "longitude": 18.69801,
                },
                "district": {
                    "id": 97,
                    "city_id": 5659,
                    "name": "Aniołki",
                    "latitude": 54.36306,
                    "longitude": 18.63193,
                },
            }
        ]

        self.mock_get.return_value = self._mock_response(mock_data)

        locations = self.cities_and_districts.get_locations(lat=52.86653, lon=18.69801)
        self.assertIsInstance(locations, list)
        self.assertGreater(len(locations), 0)
        location = locations[0]
        self.assertIsInstance(location, Location)
        self.assertIsInstance(location.city, City)
        self.assertEqual(location.city.id, 627)
        self.assertEqual(location.city.region_id, 123)
        self.assertEqual(location.city.name, "Aleksandrów Kujawski")
        self.assertEqual(location.city.county, "aleksandrowski")
        self.assertEqual(location.city.municipality, "Aleksandrów Kujawski")
        self.assertEqual(location.city.latitude, 52.86653)
        self.assertEqual(location.city.longitude, 18.69801)

        self.assertIsInstance(location.district, District)
        self.assertEqual(location.district.id, 97)
        self.assertEqual(location.district.city_id, 5659)
        self.assertEqual(location.district.name, "Aniołki")
        self.assertEqual(location.district.latitude, 54.36306)
        self.assertEqual(location.district.longitude, 18.63193)


if __name__ == "__main__":
    unittest.main()
