import types


class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model


def print_info(self):
    print("Make: ", self.make)
    print("Model:", self.model)


mycar = Car("Ford", "Escape")
mycar.info = types.MethodType(print_info, mycar)
mycar.info()
