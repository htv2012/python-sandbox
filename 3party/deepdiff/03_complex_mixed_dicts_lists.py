#!/usr/bin/env python3
import json

import deepdiff

actual = {
    "metadata": {"name": "env1", "description": "env 1"},
    "someRef": [
        {
            "ref": "two",
        },
        {
            "ref": "one",
        },
    ],
}

expected = {
    "metadata": {
        "name": "stagging",
        "description": "experimental sandbox",
        "displayName": "Stagging Area",
    },
    "someRef": [
        {
            "ref": "one",
        },
        {
            "ref": "two",
        },
        {
            "ref": "three",
        },
    ],
}

dd = deepdiff.DeepDiff(expected, actual, ignore_order=True)

print("\n# actual")
print(json.dumps(actual, indent=4))

print("\n# expected")
print(json.dumps(expected, indent=4))

print("\n# diff")
print(dd.pretty())
print("--")
