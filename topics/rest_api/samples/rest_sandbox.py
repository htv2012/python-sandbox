#!/usr/bin/env python3
import rich

from rest_api import Api

api = Api("https://httpbin.org/")

print("\n# GET /get")
resp = api.get("/get")
print(resp)
rich.print_json(data=resp.json(), indent=4)
