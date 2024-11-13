#!/usr/bin/env python3
"""
A collection of tools to work with JSON objects
"""
import jsonquery


OBJECT_UNDER_TEST = {
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


def test_query_without_predicate_without_selector():
    actual = list(jsonquery.query(
        OBJECT_UNDER_TEST,
        ("controllers", "*", "partition", "*", "name"),
    ))
    assert actual == ["default", "foo"]

def test_query_without_selector():
    actual = list(jsonquery.query(
        OBJECT_UNDER_TEST,
        ("controllers", "*", "partition", "*", "name"),
        predicate=lambda name: name.startswith("d")
    ))
    assert actual == ["default"]

def test_query_with_predicate_and_selector():
    actual = list(jsonquery.query(
        OBJECT_UNDER_TEST,
        ("controllers", "*", "partition", "*"),
        predicate=lambda partition: partition["name"] == "default",
        selector=lambda partition: partition["partition_status"],
    ))
    assert actual == ["running"]
