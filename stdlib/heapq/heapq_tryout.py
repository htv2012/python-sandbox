#!/usr/bin/env python3
"""
whatis: dynamic sort using heapq
"""

import heapq


def show_heap(heap, label):
    print(f"# {label}")
    print(f"{heap}")
    print()


def main():
    """Entry"""
    numbers = [100, 5, 2, 25]
    show_heap(numbers, "Original")

    heapq.heapify(numbers)
    show_heap(numbers, "After heapify")

    # Adding random numbers
    heapq.heappush(numbers, 67)
    heapq.heappush(numbers, 32)
    show_heap(numbers, "Add some numbers")

    smallest = heapq.heappushpop(numbers, 40)
    show_heap(numbers, f"pushpop 40, get {smallest}")

    smallest = heapq.heappushpop(numbers, 3)
    show_heap(numbers, f"pushpop 3, get {smallest}")

    smallest = heapq.heappushpop(numbers, 325)
    show_heap(numbers, f"pushpop 325, get {smallest}")

    smallest = heapq.heapreplace(numbers, 4)
    show_heap(numbers, f"replace smallest with 4, get {smallest}")

    smallest = heapq.heapreplace(numbers, 81)
    show_heap(numbers, f"replace smallest with 81, get {smallest}")

    n_largest = heapq.nlargest(3, numbers)
    show_heap(numbers, f"3 largest: {n_largest}")

    n_smallest = heapq.nsmallest(3, numbers)
    show_heap(numbers, f"3 smallest: {n_smallest}")


if __name__ == "__main__":
    main()
