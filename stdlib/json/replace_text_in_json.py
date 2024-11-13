#!/usr/bin/env python3
"""Replace text in a JSON object."""

import json


def replace_text_in_json(old2new: dict, json_object):
    json_as_text = json.dumps(json_object)
    for old_text, new_text in old2new.items():
        json_as_text = json_as_text.replace(f'"{old_text}"', f'"{new_text}"')
    new_json_object = json.loads(json_as_text)
    return new_json_object


OLD2NEW = {
    "cert1": "/ref/to/cert1",
    "cert2": "/ref/to/cert2",
}


def test_happy_path():
    obj = {
        "name": "mycert1",
        "ref1": "cert1",
        "ref2": "cert2",
        "ref3": "cert3",
    }
    new_obj = replace_text_in_json(OLD2NEW, obj)
    assert new_obj == {
        "name": "mycert1",  # Not replaced because not a whole string
        "ref1": "/ref/to/cert1",
        "ref2": "/ref/to/cert2",
        "ref3": "cert3",  # Not replaced because there is no replacement
    }
