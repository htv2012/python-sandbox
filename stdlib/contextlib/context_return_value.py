import contextlib

@contextlib.contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('p'):
    print('Hello, world')

t = tag('strong')
with t:
    print('I am excited')
