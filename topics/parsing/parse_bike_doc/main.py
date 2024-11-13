#!/usr/bin/env python3
import pathlib

import bike


def main():
    script_dir = pathlib.Path(__file__).parent
    for doc_path in script_dir.glob("commute_packing.*"):
        print(f"\n# {doc_path}")
        outline = bike.parse_bike(doc_path)
        bike.print_outline(outline)

    # doc_path = pathlib.Path(__file__).with_name("commute_packing.opml")
    # assert doc_path.exists()
    # outline = bike.parse_bike_opml(doc_path)
    # print("\n# Raw outline")
    # print(json.dumps(outline, indent=4))
    # print("\n# Using print_outline()")
    # bike.print_outline(outline)


if __name__ == "__main__":
    main()
