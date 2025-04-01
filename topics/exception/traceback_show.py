# Print traceback

import sys
import traceback


def greet(name):
    global ex, exc, value, tb
    print("Hello, {}".format(name))
    try:
        print(foo)
    except NameError:
        exc, value, tb = sys.exc_info()
        traceback.print_exc()


if __name__ == "__main__":
    greet("John")
