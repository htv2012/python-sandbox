import json
import logging
import urllib.error
import urllib.parse
import urllib.request

logging.basicConfig(level=logging.DEBUG)
logger = logging


if __name__ == "__main__":
    headers = dict(Accept="application/json")
    param = dict(
        APIKey="H2WUBDYOz6rBYFIN9Dc5KH1qMAtUAwPi",
        oauth_callback="oob",
        access="Full",
        permissions="Read",
        username="haivu",
    )
    query = urllib.parse.urlencode(param)

    url = "http://api.smugmug.com/services/oauth/1.0a/getRequestToken?{}".format(query)

    req = urllib.request.Request(url=url, headers=headers)

    logger.debug("URL: %s", url)
    try:
        response = urllib.request.urlopen(req)
        obj = json.load(response)
        print(json.dumps(obj, indent=2))
    except urllib.error.HTTPError:
        raise
