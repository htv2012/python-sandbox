"""
My sandbox to try out ideas
"""

import inspect
import unittest


def list_members(obj, show_private=False):
    func_list = []
    attr_list = []

    for member_name in dir(obj):
        if member_name.startswith('__'): continue
        if member_name.startswith('_') and not show_private: continue
        member = getattr(obj, member_name)
        if callable(member):
            func_list.append(member_name)
        else:
            attr_list.append(member_name)

    # Display the attributes first
    for member_name in sorted(attr_list):
        print '- {}'.format(member_name)

    # Display the functions
    for member_name in sorted():
        print '- {}()'.format(member_name)

class SandboxTest(unittest.TestCase):
    def test1(self):
        list_members(self, show_private=True)

    def test_get_test_name(self):
        """ Get name of the test """
        module_name, class_name, test_name = self.id().split('.')
        print 'Module:', module_name
        print 'Class:', class_name
        print 'Test:', test_name
        print 'Desc:', self.shortDescription()

class EqualityTest(unittest.TestCase):
    def test_almost_equal(self):
        expected = [2.5, 0.33]
        actual = [10.0 / 4, 1.0 / 3]
        self.assertAlmostEqual(expected, actual)

    def test_equal(self):
        expected = [2.5, 0.33]
        actual = [10.0 / 4, 1.0 / 3]
        self.assertEqual(expected, actual)

    def test_list_almost_equal(self):
        expected = [2.5, 0.33]
        actual = [10.0 / 4, 1.0 / 3]

        for e, a in zip(expected, actual):
            self.assertAlmostEqual(e, a, places=2)

if __name__ == '__main__':
    unittest.main()
