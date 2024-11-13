class Const(object):
    __red = 'red'
    red = property(lambda cls: cls.__red)


Const.blue = property(lambda cls: 'blue')

const = Const()
print(const.red)
print(const.blue)

const.blue = 'yellow'


print('---')

class Foo(object):
    pass

foo = Foo()
foo.a = 3

print(foo.a)

Foo.b = property(lambda self: self.a + 1)
print(foo.b)
