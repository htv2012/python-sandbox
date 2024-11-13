#!/usr/bin/env python3
import json
import os
import types

import httpx


def create_adm(host: str):
    def _make(path):
        path = path.strip("/")
        result = f"https://{host}/api/adm/v1/{path}".strip("/")
        return result

    return _make


def create_get(cli, host):
    def _get(path):
        url = f"https://{host}/api/adm/v1/{path.strip('/')}"
        result = cli.get(url)
        return result

    return _get


def make_api():
    # Load symbols
    with open(os.getenv("TESTRUN_SYMBOLS")) as stream:
        symbols = json.load(stream)
        symbols = types.SimpleNamespace(**symbols)

    host = symbols.control_host_ips[0]

    # client
    client = httpx.Client(
        headers={"Content-Type": "application/json"},
        auth=httpx.BasicAuth("admin", "Testenv12#"),
        verify=False,
    )

    def get(path, **kwargs):
        nonlocal client
        path = path.strip("/")
        url = f"https://{host}/api/{path}"
        result = client.get(url, **kwargs)
        return result

    return types.SimpleNamespace(
        get=get,
    )


api = make_api()
r = api.get("adm/v1/templates/usecases")
