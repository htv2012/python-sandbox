#!/usr/bin/env python3
"""
Convert a dictionary to object so we can use the dot notation, which is
more convenient
"""

import collections.abc


class NestedDict(collections.abc.Mapping):
    def __init__(self, dic):
        self.__dic = dic

    def __iter__(self):
        return iter(self.__dic)

    def __getitem__(self, key):
        value = self.__dic[key]
        if isinstance(value, dict):
            value = NestedDict(value)
        return value

    __getattr__ = __getitem__

    def __truediv__(self, path):
        obj = self
        for key in path.split("/"):
            obj = obj[key]
        return obj

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        kv = ", ".join("{}={!r}".format(k, v) for k, v in list(self.items()))
        result = "{}({})".format(self.__class__.__name__, kv)
        return result


def main():
    person = NestedDict(
        {"alias": "adam", "phone": {"office": "123-4567", "mobile": "987-6543"}}
    )

    # Access using attributes and keys
    print("Alias:", person.alias)
    print("Office:", person.phone.office)
    print("Mobile:", person["phone"]["mobile"])

    # Access using loop
    print("---")
    for k, v in list(person.phone.items()):
        print("{}: {}".format(k, v))

    # Access using slash (__truediv__)
    print("---")
    print("Mobile phone:", person / "phone" / "mobile")
    print("Office phone:", person / "phone/office")


if __name__ == "__main__":
    main()
