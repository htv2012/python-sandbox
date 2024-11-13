# Simple module to parse
print('>>>foo')

class MyEnum:
    red = 1
    green = 2
    blue = 3

class Foo(object):
    """ Doc for Foo class """
    class FooChild:
        class FooGrandChild:
            pass

    _foo = 'foo property'
    def method1(self):
        """ doc for method1 """
        pass

    @property
    def foo(self):
        return self._foo

class Bar(Foo):
    pass

def hello(name):
    print('Hello,', name)

person = 'Hai'
hello(person)
