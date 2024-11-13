#!/usr/bin/env python3
import functools

def serializable(*attributes):
    """
    A decorator that works on classes which provides state management
    for objects via pickle. As an example, if a class needs persistence
    capability via pickle, we can decorate this class with a list of
    attributes to save and load:

        @serializable("title", "author")
        class Book:
            def __init__(self, title, author):
                self.title = title
                self.author = author

    In the above example, the title and author attributes will be
    persistence via pickle.

    :param attributes: A list of attribute names
    """
    def wrapper(cls):

        @functools.wraps(cls)
        def getstate(self):
            return {name: getattr(self, name, None) for name in attributes}

        @functools.wraps(cls)
        def setstate(self, state):
            for name in attributes:
                current_value = getattr(self, name, None)
                new_value = state.get(name, current_value)
                setattr(self, name, new_value)

        setattr(cls, "__getstate__", getstate)
        setattr(cls, "__setstate__", setstate)
        return cls

    return wrapper
