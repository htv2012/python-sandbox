import collections

def str2numeric(string_value):
    converters = [
        dict(should_convert=lambda x: True, func=int),
        dict(should_convert=lambda x: True, func=float),
        dict(should_convert=lambda x: x.lower().startswith('0x'),
            func=lambda x: int(x[2:], 16)),
        dict(should_convert=lambda x: x.lower().startswith('0o'),
            func=lambda x: int(x[2:], 8)),
        dict(should_convert=lambda x: x.startswith('$'),
            func=lambda x: float(x[1:])),
        ]

    for converter in converters:
        if converter['should_convert'](string_value):
            try:
                return converter['func'](string_value)
            except ValueError:
                pass
    return string_value


def _numeric_list(row):
    """ Attempt to turn strings into numeric values for a list"""

    return [str2numeric(cell) for cell in row]

def _numeric_dict(dict_object):
    """ Attempt to turn strings into numeric values for a dict """
    return {k:str2numeric(v) for k, v in dict_object.items()}

def row2numeric(obj):
    """ Given a string, list, or dictionary, convert the elements to
    numeric values
    """
    if isinstance(obj, collections.Sequence):
        return _numeric_list(obj)
    elif isinstance(obj, collections.Mapping):
        return _numeric_dict(obj)

if __name__ == '__main__':
    print(row2numeric('25 0x20 3.2 John'.split()))
    print(row2numeric(dict(age='25', hex='0x20', gpa='3.2', name='John')))
