#!/usr/bin/env python3
def return_within_try():
    try:
        return "return value"
    finally:
        print("finally")


def return_within_except():
    try:
        raise TypeError("Out of coffee")
    except TypeError as e:
        print(repr(e))
        return "error"
    finally:
        print("finally")


def raise_within_try():
    try:
        raise ValueError("Out of milk")
    finally:
        print("finally")


def main():
    print("\n# return within try")
    print(return_within_try())

    print("\n# return within except")
    print(return_within_except())

    print("\n# raise within try")
    try:
        raise_within_try()
    except Exception as error:
        print(repr(error))


if __name__ == "__main__":
    main()
