#!/usr/bin/env python3
"""
JSON file with comment: how to filter out those comment lines.
"""

import json


def skip_comment_lines(lines):
    """Given a bunch of lines (any iterable), return a generator of good lines"""
    return (line for line in lines if not line.strip().startswith("#"))


if __name__ == "__main__":
    with open("with_comments.json") as f:
        no_comment = "\n".join(skip_comment_lines(f))
        data = json.loads(no_comment)
        print(json.dumps(data, indent=4, sort_keys=True))
