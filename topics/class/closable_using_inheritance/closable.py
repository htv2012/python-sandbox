#!/usr/bin/env python


def accessible_while_closed(func):
    """
    A decorator to mark a function as available, even after the object
    closed.
    """
    func.accessible_while_closed = True
    return func


class MarkAsClosed(object):
    def _invalid_action(self, *args, **kwargs):
        raise RuntimeError("object closed")

    def mark_as_closed(self):
        for name in dir(self):
            # Ignore private members
            if name.startswith("_"):
                continue
            member = getattr(self, name)
            # Ignore non-callable (i.e. data) members
            if not callable(member):
                continue
            # Ignore those callable members decorated with
            # accessible_while_closed
            if getattr(member, "accessible_while_closed", False):
                continue
            setattr(self, name, self._invalid_action)


class Foo(MarkAsClosed):
    def close(self):
        print("close")
        self.mark_as_closed()

    def method1(self):
        print("method1")

    @property
    def property1(self):
        return "property1"

    @accessible_while_closed
    def method2(self):
        print("method2")


if __name__ == "__main__":
    f = Foo()
    f.method1()
    f.close()
    f.method2()  # Should be OK
    try:
        print((f.property1))
        f.method1()  # Not OK
    except RuntimeError as e:
        print(e)
