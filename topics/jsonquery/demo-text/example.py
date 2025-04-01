#!/usr/bin/env python3
"""

Demo the jsonquery module

"""

import json

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
                    "partition_info": "First partition",
                }
            ],
        },
        {
            "controller": 2,
            "partition": [
                {
                    "name": "foo",
                    "partition_id": 2,
                    "partition_status": "disabled",
                    "partition_info": "Backup partition",
                }
            ],
        },
    ]
}


def print_heading(heading):
    print()
    print("-" * 72)
    print(heading)
    print("-" * 72)


def main():
    """Entry"""
    print_heading("Original Object")
    print(json.dumps(OBJECT_UNDER_TEST, sort_keys=True, indent=4))

    print_heading("Example of iter_path")
    key_path = ("controllers", "*", "partition", "*", "name")
    for value in jsonquery.iter_path(OBJECT_UNDER_TEST, key_path):
        print(value)

    print_heading("Query with both a predicate and a selector")
    result = jsonquery.query(
        OBJECT_UNDER_TEST,
        ("control*", "*", "part*", "*"),
        predicate=lambda v: v["partition_status"] == "disabled",
        selector=lambda v: v["partition_info"],
    )

    for value in result:
        print(value)

    print_heading("Query without a predicate")
    result = jsonquery.query(
        OBJECT_UNDER_TEST,
        ("controllers", "*", "partition", "*"),
        selector=lambda v: v["partition_info"],
    )
    for value in result:
        print(value)


if __name__ == "__main__":
    main()
