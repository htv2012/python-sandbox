#!/usr/bin/env python3
"""Resolve dependencies."""

import graphlib


def main():
    """Entry"""
    g = graphlib.TopologicalSorter()
    g.add("env1")
    g.add("gateway1a", "env1")
    g.add("gateway1b", "env1")
    g.add("gateway1c", "env1")

    g.add("app1ax", "gateway1a")
    g.add("app1ay", "gateway1a")
    g.add("app1az", "gateway1a")

    g.add("comp1ax-1", "app1ax")
    g.add("comp1ax-2", "app1ax")
    g.add("comp1ay-1", "app1ay")
    g.add("comp1ay-2", "app1ay")

    for x in reversed(list(g.static_order())):
        print(f"Remove {x}")


if __name__ == "__main__":
    main()
