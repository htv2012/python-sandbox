#!/usr/bin/env python

""" Why return a mutable attribute might be dangerous """


class Car(object):
    def __init__(self, owners):
        self._owners = owners

    def get_owners(self):
        """Return a list of owners. Getter/setters are evil, but that
        is the story for another day.
        This is dangerous since someone could modify that list
        """
        return self._owners


if __name__ == "__main__":
    car = Car(["John", "Cindy"])
    print("This car belongs to", car.get_owners())  # John, Cindy

    owners = car.get_owners()
    owners.append("Jim")  # Danger!
    print("This car belongs to", car.get_owners())  # John, Cindy, Jim
