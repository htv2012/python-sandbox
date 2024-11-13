#!/usr/bin/env python
"""

Demo: How to pickle a class

a class should implement `__getstate__` and `__getstate__` to support
the pickle protocol.

"""
import io
import pickle
import tempfile


class User:
    """ A class to demonstrate pickling """
    def __init__(self, uid, alias, shell):
        """ Create new instance """
        self.uid = uid
        self.alias = alias
        self.shell = shell

    def __getstate__(self):
        """ Return the state for pickling """
        return self.__dict__

    def __setstate__(self, state):
        """ Set the state, called by pickle.load """
        self.__dict__.update(state)

    def __repr__(self):
        return f'User({self.uid}, {self.alias}, {self.shell})'


def show_user(user, label):
    print(f'## {label}')
    print(f'   {user}')
    print()


def main():
    """ Entry """

    #
    # Pickling to/from a file
    #
    print('# Pickle to and from a file\n')
    original_user = User(501, 'haiv', 'bash')
    show_user(original_user, 'Pickling this user')

    with tempfile.TemporaryFile() as file_handle:
        pickle.dump(original_user, file_handle)

        file_handle.seek(0)
        new_user = pickle.load(file_handle)
        show_user(new_user, 'Unpickling')

    #
    # Pickling to/from a byte stream
    #
    print('# Pickle to and from a byte stream\n')

    original_user = User(502, 'karen', 'tcsh')
    show_user(original_user, 'Pickling this user')

    byte_stream = io.BytesIO()
    pickle.dump(original_user, byte_stream)

    byte_stream.seek(0)
    new_user = pickle.load(byte_stream)
    show_user(new_user, 'Unpickling')



if __name__ == '__main__':
    main()
