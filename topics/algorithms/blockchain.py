#!/usr/bin/env python3
"""
A crude blockchain
"""
import collections


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash

    def __hash__(self):
        return hash(self.data)

    def __repr__(self):
        return f"Block(data={self.data!r}, hash={hash(self)!r}, previous_hash={self.previous_hash!r})"


class Blockchain:
    SENTINEL = None

    def __init__(self):
        self.block = {}
        self.last_hash = Blockchain.SENTINEL
        self.chain = collections.deque()

    def __iter__(self):
        for hash_ in self.chain:
            yield self.block[hash_]

    def add(self, data):
        block = Block(data, previous_hash=self.last_hash)
        self.last_hash = hash(block)
        self.chain.appendleft(self.last_hash)
        self.block[self.last_hash] = block


def main():
    """Entry"""
    bc = Blockchain()
    bc.add("Peter")
    bc.add("Paul")
    bc.add("Mary")

    for block in bc:
        print(block)


if __name__ == "__main__":
    main()
