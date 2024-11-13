#!/usr/bin/env python

import pickle
import os

from car import Car


def show_data(label, per, seq, car):
    print('%s:' % label)
    print('  Person:', per)
    print('  Sequence:', seq)
    print('  Car:', car)
    print()


if __name__ == '__main__':
    # Create temp file in the same dir with this script
    script_dir = os.path.dirname(__file__)
    filename = os.path.join(script_dir, 'pickle_tryout.dat')

    # Prepare the data for pickling
    person1 = {'Name': 'John', 'Age': 31}
    sequence1 = 'one,two,three'.split(',')
    car1 = Car(1974, 'Mercury', 'Capri')
    show_data('Original data', person1, sequence1, car1)

    # Pickle them
    with open(filename, 'wb') as f:
        pickle.dump(person1, f)
        pickle.dump(sequence1, f)
        pickle.dump(car1, f)

    # Unpickle them
    with open(filename, 'rb') as f:
        person2 = pickle.load(f)
        sequence2 = pickle.load(f)
        car2 = pickle.load(f)
    show_data('Round-trip data', person2, sequence2, car2)

    # Test for equality
    assert person1 == person2
    assert sequence1 == sequence2
    assert car1 == car2

