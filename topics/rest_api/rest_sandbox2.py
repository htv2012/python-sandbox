from jq import jq

from rest_api import Api2


def main():
    print("\n# GET /get")
    api = Api2(prefix="https://httpbin.org")
    resp = api.get("/get")
    print(resp)
    jq(resp.json())


if __name__ == "__main__":
    main()
