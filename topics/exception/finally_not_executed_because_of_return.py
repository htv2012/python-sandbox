"""
See if finally reached
"""

def half_of(value):
    try:
        result = value / 2
    except TypeError as e:
        print('ERROR:', e)
        return 'Error'
    finally:
        print('Reached finally clause')

    return result


print(half_of('foo'))
