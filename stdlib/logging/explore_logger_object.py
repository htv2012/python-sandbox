if __name__ == '__main__':
    import logging
    from create_logger import create_logger
    import unittest
    logger = create_logger('explore_logger_object', logging.DEBUG)


class MyTest(unittest.TestCase):
    def test1(self):
        logger.info("Caller: %s", logger.findCaller())

    def test_show_logger_internals(self):
        for member_name in dir(logger):
            member = getattr(logger, member_name)
            message = '- ' + member_name
            if callable(member):
                message += '()'
            docstring = getattr(member, '__doc__')
            if docstring is not None:
                message += docstring.splitlines()[0]

            logger.info(message)

if __name__ == '__main__':
    unittest.main(verbosity=2)
