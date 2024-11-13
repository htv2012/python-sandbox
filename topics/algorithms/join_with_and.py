#!/usr/bin/env python3
import unittest
import io


def special_join(iterable, separator, last_separator):
    buf = io.StringIO()
    count = 0
    for e in iterable:
        buf.write(e)
        pos = buf.tell()
        buf.write(separator)
        count += 1

    if count == 1:
        buf.seek(pos)
        buf.truncate()
    elif count > 1:
        # Back track and write the last separator
        pos = pos - len(e) - len(separator)
        buf.seek(pos)
        buf.write(last_separator)
        buf.write(e)
        buf.truncate()

    return buf.getvalue()


SEPARATOR = ", "
LAST_SEPARATOR = " and "


class TestSpecialJoin(unittest.TestCase):
    def test_zero_item(self):
        self.assertEqual("", special_join([], SEPARATOR, LAST_SEPARATOR))

    def test_single_item(self):
        self.assertEqual("John", special_join(["John"], SEPARATOR, LAST_SEPARATOR))

    def test_two_items(self):
        self.assertEqual(
            "Frankie and Johnny",
            special_join(["Frankie", "Johnny"], SEPARATOR, LAST_SEPARATOR),
        )

    def test_multiple_items(self):
        self.assertEqual(
            "Peter, Paul and Mary",
            special_join(["Peter", "Paul", "Mary"], SEPARATOR, LAST_SEPARATOR),
        )


if __name__ == "__main__":
    unittest.main()
