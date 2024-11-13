"""List the titles of the books."""

import json

from jsonpath_ng import parse


def main():
    """Entry"""
    with open("data/bookstore.json") as stream:
        data = json.load(stream)

    print("\n# Book Titles\n")
    titles = parse("inventory[*].title")
    for datum in titles.find(data):
        print(f"- {datum.value}")


if __name__ == "__main__":
    main()
