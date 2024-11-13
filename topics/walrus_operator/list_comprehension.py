#!/usr/bin/env python3


def main():
    """Entry"""
    names = [
        "Ann",
        " Karen ",
        " Ken ",
        " Lisa ",
        "  Anna",
    ]

    print("Select 3-letter names, without walrus:")
    print([name.strip() for name in names if len(name.strip()) == 3])

    print("---")
    print("Select 3-letter names, with walrus:")
    print([n for name in names if len(n := name.strip()) == 3])


if __name__ == "__main__":
    main()
