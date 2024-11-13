from collections import Mapping, namedtuple
import imp

def load_module_or_package(module_or_package):
    """
    Given a module name or package name, import that module or
    package. This function simulates the `import module` Python
    statement.

    :param module_or_package: The name of the module or package
    :return: The module object
    """
    # Return value from imp.find_module
    ModuleInfo = namedtuple('ModuleInfo', ['file', 'path', 'description'])

    search_path = None
    for package in module_or_package.split('.'):
        module_info = ModuleInfo(*imp.find_module(package, search_path))
        module = imp.load_module(package, *module_info)
        if module_info.description == ('', '', imp.PKG_DIRECTORY):
            search_path = module.__path__
    return module


def load_from(import_line):
    """
    Simulates `from X import a, b, c`

    :param import_line: The `from X import a, b, c`
    :return: A list of symbols
    """
    from_token, module_name, import_token, symbols = import_line.split(' ', 3)
    symbol_names = [token.strip() for token in symbols.split(',')]

    if not (from_token == 'from' and import_token == 'import'):
        raise ValueError('Invalid import line: {}'.format(import_line))

    mod = load_module_or_package(module_name)
    symbols = {s: getattr(mod, s) for s in symbol_names}
    return symbols


def factory(type_name, **attrs):
    import_line = 'from {0} import {0}'.format(type_name)
    symbols = load_from(import_line)
    obj = symbols[type_name](**attrs)
    return obj


if __name__ == '__main__':


    specs = [
        ('Foo', dict(a=1, b=2, c=3)),
        ('Bar', dict(x=10, y=20, z=30)),
    ]

    for type_name, attrs in specs:
        print(factory(type_name, **attrs))
