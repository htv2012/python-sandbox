#!/usr/bin/env python
"""
Search a JSON block for a key.
"""

import logging
from collections import Mapping, Sequence

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def json_find_all(json_data, search_key):
    stack = [json_data]
    while stack:
        block = stack.pop(0)
        logger.debug("block: %r", block)
        logger.debug("stack: %r", stack)

        if isinstance(block, str):
            continue
        elif isinstance(block, Mapping):
            if search_key in block:
                logger.debug("Yield: %r", block[search_key])
                yield block[search_key]
            stack.extend(list(block.values()))
        elif isinstance(block, Sequence):
            logger.debug("Block is a sequence ====> %r", block)
            stack.extend(block)


def json_find_first(json_data, search_key):
    found = json_find_all(json_data, search_key)
    try:
        return next(found)
    except StopIteration:
        raise ValueError("Key not found: %r" % search_key)


def main():
    json_data = {
        "users": [
            {"name": "Peter", "uid": 501},
            {"name": "Paul", "uid": 502},
            {"name": "Mary", "uid": 503},
        ],
        "server": "myserver",
    }

    # Find existent keys
    print("Server:", json_find_first(json_data, "server"))
    print("Users:", ", ".join(json_find_all(json_data, "name")))

    # Find non-existent key
    try:
        print("Role:", json_find_first(json_data, "role"))
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
