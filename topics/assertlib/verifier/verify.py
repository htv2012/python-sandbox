import functools
import operator


class verify:
    verifiers = {}

    def __init__(self, actual, message=None):
        self.actual = actual
        self.message = message

    @classmethod
    def register(cls, method, name=None):
        name = name or method.__name__
        cls.verifiers[name] = method

    def __getattr__(self, name):
        method = self.verifiers[name]
        partial = functools.partial(method, self.actual, message=self.message)
        return partial

    def _compare(self, compare, expected):
        symbols = {
            operator.eq: "==",
            operator.ge: ">=",
            operator.gt: ">",
            operator.le: "<=",
            operator.lt: "<",
            operator.ne: "!=",
        }

        result = compare(self.actual, expected)
        message = self.message or ""
        message = (
            f"{message}"
            f"Verify actual:{self.actual!r} "
            f"{symbols[compare]} "
            f"expected:{expected!r} => {result}"
        )
        if result:
            print(message)
        else:
            raise AssertionError(message)

    eq = functools.partialmethod(_compare, operator.eq)
    ge = functools.partialmethod(_compare, operator.ge)
    gt = functools.partialmethod(_compare, operator.gt)
    le = functools.partialmethod(_compare, operator.le)
    lt = functools.partialmethod(_compare, operator.lt)
    ne = functools.partialmethod(_compare, operator.ne)


def in_(actual, container, message=None):
    result = actual in container
    message = message or ""
    message = f"{message} Verify {actual!r} in {container} => {result}"
    message = message.strip()
    if actual in container:
        print(message)
    else:
        raise AssertionError(message)


verify.register(in_)

class msg:
    def __init__(self, message):
        self.message = message

    def verify(self, actual):
        return verify(actual, message=self.message)
