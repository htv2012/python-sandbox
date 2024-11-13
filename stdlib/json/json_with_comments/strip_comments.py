#!/usr/bin/env python3
import json
import re


def strip_comments_from_string(buffer):
    """
    Strip comment lines from a string buffer
    """
    comments = re.compile(r"^\s*#.*$", re.MULTILINE)
    return re.sub(comments, "", buffer)


def strip_comments_from_readable(readable):
    """
    Strip comment lines from any object which has .read() method
    """
    buffer = readable.read()
    return strip_comments_from_string(buffer)


if __name__ == "__main__":
    with open("with_comments.json") as f:
        data = json.loads(strip_comments_from_readable(f))
        print(json.dumps(data, indent=4, sort_keys=True))
