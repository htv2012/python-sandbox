import logging
import unittest

from closable import do_not_close, mark_as_closed

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MyThing(object):
    @do_not_close
    def method1(self):
        logger.info("method1")

    def method2(self):
        logger.info("method2")

    @property
    def property1(self):
        return "property1"

    @property1.setter
    def property1(self, value):
        pass

    def close(self):
        logger.info("close")
        mark_as_closed(self)


class AfterClosedTest(unittest.TestCase):
    def setUp(self):
        self.mything = MyThing()
        self.mything.close()

    def test_do_not_close_method_is_still_accessible_after_close(self):
        self.mything.method1()

    def test_method_not_accessible(self):
        with self.assertRaises(RuntimeError):
            self.mything.method2()

    def test_property_is_still_accessible_after_closed(self):
        logger.info("Property: %s", self.mything.property1)
        self.mything.property1 = 5


if __name__ == "__main__":
    unittest.main()
