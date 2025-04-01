#!/usr/bin/env python3

import rich

from rest_api import Endpoint, create_session


def main():
    print("\n# GET /get")
    api = create_session()
    ep = Endpoint("https://httpbin.org")
    r = api.get(ep("/get"))
    print(r)
    rich.print_json(data=r.json(), indent=4)


if __name__ == "__main__":
    main()
