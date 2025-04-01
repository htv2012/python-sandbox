#!/usr/bin/env python


from smugpy import SmugMug

API_KEY = "H2WUBDYOz6rBYFIN9Dc5KH1qMAtUAwPi"
OAUTH_SECRET = "d978c7819db9a3b99ef44362c5ad6a3e"
APP_NAME = "TestApp"


# Request a "request token" from the smugmug servers for the given permissions.
#
# Return a pair (url, requestToken) that can be used to authorize this app to
# access the account of whomever logs in at the URL.
def smugmugOauthRequestToken(access="Public", perm="Read"):
    smugmug = SmugMug(api_key=API_KEY, oauth_secret=OAUTH_SECRET, app_name=APP_NAME)

    # Get a token that is short-lived (probably about 5 minutes) and can be used
    # only to setup authorization at SmugMug
    response = smugmug.auth_getRequestToken()

    # Get the URL that the user must visit to authorize this app (implicilty includes the request token in the URL)
    url = smugmug.authorize(access=access, perm=perm)

    return url, response["Auth"]  # (should contain a 'Token')


print((smugmugOauthRequestToken()))
