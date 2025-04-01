#!/usr/bin/env python3
from const import Const


def main():
    """Entry"""
    print("\n# Demo: Create and show")
    color = Const(red=1, green=2)
    print(f"{color=}")
    print(f"{color.red=}")
    print(f"color.red==1? {color.red == 1}")

    print("\n# Demo: iter")
    print(f"Is 2 in color? {2 in color}")
    print(f"{list(color) = }")

    print("\n# Demo: read-only")
    print("Attempt to redefine a const")
    try:
        color.green = 100
    except TypeError as error:
        print(f"ERROR: {error}")

    print("\n# Demo: Backdoor #1: __dict__")
    print("Add blue=3")
    color.__dict__["blue"] = 3  # Add a new const
    print(f"{color=}")

    print("\n# Demo: Backdoor #2: vars()")
    print("Set red=0")
    inner_data = vars(color)
    inner_data["red"] = 0
    print(f"{color=}")


if __name__ == "__main__":
    main()
