#!/usr/bin/env python

# Implements a dictionary with lower-case keys

import collections


class LowerCaseDict(collections.MutableMapping):
    def __init__(self):
        self.map = {}

    def __repr__(self):
        kv = ", ".join(["{0}:{1}".format(k, v) for k, v in self.map.items()])
        return "<LowerCaseDict {" + kv + "} >"

    # === Implement the ABC ===
    def __setitem__(self, key, value):
        key = key.lower()
        self.map[key] = value

    def __getitem__(self, key):
        key = key.lower()
        return self.map[key]

    def __delitem__(self, key):
        key = key.lower()
        del self.map[key]

    def __iter__(self):
        return iter(self.map)

    def __len__(self):
        return len(self.map)

    # === End ABC ====


# Try out
d = LowerCaseDict()
d["HAMMER"] = 374
d["Saw"] = 19

print(d)
