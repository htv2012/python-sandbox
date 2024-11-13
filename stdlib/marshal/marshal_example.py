#!/usr/bin/python

# marshal_example.py
# by Hai Vu (C) 2008
# Demo of writing and reading binary data from/to file using the marshal
# module


import marshal

if __name__ == '__main__':
    # Store
    with open('marshal_example.dat', 'wb') as outfile:
        marshal.dump(dict(name='hai', age=39), outfile)
        marshal.dump('one two three'.split(), outfile)
        marshal.dump('hello, world', outfile)
        marshal.dump(1985.75, outfile)

    # Load
    with open('marshal_example.dat', 'rb') as infile:
        print('Dictionary:', marshal.load(infile))
        print('List:      ', marshal.load(infile))
        print('String:    ', marshal.load(infile))
        print('Float:     ', marshal.load(infile))
