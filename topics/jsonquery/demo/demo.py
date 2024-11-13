#!/usr/bin/env python3
"""
A Python skeleton script
"""
import json
import pathlib
import pprint

import sys

this_script = pathlib.Path(__file__)
sys.path.append(str(this_script.parent.parent))

import jsonquery


def main():
    """ Entry """
    component_filename = this_script.with_name("component.json")
    with open(component_filename) as stream:
        json_object = json.load(stream)

    result = jsonquery.query(
        json_object,
        key_path=("component", "*", "properties", "property", "*"),
        predicate=lambda d: d["name"].startswith("fw-version"),
        selector=lambda d: (d["name"], d["state"]["value"]),
    )

    pprint.pprint(list(result))
if __name__ == '__main__':
    main()

