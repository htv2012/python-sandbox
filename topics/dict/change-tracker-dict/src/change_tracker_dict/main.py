#!/usr/bin/env python3

from change_tracker_dict import ChangeTrackerDict


def main():
    original = {"a": 1, "b": 2}
    print(f"{original=}")

    # Start tracking changes
    original = ChangeTrackerDict(original)

    # Make changes
    original["a"] = 10
    del original["b"]
    original["c"] = 30

    # Report
    print(f"After changes: {dict(original)}")
    print("Changes are:")
    for change in original.changes:
        print(change)


if __name__ == "__main__":
    main()
