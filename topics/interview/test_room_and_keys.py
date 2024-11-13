#!/usr/bin/env python
"""
There are n rooms labeled from 0 to n - 1 and all the rooms are
locked except for room 0. Your goal is to visit all the rooms.
However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks, and
you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can
obtain if you visited room i, return true if you can visit all the
rooms, or false otherwise.
"""
from typing import List

import pytest


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Set of room numbers which are opened
        opened = set()

        # Set of unused keys
        unused_keys = {0}

        while unused_keys:
            key = unused_keys.pop()
            opened.add(key)
            new_keys = set(rooms[key]) - opened
            unused_keys |= new_keys

        return len(opened) == len(rooms)


def test_positive1():
    solution = Solution()
    assert solution.canVisitAllRooms([[1], [2], [3], []])


def test_positive2():
    solution = Solution()
    assert solution.canVisitAllRooms([[1, 3], [2, 4], [5], [], [], []])


def test_negative1():
    solution = Solution()
    assert not solution.canVisitAllRooms([[1, 3], [1, 3], [], []])


def test_negative2():
    solution = Solution()
    assert not solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
