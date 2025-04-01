#!/usr/bin/env python3

from jq import jq
from rest_api import Endpoint, create_session


def main():
    print("\n# GET /get")
    api = create_session()
    ep = Endpoint("https://httpbin.org")
    r = api.get(ep("/get"))
    print(r)
    jq(r.json())


if __name__ == "__main__":
    main()
