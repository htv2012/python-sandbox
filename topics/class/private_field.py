class Foo(object):
    def __init__(self):
        self.public = 5
        self.__private = 10

    @property
    def x(self):
        return self.__private

    @x.setter
    def x(self, value):
        self.__private = value


f = Foo()
print(f.public)
print(f.x)
f.x = 19
print(f.x)
