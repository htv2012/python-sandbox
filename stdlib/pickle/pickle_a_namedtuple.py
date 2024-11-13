#!/usr/bin/env python
"""
whatis: How to pickle and unpickle a namedtuple
"""
import collections
import io
import pickle


def show_user(user, label):
    print(f'## {label}')
    print(f'   {user}')
    print()


def main():
    """ Entry """
    User = collections.namedtuple('User', 'uid alias')

    user1 = User(501, 'john')
    show_user(user1, 'Pickling this user')

    byte_io = io.BytesIO()

    # Pickle will not work for namedtuple, so we need to convert it into
    # a tuple before pickling
    pickle.dump(tuple(user1), byte_io)

    # Likewise, unpickling will return a tuple, we need to convert it
    # back to a named tuple
    byte_io.seek(0)
    user2 = pickle.load(byte_io)
    user2 = User(*user2)
    show_user(user2, 'Unpickling')


if __name__ == '__main__':
    main()

