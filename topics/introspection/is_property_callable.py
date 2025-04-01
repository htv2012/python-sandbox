#!/usr/bin/env python
"""Is a property consider callable?"""


class Foo:
    """Is a property callable?"""

    moo_value = "moo value"

    @property
    def bar_property(self):
        return "bar value"

    def show_method(self):
        pass


if __name__ == "__main__":
    foo = Foo()
    for attribute_name in dir(foo):
        attribute_object = getattr(foo, attribute_name)
        print(
            "{}: {!r}, callable: {}".format(
                attribute_name, attribute_object, callable(attribute_object)
            )
        )
