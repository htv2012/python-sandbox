"""Wrap the curl command"""


def options(*args, **kwargs):
    opt = list(args)
    opt.extend(f"--{key.replace('_', '-')}={value}" for key, value in kwargs.items())
    return opt
