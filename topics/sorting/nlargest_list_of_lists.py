#!/usr/bin/python3
"""Get the largest/smallest from many lists."""

import heapq
import pprint


def main():
    scores = [
        [89.5, 95.1, 73.2],  # Class 1
        [69.0, 72.2, 77.0],  # Class 2
        [97.0, 99.0, 67.1],  # Class 3
    ]

    print("\n# scores")
    pprint.pprint(scores, indent=4)

    print("\n# Top 3 highest scores")
    que = heapq.merge(*scores)
    print(heapq.nlargest(3, que))

    print("\n# Top 3 lowest scores")
    que = heapq.merge(*scores)
    print(heapq.nsmallest(3, que))


if __name__ == "__main__":
    main()
