#!/usr/bin/env python3
"""Demo: Box leaves original data untouched."""

import json

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
    print("\n#Original Data:")
    print(json.dumps(data, indent=4))

    print("\n# Create box")
    bx = box.Box(data)
    print(bx)

    print("\n# After modification")
    bx.metadata.description = "modified"
    print(bx)

    print("\n# Original data:")
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()
