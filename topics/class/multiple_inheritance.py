class X(object):
    pass


class Y(object):
    pass


class Z(object):
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print("Method Resolution Order for M:")
for i in M.mro():
    print(i)
