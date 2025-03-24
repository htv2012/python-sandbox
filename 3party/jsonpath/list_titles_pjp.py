import json
import pathlib

import jsonpath


def main():
    data_path = pathlib.Path(__file__).parent / "data" / "bookstore.json"
    with open(data_path) as stream:
        store = json.load(stream)

    print("\n# Book Titles\n")
    titles = jsonpath.findall("$.inventory..title", store)
    for title in titles:
        print(f"- {title}")


if __name__ == "__main__":
    main()
