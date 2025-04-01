#!/usr/bin/env python
import collections


class OneBasedTuple(collections.abc.Sequence):
    """
    A tuple where index starts at 1 instead of the usual 0. For example:

        names = Base1Tuple(["Alex", "Beatrice", "Carmen"])
        assert names[1] == "Alex"
        assert names[2] == "Beatrice"
        assert names[3] == "Carmen"
        assert names[-1] == "Carmen"
        # names[0] or names[4] will raise an IndexError
    """

    def __init__(self, iterable=None):
        self._tuple = tuple(iterable or [])

    def _validate_index(self, index):
        if index == 0:
            raise IndexError(f"Index out of range, expect 1-{len(self)}, not {index}")

    def _get_slice(self, slice_object):
        start = slice_object.start
        stop = slice_object.stop
        step = slice_object.step
        self._validate_index(start)

        if start > 0:
            start = start - 1
        if stop > 0:
            stop -= 1

        new_slice = slice(start, stop, step)
        return self._tuple[new_slice]

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._get_slice(index)
        self._validate_index(index)
        if index > 0:
            index = index - 1

        return self._tuple[index]

    def __iter__(self):
        return iter(self._tuple)

    def __len__(self):
        return len(self._tuple)
