import types


class Profile:
    """Profile a function"""

    def __init__(self, func):
        # functools.wraps(func)(self)
        self.func = func
        self.__doc__ = func.__doc__
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profile
def greet(name):
    """Show greetings"""
    print("Hello {name}".format(**locals()))


if __name__ == "__main__":
    greet("Johnny")
    greet("Frankie")
    print("Greet was called {} time(s)".format(greet.ncalls))
    print("Doc:", greet.__doc__)
