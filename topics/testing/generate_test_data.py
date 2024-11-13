#!/usr/bin/env python
# whatis: dynamically generate all test cases

from collections import namedtuple
from itertools import product


def generate_test_data(**items):
    TestData = namedtuple('TestData', items)
    return map(TestData._make, product(*items.values()))

test_data = generate_test_data(
    sheet_type=('Worksheet', 'Dashboard', 'Storyboard'),
    data_source=('relational', 'cube'),
    publish=(False, True))

for td in test_data:
    print(td)
