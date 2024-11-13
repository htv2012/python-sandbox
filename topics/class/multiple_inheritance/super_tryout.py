class X(object):
    def __init(self, a, b):
        self.a = a
        self.b = b


class Y(object):
    def __init(self, c):
        self.c = c


class XY(X, Y):
    def __init__(self):
        s = "Super for XY:", super(XY, self)
        print(("Super is of type X:", isinstance(s, X)))
        print(("Super is of type Y:", isinstance(s, Y)))
        print(("MRO:", XY.mro()))
        super(XY, self).__init__(9)


xy = XY()
