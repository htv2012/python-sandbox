#!/usr/bin/env python3
"""Resolve dependencies using a dictionary.

Also: demonstrate set operations.
"""
import copy


def determine_order(tasks):
    # Make duplicate, we don't want to destroy the original
    tasks = copy.deepcopy(tasks)

    # Compile a list of all the tasks
    remaining = set()
    for node, dependencies in tasks.items():
        remaining.add(node)
        remaining.update(dependencies)

    # Perform tasks, in order
    while remaining:
        # These can be done concurrently
        todo = remaining - tasks.keys()
        yield todo

        # Remove finished tasks from the tasks hierarchy
        tasks = {
            key: updated_value
            for key, value in tasks.items()
            if (updated_value := value - todo)
        }

        # Remove finished tasks from the set of remaining tasks
        remaining -= todo


def main():
    """Perform script."""
    tasks_hierarchy = {
        "A": {"B", "C"},  # A depends on B and C
        "B": {"D", "E"},  # B depends on D and E
        "C": {"F", "G", "H"},  # C depends on F, G, and H
    }
    print("Task hierarchy:")
    for task, depend in tasks_hierarchy.items():
        print(f"- {task} depends on {', '.join(depend)}")
    print()

    for concurrent_tasks in determine_order(tasks_hierarchy):
        concurrent = ""
        if len(concurrent_tasks) > 1:
            concurrent = " concurrently"
        print(f"Perform{concurrent}: {', '.join(concurrent_tasks)}")


if __name__ == "__main__":
    main()
