"""
Property is slower than data member
"""

import timeit


class Demo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


if __name__ == "__main__":
    a = Demo(5, 7)
    data_time = timeit.timeit("a.x", "from __main__ import a")
    property_time = timeit.timeit("a.y", "from __main__ import a")

    print("Data time:     {:.3} seconds".format(data_time))
    print("property time: {:.3} seconds".format(property_time))
