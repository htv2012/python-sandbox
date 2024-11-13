import warnings


class Dog(object):
    def __init__(self, name):
        warnings.warn("Deprecated, please use Canine class")
        self.name = name

    def bark(self):
        print("{}: woof".format(self.name))

    def destroy(self, thing):
        print("{}: destroy {}".format(self.name, thing))


if __name__ == "__main__":
    print("Hello")
    dog = Dog("Buster")
    dog.bark()
    dog.destroy("Tracy's favorite shoes")
    print("Goodbye")
