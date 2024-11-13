#!/usr/bin/env python3
from collections import deque, namedtuple
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

class Column:
    def __init__(self, name, discs):
        self.name = name
        self.discs = deque(discs)

    def pop(self):
        return self.discs.popleft()
    
    def put(self, disc):
        self.discs.appendleft(disc)
    
    def __len__(self):
        return len(self.discs)
    
    def __str__(self):
        return f"[{self.name}]"
    
    def __repr__(self):
        return f"{self.name}{list(self.discs)}"
    
def move(count: int, source: Column, dest: Column, temp: Column):
    LOGGER.debug("move(count=%r, source=%r, dest=%r, temp=%r)", count, source, dest, temp)
    if count == 0:
        return
    assert len(source) > 0, f"{source=}, {dest=}, {temp=}"

    # Move all but the bottom disc to temp...    
    yield from move(count - 1, source, temp, dest)

    # So we can move the bottom disc to dest
    disc = source.pop()
    dest.put(disc)
    yield disc, source.name, dest.name
    
    # Move all the top discs from temp to dest
    yield from move(count - 1, temp, dest, source)


source = Column("A", [1,2,3])
dest = Column("B", [])
temp = Column("C", [])

print(f"{source}: {source.discs}")
print(f"{dest}: {dest.discs}")
print(f"{temp}: {temp.discs}")
print()

operations = move(3, source, dest, temp)
for operation in operations:
    print("Move disc (%d) from %s to %s" % operation)
