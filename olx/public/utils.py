from urllib import parse

import requests


def reverse_url_to_params(url: str):
    try:
        splitted = parse.urlsplit(url)
        new_path = splitted.path.replace("/", ",")

        api_url = f"https://www.olx.pl/api/v1/friendly-links/query-params/{new_path}/"

        params = dict(parse.parse_qsl(parse.urlsplit(url).query))

        response = requests.get(api_url, params=params)
        result = response.json()

        if result.get("data"):
            return result["data"]

        return None
    except Exception as e:
        print("Error occured while reversing url to parameters:", e)
        return None


if __name__ == "__main__":
    url = "https://www.olx.pl/elektronika/gry-konsole/konsole/playstation/q-playstation-4/?search%5Border%5D=filter_float_price:asc&search%5Bfilter_float_price:from%5D=250&search%5Bfilter_float_price:to%5D=450&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_version%5D%5B0%5D=playstation4"
    params = reverse_url_to_params(url)
    print(params)
