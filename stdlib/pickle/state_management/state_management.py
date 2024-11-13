#!/usr/bin/env python
"""
This module provide a class decorator which adds `__getstate__()` and
`__setstate__()` to a class
"""


def state(attributes):
    """
    A class decorator which adds `__getstate__()` and `__setstate__()` to a class. These get/set methods only operate on those instant attributes lists in the `attributes` parameter.
    For example:

        @state(['uid', 'alias', 'shell'])
        class MyClass:
            ...

    The get/set methods will operate only on `self.uid`, `self.alias`, and `self.shell` as specified in the decorator.

    :param attributes: A list of attributes to get/set
    """
    def patch_class(cls):
        def getstate(self):
            """
            Returns a dictionary representing the state of this object
            """
            return dict((key, getattr(self, key)) for key in attributes)

        def setstate(self, state_dict):
            """
            Updates the state of this object based on the dictionary `state_dict`.

            :param state_dict: The dictionary representing the new state
            """
            sentinel = object()
            for key in attributes:
                new_value = state_dict.get(key, sentinel)
                if new_value is not sentinel:
                    setattr(self, key, new_value)
        
        cls.__getstate__ = getstate
        cls.__setstate__ = setstate

        return cls
    return patch_class

