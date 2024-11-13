class SingleDispatch(object):
    def __call__(self, obj, *args, **kwargs):
        func = self.dispatch.get(type(obj), self.default_dispatch)
        return func(obj, *args, **kwargs)

    def register(self, type_, func):
        self.dispatch[type_] = func

    def default_dispatch(self, obj, *args, **kwargs):
        message = "Cannot handle type {}".format(type(obj).__name__)
        raise NotImplementedError(message)

    def __init__(self):
        self.dispatch = dict()


if __name__ == "__main__":
    dispatch = SingleDispatch()
    dispatch.register(int, lambda x: "Integer: {}".format(x))
    dispatch.register(list, lambda x: "List: {!r}".format(x))

    print(dispatch(5))
    print(dispatch([501, "haiv", "bash"]))
    # print dispatch('Hello')
