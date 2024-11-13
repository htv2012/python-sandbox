#!/usr/bin/env python3
# camel_killer_box converts displayName -> display_name

from box import Box


def main():
    """Entry"""
    box = Box({"name": "env1", "displayName": "Environment 1"}, camel_killer_box=True)
    print(f"name={box.name!r}")
    print(f"display_name={box.display_name!r}")

    print("\nConvert to JSON:")
    json_object = box.to_json()
    print(json_object)


if __name__ == "__main__":
    main()
