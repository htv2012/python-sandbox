#!/usr/bin/env python3
# https://xiaoxing.us/2018/04/15/singleton-in-python/
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Env(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class SubEnv(Env):
    pass


c1 = Config("foo")
c2 = Config("bar")
c3 = Config()
assert c1 is c2
assert c1 is c3
assert c1.name == "foo"
assert c2.name == "foo"
assert c3.name == "foo"

env1 = Env("blah")
env2 = Env("blah")
se1 = SubEnv("moo")
print(Singleton._instances)
