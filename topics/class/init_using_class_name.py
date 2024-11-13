#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
initialize using class name
"""


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value
        print("MyBaseClass.__init__, value={}".format(self.value))


class TimesTwo(object):
    def __init__(self):
        self.value *= 2
        print("TimesTwo.__init__, value={}".format(self.value))


class PlusFive(object):
    def __init__(self):
        self.value += 5
        print("PlusFive.__init__, value={}".format(self.value))


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)

        # self.value depends on the order of initialization. Switch them
        # and observe
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print("main, value={}".format(foo.value))


#
# Diamond inheritance will cause problem
#


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print("main diamond, value={}".format(foo.value))


# ======================================================================
# To correct for the diamond inheritance problem, use super
# ======================================================================


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5
        print("TimesFiveCorrect.__init__, value={}".format(self.value))


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2
        print("PlusTwoCorrect.__init__, value={}".format(self.value))


# class GoodWay(PlusTwoCorrect, TimesFiveCorrect):
class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)
        print("GoodWay.__init__, value={}".format(self.value))


print("\nDiamond:")
foo = GoodWay(5)
print("MRO:")
for cls in GoodWay.__mro__:
    print("- {}".format(cls))
