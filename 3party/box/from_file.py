#!/usr/bin/env python3
import pathlib

import box


def main():
    data_path = pathlib.Path(__file__).with_name("data")
    for path in data_path.glob("data.*"):
        bx = box.box_from_file(path)
        print(f"\n# From {path.name}\n{bx!r}")


if __name__ == "__main__":
    main()
