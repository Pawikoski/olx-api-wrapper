class Olx:
    def __init__(self) -> None:
        self.url = "https://www.olx.pl"
        self.endpoints = {
            "auth": "/api/open/oauth/token/",
        }
        self.default_scope = "read write v2"
