#!/usr/bin/env python3
"""
Remove hierarchical objects
"""

import graphlib
import json

hierarchy = {
    "A1": {
        "A1.1": {
            "A1.1.1": {},
            "A1.1.2": {},
            "A1.1.3": {},
        },
        "A1.2": {
            "A1.2.1": {},
            "A1.2.2": {},
        },
    },
    "B1": {
        "B1.1": {
            "B1.1.1": {},
            "B1.1.2": {},
            "B1.1.3": {},
        }
    },
    # B2 is odd: it depends on objects elsewhere
    "B2": {
        "A1.1": {},
        "A1.2": {},
        "B1.1": {},
    },
}


def build_dependencies(hier: dict):
    que = [hier]
    dependencies = graphlib.TopologicalSorter()

    while que:
        node = que.pop()
        for key, value in node.items():
            dependencies.add(key, *list(value))
            que.append(value)

    return dependencies


def cleanup_concurrently(dependencies: graphlib.TopologicalSorter):
    dependencies.prepare()
    while dependencies.is_active():
        batch = dependencies.get_ready()
        print(f"- Remove concurrently: {batch}")
        dependencies.done(*batch)


def main():
    print("\n# Objects Hierarchy")
    print(json.dumps(hierarchy, indent=4))

    dependencies = build_dependencies(hierarchy)
    print("\n# Clean up")
    cleanup_concurrently(dependencies)


if __name__ == "__main__":
    main()
