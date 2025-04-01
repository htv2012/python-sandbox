#!/usr/bin/env python
# encoding: utf-8
"""
formatting_example.py

Created by Hai Vu on 2012-11-02.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

# from __future__ import print_function


class Car:
    make = "Ford"


def main():
    # Dictionary
    d = dict(id=501, alias="haiv", shell="bash")
    print(("Dictionary: {0[alias]}".format(d)))  # haiv

    # List
    names = ["Peter", "Paul", "Mary"]
    print(("List: {0[1]}".format(names)))  # Paul

    # Locals
    filename = "foo.txt"
    print(("Locals: {filename}".format(**locals())))  # foo.txt

    # Alignment
    print(("Left alignment:  >{:<4}<".format(25)))
    print(("Right alignment: >{:4}<".format(25)))
    print(("Zero fill:       >{:04}<".format(25)))
    print(("Dynamic width:   >{:{width}}<".format(25, width=4)))
    print(("Left alignment with fill:   >{:!<10}<".format("text")))
    print(("Right alignment with fill:  >{:!>10}<".format("text")))
    print(("Center alignment with fill: >{:!^10}<".format("text")))

    # Float
    f = 2393.57
    print(("Float, default:             >{}<".format(f)))
    print(("Float, width and precision: >{:12.2f}<".format(f)))
    print(("Float, scientific:          >{:12.2e}<".format(f)))
    print(("Float, with comma:          >{:12,.2f}<".format(f)))
    print(("Percentage:                 >{:12.2%}<".format(0.36592)))

    # Object
    c = Car()
    print(("Format object: {.make}".format(c)))


if __name__ == "__main__":
    main()
