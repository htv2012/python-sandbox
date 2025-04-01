#!/usr/bin/env python3
"""
This module provides functions that query a JSON object.
"""

import fnmatch
from collections.abc import Mapping, Sequence


def _get_key_value_function(json_object):
    """
    Returns a function that would return a key/value pair for a given object

    :param json_object: A nested list, dict objects
    :return: A function object
    """
    if isinstance(json_object, Sequence) and not isinstance(json_object, str):
        key_value_function = enumerate
    elif isinstance(json_object, Mapping):
        key_value_function = dict.items
    else:
        raise ValueError(
            "Cannot get key/value function for object of type "
            "{type(json_object).__name__}",
            json_object=json_object,
        )

    return key_value_function


def _iter_path(json_object, key_path):
    """
    Given a JSON object and a key path (a tuple of keys that would lead
    to an object within the JSON object), returns all the applicable
    objects that indicated by the key path. For example, given:

        json_object = {
            "person": {
                "business_phone": "555-1252",
                "mobile_phone": "555-1111"
            }
        }

        key_path = ("person", "*_phone")

    then this function will generate a list of

        ["555-1252", "555-1111"]

    Note that the key_path can be a tuple or list of string, whereas each
    key in the path can be a wildcard--the same wildcard that matches
    Linux filenames. The wildcards also work on list indices, not just
    dictionary keys.

    :param json_object: A nested list, dict objects
    :param key_path: A list or tuple of strings indicate the path
    :return: A generator object that produces a list of objects
    """
    if isinstance(key_path, str):
        key_path = [key_path]
    else:
        key_path = list(key_path)

    while key_path:
        key = key_path.pop(0)
        try:
            json_object = json_object[key]
        except (KeyError, TypeError):
            key_value_function = _get_key_value_function(json_object)
            for subkey, subvalue in key_value_function(json_object):
                if fnmatch.fnmatch(str(subkey), str(key)):
                    yield from _iter_path(subvalue, key_path)
            return

    yield json_object


def query(json_object, key_path, predicate=None, selector=None):
    """
    Queries a JSON object. The `key_path` is a list or tuple of strings
    indicating the paths it takes to get to the objects within. Each key
    in the key path can be a wildcard such as "control*", "*_phone", or
    "name_???".

    The `predicate` will be applied to each object that are found at
    the end of the key path. If the `predicate` returns True, then
    the function will pass that object to the `selector` and yield the
    result. If the predicate is omitted, then every objects found will
    be selected. If `selector` is omitted, then the objects will be
    returned as is.

    Given:

        >>> json_object = {
            "controllers": [
                {
                    "controller": 1,
                    "partition": [
                        {
                            "name": "default",
                            "partition_id": 1,
                            "partition_status": "running",
                            "partition_info": "First partition"
                        }
                    ]
                },
                {
                    "controller": 2,
                    "partition": [
                        {
                            "name": "foo",
                            "partition_id": 2,
                            "partition_status": "disabled",
                            "partition_info": "Backup partition"
                        }
                    ]
                }
            ]
        }

    then:

        # Find the names of all partitions
        >>> list(query(json_obj, ("controllers", "*", "partition", "name"))
        ["default", "foo"]

        # Find the partitions that are running
        >>> list(query(json_obj,
                       ("controllers", "*", "partition"),
                       predicate=lambda partition: partition["partition_status"] == "running"))
        [{"partition": {"name": "default",
                        "partition_id": 1,
                        "partition_status": "running",
                        "partition_info": "First partition"}}]

        # Find the names of those partitions that are running
        >>> list(query(json_obj,
                       ("controllers", "*", "partition"),
                       predicate=lambda partition: partition["partition_status"] == "running",
                       selector=lambda partition: partition["partition_name"]))
        ["default"]

    :param json_object: A nested list, dict objects
    :param key_path: A list or tuple of strings indicate the path
    :param predicate: A function that takes an object and returns True/False
    :param select: A function that takes an object and return the fields within
    :return: A generator object that creates a list of object that fits the predicate
    """
    if predicate is None:
        predicate = lambda value: True

    if selector is None:
        selector = lambda value: value

    for value in _iter_path(json_object, key_path):
        if predicate(value):
            yield selector(value)
