#!/usr/bin/env python3
from urllib.parse import urlencode


class Url:
    def __init__(self, url):
        self._url = url

    def __str__(self):
        return self._url

    def __floordiv__(self, path):
        path = path.lstrip("/")
        new_url = f"{self._url}/{path}"
        return Url(new_url)

    def __truediv__(self, path: str):
        return str(self // path)

    def __call__(self, *args, **kwargs):
        path = "/".join(arg.strip("/") for arg in args) + urlencode(kwargs, doseq=True)
        return (self / path).removesuffix("/")
