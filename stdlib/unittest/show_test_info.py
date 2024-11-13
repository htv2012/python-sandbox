from __future__ import print_function
import unittest
import importlib

def main():
    module_name = 'compare_objects'
    module = importlib.import_module(module_name)
    test_loader = unittest.TestLoader()

    test_cases = []
    print(dir(module))
    for object_name in dir(module):
        object_ = getattr(module, object_name)
        # print(object_)
        if isinstance(object_, unittest.TestCase):
            test_cases.append(object_)

    print(module_name)
    print(test_cases)

if __name__ == '__main__':
    main()