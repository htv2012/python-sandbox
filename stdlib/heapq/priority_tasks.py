#!/usr/bin/env python3
"""
whatis: Create priority tasks list using heapq
"""

import collections
import heapq
from heapq import heappop, heappush, heappushpop, heapreplace

Task = collections.namedtuple("Task", ["priority", "name"])


def main():
    """Entry"""
    print("\n# Unordered tasks")
    tasks = [
        Task(3, "Wash car"),
        Task(2, "Clean kitchen"),
        Task(1, "Feed Fido"),
        Task(2, "Clean office"),
    ]

    for task in tasks:
        print(task)

    heapq.heapify(tasks)
    print("\n# Tasks after heapify")
    for task in tasks:
        print(task)

    task = Task(1, "Turn off light")
    print("\n# Add new task")
    print(f"Add: {task}")
    heappush(tasks, task)

    print("\n# Work on")
    print(f"Do: {heappop(tasks)}")
    print(f"Do: {heappop(tasks)}")

    print("\n# Push, then pop")
    task = Task(1, "Order food")
    print(f"Add: {task}")
    print(f"Do: {heappushpop(tasks, task)}")

    print("\n# Pop, then push")
    to_add = Task(1, "Call service")
    print(f"Add: {to_add}")
    to_do = heapreplace(tasks, to_add)
    print(f"Do: {to_do}")


if __name__ == "__main__":
    main()
