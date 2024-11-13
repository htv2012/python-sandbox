#!/usr/bin/env python
"""
Demonstrate the use of a decorator to provide `__getstate__` and
`__setstate__` functionality
"""
import state_management


@state_management.state(['uid', 'alias', 'shell'])
class User:
    def __init__(self, uid, alias, shell):
        self.uid = uid
        self.alias = alias
        self.shell = shell

    def __repr__(self):
        return 'User({0.uid}, {0.alias}, {0.shell})'.format(self)


if __name__ == '__main__':
    user = User(501, 'haiv', 'bash')
    print(user)
    print(user.__getstate__())
    
    user.__setstate__({'shell': 'zsh'})
    print(user)

