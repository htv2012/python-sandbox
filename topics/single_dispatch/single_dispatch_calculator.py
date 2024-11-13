import operator


class Caculator(object):
    def __call__(self, op, *args, **kwargs):
        func = self.dispatch.get(op, self.default_dispatch)
        return func(*args, **kwargs)

    def register(self, op, func):
        self.dispatch[op] = func

    def default_dispatch(self, op, *args, **kwargs):
        raise NotImplementedError("Cannot handle op {}".format(op))

    def __init__(self):
        self.dispatch = dict()


if __name__ == "__main__":
    calculate = Caculator()
    calculate.register("+", operator.add)
    calculate.register("-", operator.sub)
    calculate.register("#", lambda x: " ".join(x))

    script = """# What is 2 + 5?\n + 2 5"""
    for line in script.splitlines():
        tokens = line.split()
        print(">>>", tokens, repr(line))
        op = tokens.pop(0)
        print(line)
        print(calculate(op, *tokens))
