from contextlib import contextmanager

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('p'):
    print('Lorem ipsum dolor sit amet,')
    print('consectetur adipiscing elit.')
