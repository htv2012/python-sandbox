import collections.abc

MISSING = object()


class ChangeTrackerDict(collections.abc.MutableMapping):
    """Like an elephant, this dict remembers changes made to it."""

    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
        self._ledger = []

    def __delitem__(self, key):
        prev_value = self._data.get(key, MISSING)
        del self._data[key]
        self._ledger.append(dict(action="del", key=key, prev_value=prev_value))

    def __setitem__(self, key, value):
        prev_value = self._data.get(key, MISSING)
        self._data[key] = value
        self._ledger.append(
            dict(action="set", key=key, prev_value=prev_value, value=value)
        )

    @property
    def dirty(self):
        return bool(self._ledger)

    @property
    def changes(self):
        return self._ledger.copy()

    #
    # Mundance stuff
    #

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __repr__(self):
        return f"ChangeTrackerDict({self._data!r})"


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
