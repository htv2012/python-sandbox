#!/usr/bin/env python
def str2bool(value):
    """ Converts the string `value` to boolean.

    :param value: A string, only 2 values are accepted: 'True' and 'False'
    :return: A boolean
    :raise KeyError: for other values of value
    """
    try:
        valid = {'True': True, 'False': False}
        return valid[value]
    except KeyError:
        raise ValueError(f'{value!r} is not a valid bool value')


if __name__ == '__main__':
    import unittest


    class Str2BoolTests(unittest.TestCase):
        def test_true(self):
            self.assertEqual(True, str2bool('True'))

        def test_false(self):
            self.assertEqual(False, str2bool('False'))

        def test_invalid_value(self):
            self.assertRaises(ValueError, str2bool, 'true')

    unittest.main()
