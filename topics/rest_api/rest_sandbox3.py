#!/usr/bin/env python3
import json
import shutil
import subprocess

from rest_api import Endpoint, create_session


def jq(obj):
    """Print a JSON object."""
    text = json.dumps(obj, indent=4)
    if shutil.which("jq"):
        subprocess.run(["jq", "."], input=text, encoding="utf-8")
    else:
        print(text)


api = create_session()
ep = Endpoint("https://httpbin.org")
r = api.get(ep("/get"))
print(r)
jq(r.json())
