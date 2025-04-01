#!/usr/bin/env python3
"""Demo problem with using mutable as default parameter."""


class Directive:
    def __init__(self, name, args=[]):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"Directive(name={self.name!r}, args={self.args!r})"


d1 = Directive("D1")
d2 = Directive("D2")

# Problem #1: Modify d1's args will affect d2
d1.args.append("foo")
print(d1)  # Directive(name='D1', args=['foo'])
print(d2)  # Directive(name='D2', args=['foo'])

# Also part of problem #1
d3 = Directive("D3")
print(d3)  # Directive(name='D3', args=['foo'])

# Problem #2: Not making a copy, but use a shared args
my_args = [1, 2, 3]
d4 = Directive("D4", my_args)
print(d4)  # Directive(name='D3', args=[1, 2, 3])
my_args.append(4)
print(d4)  # Directive(name='D3', args=[1, 2, 3, 4])
