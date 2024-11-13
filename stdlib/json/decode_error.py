#!/usr/bin/env python3
"""
Decode JSON error
"""

import json


def main():
    """Entry"""
    text = '{"key": "value"'  # Missing closing brace
    try:
        json.loads(text)
    except json.JSONDecodeError as error:
        print("JSON decode error, text:")
        print("---")
        print(error.doc)
        print("---")
        print(error.msg)
        print(f"Position: {error.pos}")
        print(f"Line: {error.lineno}, column: {error.colno}")


if __name__ == "__main__":
    main()
