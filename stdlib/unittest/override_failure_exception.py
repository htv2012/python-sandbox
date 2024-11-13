    from __future__ import print_function
    import logging
    import unittest


    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


    class MyTest(unittest.TestCase):
        class failureException(AssertionError):
            def __init__(self, message):
                logger.error('Message: %r', message)  # Display
                self.message = message
                if isinstance(message, dict):
                    self.test_name = message['test_name']      # e.g. __main__.MyTest.test1
                    self.message = message['message']

                # Call your API here

            def __str__(self):
                return 'AssertionError: {}'.format(self.message)


        def test1(self):
            x = True
            self.assertFalse(
                x,
                {
                    'message': 'x should not be True',
                    'test_name': self.id(),
                }
            )


    if __name__ == '__main__':
        unittest.main()
