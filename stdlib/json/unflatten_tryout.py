#!/usr/bin/env python3
import json
import shutil
import subprocess

from unflatten_json import unflatten


def jq(obj):
    """Print a JSON object."""
    text = json.dumps(obj, indent=4)
    if shutil.which("jq"):
        subprocess.run(["jq", "."], input=text, encoding="utf-8")
    else:
        print(text)


def main():
    """Entry"""
    raw = {
        "metadata.name": "First Environment",
        "metadata.description": "This is a sandbox",
        "metadata.tags[1]": "tag1",
        "metadata.tags[0]": "tag0",
        "useCases[0].templateGroupRef.ref": "u1",
        "useCases[1].templateGroupRef.ref": "u2",
    }

    print("\nInput:")
    jq(raw)
    print()

    print("\nOutput:")
    result = unflatten(raw)
    jq(result)
    print()


if __name__ == "__main__":
    main()
