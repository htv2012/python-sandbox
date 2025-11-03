

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

    def __getattr__(self):
        return {
            'abcd': 1,
            'efgh': 2,
            'ijkl': 3,
        }

    _foo = 'foo property'
    def method1(self):
        """ doc for method1 """
        pass

    def method2(self, arg1, arg2=1, *args, **kwargs):
        """Doc for method2"""
        pass

    @property
    def foo(self):
        return self._foo

class Bar(Foo):
    def method1(self):
        pass

    @property
    def property1(self):
        pass

def hello(name):
    print('Hello,', name)

person = 'Hai'
hello(person)
