"""
How does init inheritance work?
If the derived class does not have __init__, the base class' will be
used
"""


class Base(object):
    def __init__(self, desktop=None):
        self.desktop = desktop


class Foo(Base):
    def show(self):
        print("Desktop:", self.desktop)


f = Foo("Tableau Desktop")
f.show()
