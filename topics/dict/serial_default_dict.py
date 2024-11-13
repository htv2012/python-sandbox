""" A defaultdict where each new value is a new increment """

from collections import defaultdict
from itertools import count


def serial_counter(start=0):
    counter = count(start)

    def next_value():
        return next(counter)

    return next_value


if __name__ == "__main__":
    d = defaultdict(serial_counter(101))
    print("d['a'] =", d["a"])
    print("d['b'] =", d["b"])
    print("d['c'] =", d["c"])
    print(dict(d))
