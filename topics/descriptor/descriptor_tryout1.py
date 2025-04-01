import logging
import os

logging.basicConfig(level=os.getenv("LOGLEVEL", logging.WARN))


class RevealAccess(object):
    """A data descriptor that sets and returns values
    normally and prints a message logging their access.
    """

    def __init__(self, value=None, name="var"):
        logging.debug("init: name=%r, value=%r", name, value)
        self.value = value
        self.name = name

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, value):
        logging.debug("set: value=%r", value)
        self.value = value

    def __repr__(self):
        return f"<{self.value!r}>"


class MyClass(object):
    x = RevealAccess(10, "X")
    y = RevealAccess(20)

    def __init__(self):
        self.y = RevealAccess("hello", "Y")

    def __repr__(self):
        return f"MyClass(x={self.x}, y={self.y})"


if __name__ == "__main__":
    print("\n# Create an object")
    m = MyClass()
    print(m)

    print("\n# Modify x")
    m.x = 20
    print(m)

    print("\n# The data descriptor does not work for instance attribute")
    m.y = "world"
    print(m)
