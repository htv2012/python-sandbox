import logging

logging.basicConfig(level=logging.DEBUG)


def __getattr__(name):
    return getattr(logging, name)
    
