#!/usr/bin/env python3
""" """


def raise_me(exception_object):
    raise exception_object


def try_me(exception_object):
    try:
        raise_me(exception_object)
    except Exception as exc:
        print("Ignoring:", exc)


def try_me_with_class(klass, message):
    exception_object = klass(message)
    try_me(exception_object)


def true_or_raise(value, exception_object):
    if value:
        return
    raise exception_object


def try_true_or_raise(value, exception_object):
    print("Value:", value)

    try:
        true_or_raise(value, exception_object)
    except Exception as exc:
        print("Ignoring", exc)


def main():
    """Entry"""
    try_me(RuntimeError("Out of milk"))
    try_me(KeyError("Invalid key: F-"))
    try_me_with_class(RuntimeError, "Bad coffee")

    try_true_or_raise(5, RuntimeError("Five is good"))
    try_true_or_raise(0, RuntimeError("Five is good"))


if __name__ == "__main__":
    main()
