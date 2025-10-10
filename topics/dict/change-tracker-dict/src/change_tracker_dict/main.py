#!/usr/bin/env python3

from change_tracker_dict import ChangeTrackerDict


def main():
    print()
    print("ChangeTrackerDict Demo")

    original = {"a": 1, "b": 2}
    print()
    print(f"{original = }")

    # Start tracking changes
    original = ChangeTrackerDict(original)

    # Make changes
    original["a"] = 10
    del original["b"]
    original["c"] = 30
    original.pop("c")
    original.update({"d": 40, "e": 50})

    # Report
    print()
    print(f"After changes = {dict(original)}")

    print()
    print("The following changes were recorded:")
    for change in original.changes:
        print(change)


if __name__ == "__main__":
    main()
