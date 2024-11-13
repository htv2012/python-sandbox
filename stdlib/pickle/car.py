# Class to try pickling
class Car(object):
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __repr__(self):
        return 'Car(year={!r}, make={!r}, model={!r})'.format(self.year, self.make, self.model)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
