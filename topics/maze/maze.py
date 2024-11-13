#!/usr/bin/env python


class Cell(object):
    def __init__(self, name, neighbors=None):
        self.name = name
        if neighbors is None:
            neighbors = []
        self.neighbors = list(neighbors)


def find_path(start, dest, seen=None):
    if start is dest:
        return [start]

    if seen is None:
        seen = set()
    seen.add(start)

    for ncell in start.neighbors:
        if ncell in seen:
            continue

        path = find_path(ncell, dest, seen)
        if path is not None:
            return [start] + path

    return None



