"""
Dynamically set attributes for a class
"""


class Foo(object):
    def __init__(self, **kwargs):
        for k, v in list(kwargs.items()):
            setattr(self, k, v)
            # self.__setattr__(k, v)


f2 = Foo(shell="/bin/bash", group="wheels")
print(f2.shell)
print(f2.group)
