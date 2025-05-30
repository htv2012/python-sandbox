#!/usr/bin/env python3
import json
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from rauth import OAuth1Service

OAUTH_ORIGIN = "https://secure.smugmug.com"
REQUEST_TOKEN_URL = OAUTH_ORIGIN + "/services/oauth/1.0a/getRequestToken"
ACCESS_TOKEN_URL = OAUTH_ORIGIN + "/services/oauth/1.0a/getAccessToken"
AUTHORIZE_URL = OAUTH_ORIGIN + "/services/oauth/1.0a/authorize"

API_ORIGIN = "https://api.smugmug.com"

SERVICE = None


def get_service():
    global SERVICE
    if SERVICE is None:
        try:
            with open("config.json", "r") as fh:
                config = json.load(fh)
        except IOError:
            print("====================================================")
            print("Failed to open config.json! Did you create it?")
            print("The expected format is demonstrated in example.json.")
            print("====================================================")
            sys.exit(1)
        try:
            assert isinstance(config["key"], str)
            assert isinstance(config["secret"], str)
        except (TypeError, AssertionError):
            print("====================================================")
            print("Invalid config.json!")
            print("The expected format is demonstrated in example.json.")
            print("====================================================")
            sys.exit(1)
        SERVICE = OAuth1Service(
            name="smugmug-oauth-web-demo",
            consumer_key=config["key"],
            consumer_secret=config["secret"],
            request_token_url=REQUEST_TOKEN_URL,
            access_token_url=ACCESS_TOKEN_URL,
            authorize_url=AUTHORIZE_URL,
            base_url=API_ORIGIN + "/api/v2",
        )
    return SERVICE


def add_auth_params(auth_url, access=None, permissions=None):
    if access is None and permissions is None:
        return auth_url
    parts = urlsplit(auth_url)
    query = parse_qsl(parts.query, True)
    if access is not None:
        query.append(("Access", access))
    if permissions is not None:
        query.append(("Permissions", permissions))
    return urlunsplit(
        (parts.scheme, parts.netloc, parts.path, urlencode(query, True), parts.fragment)
    )
