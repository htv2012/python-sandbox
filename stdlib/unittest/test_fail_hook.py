"""
Problem: I have some extra works to do when a test failed (like taking
    screenshot, or save off artifacts). How do I hook this into the
    unittest ecosystem?

Reference:
http://www.anggrianto.com/blog/extending-unittest-for-taking-screenshot-on-failure/
"""
import unittest


class TestWithHook(unittest.TestCase):
    @property
    def failureException(self):
        class MyFailure(AssertionError):
            def __init__(self, *args, **kwargs):
                print '==== EXTRA WORK HERE ==='
                super(MyFailure, self).__init__(*args, **kwargs)
        MyFailure.__name__ = AssertionError.__name__
        return MyFailure


class MyTest(TestWithHook):
    def test1(self):
        self.assertEqual(2 + 2, 5)


if __name__ == '__main__':
    unittest.main()