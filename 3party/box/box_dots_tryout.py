#!/usr/bin/env python3
"""Demo: with box_dots param, we can use key with dots to traverse."""

import box


def main():
    data = {
        "metadata": {
            "name": "myenv",
            "description": "My First environment",
            "tags": ["sandbox", "experimental"],
        }
    }
    print("\n# Original data:")
    bx = box.Box(data, box_dots=True)
    print(f"{bx=}")

    print("\n# Access using keys with dots:")
    print(f"{bx['metadata.name']=}")
    print(f"{bx['metadata.description']=}")
    print(f"{bx['metadata.tags']=}")

    print("\n# DDBox is almost the same:")
    bx = box.DDBox(data)
    print(f"{bx['metadata.name']=}")
    print(f"{bx['metadata.description']=}")
    print(f"{bx['metadata.tags']=}")


if __name__ == "__main__":
    main()
