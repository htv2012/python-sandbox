#!/usr/bin/env python3
"""
How to keep track of changes to a dictionary
"""

import collections

__all__ = ["ChangeTrackerDict"]


class ChangeTrackerDict(collections.ChainMap):
    """A dictionary which tracks changes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deleted_keys = []
        self.tracker = {}
        self.maps.insert(0, self.tracker)

    def __delitem__(self, key):
        # Remove the tracker, delete, then add the tracker back
        del self.maps[0]
        super().__delitem__(key)
        self.maps.insert(0, self.tracker)
        self.deleted_keys.append(key)

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
