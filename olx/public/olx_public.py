import requests


class OlxPublic:
    def __init__(self) -> None:
        self.url = "https://www.olx.pl"
        self.headers = {}

    def get(self, endpoint: str, extra_headers: dict = None, *args, **kwargs):
        url = self.url + endpoint
        headers = self.headers
        if extra_headers:
            headers = {
                **headers,
                **extra_headers
            }

        return requests.get(url=url, headers=headers, *args, **kwargs)
