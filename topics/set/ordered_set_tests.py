import unittest
from ordered_set import OrderedSet


class OrderedSetTests(unittest.TestCase):
    def setUp(self):
        super(OrderedSetTests, self).setUp()
        self.ordered_set = OrderedSet()

    def test_create_empty(self):
        self.assertEqual(0, len(self.ordered_set))

    def test_create_from_list(self):
        self.ordered_set = OrderedSet(['a', 'b', 'c'])
        self.assertEqual(3, len(self.ordered_set))
        self.assertIn('a', self.ordered_set)
        self.assertIn('b', self.ordered_set)
        self.assertIn('c', self.ordered_set)
        self.assertNotIn('d', self.ordered_set)
        self.assertEqual(['a', 'b', 'c'], list(self.ordered_set))

    def test_create_from_dict(self):
        """ Create a new OrderedSet from a dictionary """
        self.ordered_set = OrderedSet(dict(a=10, b=20, c=30))
        self.assertEqual(3, len(self.ordered_set))
        self.assertIn('a', self.ordered_set)
        self.assertIn('b', self.ordered_set)
        self.assertIn('c', self.ordered_set)
        self.assertNotIn('d', self.ordered_set)
        self.assertEqual({'a', 'b', 'c'}, set(self.ordered_set))

    def test_add(self):
        """ Add items to an OrderedSet """
        self.ordered_set.add('a')
        self.assertEqual(['a'], list(self.ordered_set))

        self.ordered_set.add('b')
        self.assertEqual(['a', 'b'], list(self.ordered_set))

if __name__ == '__main__':
    unittest.main()
