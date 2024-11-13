#!/usr/bin/env python3
import deepdiff

actual = {
    "metadata": {
        "name": "env1",
        "description": "env 1"
    }
}

expected = {
    "metadata": {
        "name": "stagging",
        "description": "experimental sandbox",
        "displayName": "Stagging Area",
    }
}

dd = deepdiff.DeepDiff(actual, expected)
print("\n# Raw print:")
print(dd)
print("--")

print("\n# pretty print:")
print(dd.pretty())
print("--")
