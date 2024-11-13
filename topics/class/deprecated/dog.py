import deprecated


@deprecated.deprecated_class
class Dog(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("{}: woof".format(self.name))

    def destroy(self, thing):
        print("{}: destroy {}".format(self.name, thing))


if __name__ == "__main__":
    dog = Dog("Fido")
    dog.bark()
    dog.destroy("Lisa's favorite shoes")
