#!/usr/bin/env python3
"""
whatis: Create priority lists using bisect or heapq
"""

import collections
import bisect
import heapq


Task = collections.namedtuple("Task", "priority name")


def main():
    """Entry"""
    print("# Unordered tasks")
    unordered_tasks = [
        Task(3, "Wash car"),
        Task(2, "Clean kitchen"),
        Task(1, "Feed the dog"),
        Task(2, "Clean office"),
    ]

    for task in unordered_tasks:
        print(f"  {task}")

    print()

    #
    # Using bisect
    #
    print("# Using bisect")
    tasks = []
    for task in unordered_tasks:
        bisect.insort(tasks, task)

    for task in tasks:
        print(f"  {task}")

    print()

    #
    # Using heapq
    #
    print("# Using heapq")
    tasks = unordered_tasks[:]
    heapq.heapify(tasks)
    while tasks:
        task = heapq.heappop(tasks)
        print(f"  {task}")

    print()


if __name__ == "__main__":
    main()
