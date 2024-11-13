def greet(name):
    print("Hello, {}".format(name))


class Foo:
    greet2 = staticmethod(greet)
    greet = staticmethod(greet)


if __name__ == "__main__":
    greet("world")
    Foo.greet2("world2")
    Foo.greet("world3")
