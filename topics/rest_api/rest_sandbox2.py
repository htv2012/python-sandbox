import json
import shutil
import subprocess

from rest_api import Api2


def jq(obj):
    """Print a JSON object."""
    text = json.dumps(obj, indent=4)
    if shutil.which("jq"):
        subprocess.run(["jq", "."], input=text, encoding="utf-8")
    else:
        print(text)


api = Api2(prefix="https://httpbin.org")

r = api.get("/get")
print(r)
jq(r.json())
