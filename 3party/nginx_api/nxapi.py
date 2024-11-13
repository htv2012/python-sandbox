#!/usr/bin/env python3
"""
NGINX Controller API Wrapper
"""
import requests


class NginxApi:
    def __init__(self, host):
        self.host = host
        self.session = requests.Session()

    def login(self, username, password):
        url = self.make_url("/platform/login")
        payload = {
            "credentials": {"username": username, "password": password, "type": "BASIC"}
        }
        response = self.session.get(url, json=payload)
        print(response)

    def make_url(self, path):
        path = path.lstrip("/")
        url = f"https://{self.host}/api/v1/{path}"
        return url


