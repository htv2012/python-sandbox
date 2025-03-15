import json
import shutil
import subprocess


def jq(obj):
    """Print a JSON object."""
    text = json.dumps(obj, indent=4)
    if shutil.which("jq"):
        subprocess.run(["jq", "."], input=text, text=True)
    else:
        print(text)
