from jq import jq

from rest_api import Api, Endpoint, create_session

session = create_session()
endpoint = Endpoint("https://httpbin.org/")
api = Api(session=session, endpoint=endpoint)

print(f"\n# GET {endpoint('/get')}")
resp = api.get("/get")
print(resp)
jq(resp.json())
