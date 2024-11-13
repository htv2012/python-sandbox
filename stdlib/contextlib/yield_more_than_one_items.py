""" Cannot yield more than one items """
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    odd = list()
    even = list()
    yield odd, even
    print('odd:', odd)
    print('event:', even)
    print("</%s>" % name)
    yield odd

with tag("h1") as (o, e):
	o.append(5)
	e.append(6)

