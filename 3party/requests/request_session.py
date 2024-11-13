#!/usr/bin/env python3
import requests


class Api:
    def __init__(self, root):
        self.root = root.rstrip("/")
        self.session = requests.Session()
        self.response = None

    def get(self, path, **kwargs):
        path = path.lstrip("/")
        url = f"{self.root}/{path}"
        self.response = self.session.get(url, **kwargs)
        return self.response

api = Api("https://httpbin.org/")
r = api.get("/get")
