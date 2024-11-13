#!/usr/bin/env python3
"""
Load symbols.
"""
import argparse
import json
import os
import sys


def load(path=None):
    path = path or os.getenv("TESTRUN_SYMBOLS") or os.get("SYSTEST_SYMBOLS")
    assert os.path.exists(path), f"Path not found: {path}"

    with open(path, "r", encoding="utf-8") as stream:
        symbols = json.load(stream)

    return symbols


def main():
    """Load and print the symbols."""
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    options = parser.parse_args()

    symbols = load(options.path)
    json.dump(symbols, sys.stdout, indent=4)


if __name__ == "__main__":
    main()
