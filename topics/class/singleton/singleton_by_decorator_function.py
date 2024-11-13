"""
Attempt to create a singleton by decorator function

Pros:
- Simple, just tag the @singleton to the top

Cons:
- Cannot create subclass
"""


def singleton(cls):
    instances = {}

    def create_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return create_instance


@singleton
class Bar(object):
    pass


bar1 = Bar()
bar2 = Bar()
print(f"bar1: {bar1}")
print(f"bar2: {bar2}")
print(f"Are they the same? {bar1 is bar2}")
