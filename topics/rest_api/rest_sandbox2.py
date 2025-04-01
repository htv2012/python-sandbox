#!/usr/bin/env python3
import rich

from rest_api import Api2


def main():
    print("\n# GET /get")
    api = Api2(prefix="https://httpbin.org")
    resp = api.get("/get")
    print(resp)
    rich.print_json(data=resp.json(), indent=4)


if __name__ == "__main__":
    main()
