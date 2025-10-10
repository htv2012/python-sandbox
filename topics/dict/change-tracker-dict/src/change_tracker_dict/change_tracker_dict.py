#!/usr/bin/env python3
"""
How to keep track of changes to a dictionary
"""

import collections
import contextlib

__all__ = ["ChangeTrackerDict"]
NO_DEFAULT = object()


class ChangeTrackerDict(collections.ChainMap):
    """A dictionary which tracks changes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deleted_keys = []
        self.tracker = {}
        self.maps.insert(0, self.tracker)

    def pop(self, key, default=NO_DEFAULT):
        with self.no_tracker():
            if key in self.tracker:
                ret = self.tracker.pop(key, default)
                ret2 = super().pop(key, default)
                self.deleted_keys.append(key)
                if ret is NO_DEFAULT and ret2 is NO_DEFAULT:
                    raise KeyError(key)
                elif ret is not NO_DEFAULT:
                    return ret
                else:
                    return ret2
            else:
                ret = super().pop(key, default)
                self.deleted_keys.append(key)
                if ret is NO_DEFAULT:
                    raise KeyError(key)
                return ret

    def __delitem__(self, key):
        self.pop(key)

    @contextlib.contextmanager
    def no_tracker(self):
        """Temporarily remove the tracker, then add back on"""
        del self.maps[0]
        try:
            yield
        finally:
            self.maps.insert(0, self.tracker)

    @property
    def changed(self) -> bool:
        return bool(self.tracker or self.deleted_keys)

    @property
    def changes(self) -> list:
        updates = [
            f"Updated: [{key!r}]={value!r}" for key, value in self.tracker.items()
        ]
        deletions = [f"Deleted: [{key!r}]" for key in self.deleted_keys]
        return updates + deletions
