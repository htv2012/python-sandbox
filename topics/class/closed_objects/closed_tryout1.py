#!/usr/bin/env python
from closed_objects import mark_as_closed


class User(object):
    # @accessible_while_closed
    def greet(self):
        print("Hello")

    def close(self):
        mark_as_closed(self)


if __name__ == "__main__":
    user = User()
    user.greet()

    user.close()
    user.greet()
