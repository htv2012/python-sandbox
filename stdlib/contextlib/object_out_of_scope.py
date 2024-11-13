"""
Will the object that a context manager yield go out of scope after the
with block?
"""
import contextlib
from io import StringIO


@contextlib.contextmanager
def tag(name):
    buffer = StringIO()
    buffer.write('<{}>'.format(name))
    yield buffer
    buffer.write('</{}>'.format(name))

if __name__ == '__main__':
    with tag('strong') as element:
        element.write('foo')

    # Out of the with block, the object 'element' is still valid, not
    # out of scope
    print(element.getvalue())
