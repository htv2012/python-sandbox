#!/usr/bin/env python

import greeting


def main():
    """ Entry """
    greeting.hello('Johnny')
    g = greeting.Greeting('Amanda')
    g.greet()

    g2 = greeting.Greeting('Kaleb')
    g2.greet()
    g2.greet()
    g2.greet()

if __name__ == '__main__':
    main()
