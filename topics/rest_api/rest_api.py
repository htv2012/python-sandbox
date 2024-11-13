"""Provide RESTful Web Services Support."""
import requests
import urllib3
from requests.sessions import PreparedRequest, Request


def create_session():
    urllib3.disable_warnings()

    session = requests.Session()
    session.verify = False
    session.headers.update(
        {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )
    return session


class Endpoint:
    def __init__(self, prefix: str):
        self.prefix = prefix.removesuffix("/")

    def __call__(self, *segments) -> str:
        suffix = "/".join(segment.strip("/") for segment in segments)
        return f"{self.prefix}/{suffix}"


class Api:
    def __init__(self, session: requests.Session, endpoint: Endpoint):
        self.session = session
        self.ep = endpoint

    def get(self, url, **kwargs):
        url = self.ep(url)
        return self.session.get(url, **kwargs)

    def post(self, url: str, data=None, json=None, **kwargs):
        url = self.ep(url)
        return self.session.post(url, data=data, json=json, **kwargs)

    def put(self, url: str, data=None, **kwargs):
        url = self.ep(url)
        return self.session.put(url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        url = self.ep(url)
        return self.session.delete(url, **kwargs)


class Api2(requests.Session):
    def __init__(self, prefix: str):
        urllib3.disable_warnings()

        super().__init__()
        self.verify = False
        self.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        self.prefix = prefix.removesuffix("/")

    def __repr__(self):
        return f"<{self.__class__.__name__} prefix={self.prefix!r}>"

    def prepare_request(self, request: Request) -> PreparedRequest:
        url = request.url.strip("/")
        request.url = f"{self.prefix}/{url}".removesuffix("/")
        return super().prepare_request(request)
