#!/usr/bin/env python3
"""
Aggregated Settings
"""

import collections
import collections.abc
import contextlib
import json
import pathlib

import yaml


def _read_source(source):
    if isinstance(source, collections.abc.Mapping):
        return source

    if isinstance(source, (str, pathlib.Path)):
        path = pathlib.Path(source)
        stream = open(path)
    elif hasattr(source, "read"):
        # A file-like object
        stream = source
    else:
        raise ValueError(f"Expect a dictionary, or file name, not {source!r}")

    start = stream.tell()
    for loader in [json.load, yaml.safe_load]:
        stream.seek(start)

        with contextlib.suppress(json.decoder.JSONDecodeError):
            data = loader(stream)
            return data

    raise ValueError(f"Cannot load {source!r}")


class Settings:
    def __init__(self, *sources):
        self._chain_map = collections.ChainMap(*sources)

    def __getattr__(self, name):
        value = self._chain_map[name]
        with contextlib.suppress(json.decoder.JSONDecodeError, TypeError):
            value = json.loads(value)
        return value

    @classmethod
    def from_mixed_sources(cls, *mixed_sources):
        sources = [_read_source(source) for source in mixed_sources]
        return cls(*sources)
