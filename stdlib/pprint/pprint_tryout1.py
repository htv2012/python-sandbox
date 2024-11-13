

#!/usr/bin/env python

import pprint

class Car(object):
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def __repr__(self):
        return '<Car {} {} {}>'.format(self.year, self.make, self.model)
    def __str__(self):
        return '{} {} {}'.format(self.year, self.make, self.model)

cars = [
        Car(2000, 'Mercedes', 'E430'),
        Car(2002, 'Mercedes', 'ML320')
]

pprint.pprint(cars, indent=4)
