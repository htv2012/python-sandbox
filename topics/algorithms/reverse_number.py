#!/usr/bin/env python
""" Referse a number """


def reverse_number(number):
    sign = number // abs(number)
    str_form = "".join(reversed(str(abs(number))))
    number = int(str_form) * sign
    return number


for number in [-1, 2, 12345, -23456789]:
    print("Original: {!r}, reversed: {!r}".format(number, reverse_number(number)))
