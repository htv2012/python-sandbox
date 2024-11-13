from collections import MutableMapping


class CaseInsensitiveDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._dict = dict()
        for k, v in args:
            self._dict[k.lower()] = v
        for k, v in kwargs.items():
            self._dict[k.lower()] = v

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __getitem__(self, name):
        return self._dict[name.lower()]

    def __setitem__(self, key, value):
        key = key.lower()
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]
        pass


d = CaseInsensitiveDict(("Karen", 89), ("Norine", 93), Jake=95, Anna=96)
d["John"] = 97
print(d["JOHN"])

print("---")
print("\n".join("{}: {}".format(*kv) for kv in d.items()))
