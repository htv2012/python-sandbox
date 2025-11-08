def exec_catch(func, *args, **kwargs):
    """Execute a function, return the result, exception."""
    try:
        return func(*args, **kwargs), None
    except Exception as err:
        return None, err
