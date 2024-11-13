from rest_api import Api, Endpoint, create_session

session = create_session()
endpoint = Endpoint("https://httpbin.org/")
api = Api(session=session, endpoint=endpoint)

r = api.get("/get")
print(r)
