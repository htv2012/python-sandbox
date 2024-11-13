#!/usr/bin/env python3
from typed_input import typed_input

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self.x,
            self.y)

    @classmethod
    def from_csv_string(cls, csv_string):
        parameters = [float(n.strip()) for n in csv_string.split(',')]
        return cls(*parameters)

if __name__ == '__main__':
    v = typed_input(
        prompt='Enter two numbers separated by comma: ',
        return_type=Vector.from_csv_string)
    print('Vector:', v)
