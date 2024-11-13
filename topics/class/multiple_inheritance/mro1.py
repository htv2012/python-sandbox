#!/usr/bin/env python

""" What's the init sequence is like for multiple inheritance """


class Base1(object):
    def __init__(self):
        print("Base1.__init__")


class Base2(object):
    def __init__(self):
        print("Base1.__init__")


class Multi(Base1, Base2):
    def __init__(self):
        super(Multi, self).__init__()
        print("Multi.__init__")


if __name__ == "__main__":
    m = Multi()
