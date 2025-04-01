class Foo(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        attrs = ", ".join(
            "{}={!r}".format(k, v) for k, v in list(self.__dict__.items())
        )
        return "{}({})".format(self.__class__.__name__, attrs)
