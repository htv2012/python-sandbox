#!/usr/bin/env python

import random_with_seed2 as random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', type=str)
    options = parser.parse_args()
    if options.seed is not None:
        random.seed(options.seed)

    print('Seed was set to:', random.get_seed())
    mylist = [random.randint(0, 100) for _ in range(5)]
    print(mylist)
