"""Ordered tasks.
A depends on B C
B depends on D E
C depends on F G H
"""

import graphlib


def main():
    """Entry"""
    tasks_hierarchy = {
        "A": ["B", "C"],  # A depends on B and C
        "B": ["D", "E"],  # B depends on D and E
        "C": ["F", "G", "H"],  # C depends on F, G, and H
    }
    tasks = graphlib.TopologicalSorter(tasks_hierarchy)

    print("\n# Task hierarchy: keys are the tasks, values are dependencies")
    print(tasks_hierarchy)

    print("\n# Order to perform tasks")
    print("# Tasks on the same line can be performed concurrently")
    tasks.prepare()
    while tasks.is_active():
        concurrent_tasks = list(tasks.get_ready())
        print(", ".join(concurrent_tasks))
        tasks.done(*concurrent_tasks)


if __name__ == "__main__":
    main()
