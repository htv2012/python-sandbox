import urllib.request, urllib.error, urllib.parse
import json

user = 'haivu'
headers = dict(Accept='application/json')

apikey = 'H2WUBDYOz6rBYFIN9Dc5KH1qMAtUAwPi'
# url = 'http://api.smugmug.com/services/oauth/1.0a/getRequestToken'
url = 'http://www.smugmug.com/api/v2/user/{}'.format(user)
url += '?APIKey={}'.format(apikey)
# url += '&oauth_callback=oob'
req = urllib.request.Request(url=url, headers=headers)

try:
    response = urllib.request.urlopen(req)
    obj = json.load(response)
    print(json.dumps(obj, indent=2))
except urllib.error.HTTPError as e:
    if e.code == 404:
        print('User not found: {}'.format(user))
