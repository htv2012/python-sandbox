import collections.abc
import reprlib
from typing import Iterable, Optional


class frozendict(collections.abc.Mapping):
    def __init__(self, iterable: Optional[Iterable] = None, **kwargs):
        raw = dict(iterable or tuple()) or dict(**kwargs)
        self.__data = raw

    def __getitem__(self, key):
        return self.__data[key]

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    def __hash__(self):
        return hash(repr(self.__data))

    def __repr__(self) -> str:
        content = reprlib.repr(self.__data)
        return f"{self.__class__.__name__}({content})"
