#!/usr/bin/env python3
"""
Use the assignment expression (AKA walrus operator) to simplify the
if statement.
"""


def main():
    """Entry"""
    d = {"metadata": {"name": "John"}}

    # Without walrus
    if d.get("metadata", {}).get("name") is not None:
        print(f"Hello {d.get('metadata', {}).get('name')}")

    # With walrus
    if (name := d.get("metadata", {}).get("name")) is not None:
        print(f"Hello {name}")


if __name__ == "__main__":
    main()
