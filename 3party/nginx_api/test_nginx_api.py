#!/usr/bin/env python3
from urllib import response
import nxapi


def test_make_url():
    api = nxapi.NginxApi("1.2.3.4")
    assert api.make_url("/platform/login") == "https://1.2.3.4/api/v1/platform/login"
    assert api.make_url("platform/login") == "https://1.2.3.4/api/v1/platform/login"


def test_login():
    api = nxapi.NginxApi("52.38.180.93")
    response = api.login("admin@nginx.test", "Testenv12#")
    assert response is not None