#!/usr/bin/env python

# Implements a dictionary with lower-case keys

import collections.abc


class Headers(collections.abc.MutableMapping):
    def __init__(self, dict_object=None):
        if dict_object is None:
            dict_object = {}
        self._data = {self._normalize(key): value for key, value in dict_object.items()}

    @staticmethod
    def _normalize(key):
        return "-".join(tok.title() for tok in key.split("-"))

    def __setitem__(self, key, value):
        key = self._normalize(key)
        self._data[key] = value

    def __getitem__(self, key):
        key = self._normalize(key)
        return self._data[key]

    def __delitem__(self, key):
        key = self._normalize(key)
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)
