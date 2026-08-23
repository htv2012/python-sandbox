#!/usr/bin/env python3
import mmap
import pathlib


def main():
    path = pathlib.Path("/tmp/data.txt")
    path.write_text("hello world")
    print("# content before modification")
    print(path.read_text())

    with open("/tmp/data.txt", "r+b") as stream, mmap.mmap(stream.fileno(), 0) as m:
        print("\n# modify the first 5 bytes")
        m[:5] = b"Howdy"

    print("\n# content after modification")
    print(path.read_text())


if __name__ == "__main__":
    main()
