#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import json
import urllib


def get_json(url):
    response = urllib.urlopen(url)
    data = json.load(response)
    return data


def my_ip():
    data = get_json("http://ip.jsontest.com/")
    return data["ip"]


if __name__ == "__main__":
    print("My External IP:", my_ip())
