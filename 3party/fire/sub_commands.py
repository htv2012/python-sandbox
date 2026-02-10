#!/usr/bin/env python3
"""
Sub commands
"""

import fire


def hi(name: str = "world"):
    print(f"Hello, {name}")


def bye(name: str = "world"):
    print(f"Goodbye, {name}")


if __name__ == "__main__":
    fire.Fire()
