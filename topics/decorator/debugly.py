""" Add debugging information to a function call """


from functools import wraps


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        argslist = ['{!r}'.format(arg) for arg in args]
        kwargslist = ['{}={!r}'.format(k, v) for k, v in list(kwargs.items())]
        arguments = ', '.join(argslist + kwargslist)
        print('{}({})'.format(func.__name__, arguments))
        return func(*args, **kwargs)
    return wrapper
