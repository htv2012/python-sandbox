#!/usr/bin/env python3
"""
Tower of Hanoi
"""

import collections


class Stack(collections.deque):
    def push(self, element):
        self.appendleft(element)

    def pop(self):
        return self.popleft()

    def get_elements(self):
        count = self.maxlen
        elements = [" "] * count + list(self)
        return elements[-count:]


def print_stacks(stacks):
    print()
    print(" ".join(stacks))
    print("- - -")
    height = max(map(len, stacks.values()))
    grid = zip(*[stack.get_elements() for stack in stacks.values()])
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


def move(stacks, count, src, dest, temp):
    # print(f"Stacks: {stacks}")
    # print(f"count={count}, src={src}, dest={dest}, temp={temp}")
    # print()

    if count == 1:
        top = stacks[src].pop()
        stacks[dest].push(top)
        print_stacks(stacks)
        print(f"Move disc {top}, {src} -> {dest}")
    else:
        # Moves all, but the last disc src -> temp
        move(stacks, count - 1, src=src, dest=temp, temp=dest)

        # Move bottom disc src -> dest
        bottom = stacks[src].pop()
        stacks[dest].push(bottom)
        print_stacks(stacks)
        print(f"Move disc {bottom}, {src} -> {dest}")

        # Move all temp -> dest
        move(stacks, count - 1, src=temp, dest=dest, temp=src)


def hanoi(n):
    stacks = dict(
        A=Stack(range(1, n + 1), maxlen=n),
        B=Stack(maxlen=n),
        C=Stack(maxlen=n),
    )
    print(f"Starts with {n} discs, where disc 1 is on top")
    print_stacks(stacks)
    move(stacks, count=len(stacks["A"]), src="A", dest="C", temp="B")


def main():
    """Entry"""
    hanoi(4)


if __name__ == "__main__":
    main()
