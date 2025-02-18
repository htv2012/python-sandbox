# nested dict
import collections.abc
import reprlib


class DotKeyDict(collections.abc.MutableMapping):
    def __init__(self, raw: dict = None, separator="."):
        self.raw = raw or {}
        self.separator = separator

    def __len__(self):
        return len(self.raw)

    def __iter__(self):
        return iter(self.raw)

    def __getitem__(self, key):
        keys = key.split(self.separator)
        node = self.raw
        for sub_key in keys:
            try:
                node = node[sub_key]
            except (TypeError, KeyError):
                if sub_key.isnumeric() and isinstance(node, list):
                    node = node[int(sub_key)]
                else:
                    raise KeyError(f"{key}: {sub_key} not found")
        return node

    def __setitem__(self, key, value):
        keys = key.split(self.separator)
        leaf_key = keys.pop()
        node = self.raw
        for key in keys:
            node = node.setdefault(key, {})
        node[leaf_key] = value

    def __delitem__(self, key):
        keys = key.split(self.separator)
        leaf_key = keys.pop()
        node = self.raw
        for sub_key in keys:
            if sub_key not in node:
                raise KeyError(f"{key}: {sub_key} not found")
            node = node[sub_key]
        if leaf_key not in node:
            raise KeyError(f"{key}: {leaf_key} not found")
        del node[leaf_key]

    def __repr__(self):
        return reprlib.repr(self.raw)
