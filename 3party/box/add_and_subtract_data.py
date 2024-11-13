#!/usr/bin/env python3
"""Demo: Add data to and subtract data from a box."""

import box


def main():
    """Entry"""
    data = {
        "metadata": {
            "name": "myenv",
            "description": "My First environment",
            "tags": ["sandbox", "experimental"],
        }
    }
    bx = box.Box(data)
    print("\n# Original box")
    print(bx)

    print("\n# Add more data")
    bx = bx + {"payload": {}}
    bx += {"metadata": {"tags": ["tag1", "tag2"]}}  # Will orverwrite
    bx += box.Box(metadata={"name": "MYENV_1"})
    print(bx)

    print("\n# Subtract data")
    bx -= {"payload": {}}
    print(bx)


if __name__ == "__main__":
    main()
