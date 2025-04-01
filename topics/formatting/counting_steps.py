#!/usr/bin/env python3
"""
Demo: Prints the steps with automatic step numbers
"""


def steps_counter(number=1):
    def step(message):
        nonlocal number
        result = "%2d. %s" % (number, message)
        number += 1
        return result

    return step


def main():
    """Entry"""
    step = steps_counter()
    print(step("Creating objects"))
    print(step("Query missing parameters"))
    print(step("Report"))


if __name__ == "__main__":
    main()
