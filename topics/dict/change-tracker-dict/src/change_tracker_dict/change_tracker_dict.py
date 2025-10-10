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
                super().pop(key, default)
            else:
                ret = super().pop(key, default)
                if ret is NO_DEFAULT:
                    raise KeyError(key)

            self.deleted_keys.append(key)
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
