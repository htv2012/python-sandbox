import unittest

from jsontools import JsonObject


class JsonObjectTest(unittest.TestCase):
    def setUp(self):
        self.raw_dict = {"a": 1, "b": {"c": 2, "d": 3}}
        self.raw_list = ["abc", "def"]
        self.dict_object = JsonObject(self.raw_dict)
        self.list_object = JsonObject(self.raw_list)

    def test_create(self):
        """Creates with different raw sources"""
        JsonObject({})
        JsonObject([])

        with self.assertRaises(ValueError):
            JsonObject(2)

        with self.assertRaises(ValueError):
            JsonObject("foo")

    def test_getattr(self):
        """Tests __getattr__"""
        self.assertEqual(1, self.dict_object.a)
        self.assertEqual(2, self.dict_object.b.c)
        self.assertEqual(3, self.dict_object.b.d)

    def test_getitem(self):
        """Tests __getitem__"""
        self.assertEqual("abc", self.list_object[0])
        self.assertEqual("def", self.list_object[1])
        with self.assertRaises(IndexError):
            self.list_object[3]

    def test_iter_dict(self):
        """Tests the iter feature over a dict"""
        actual = list(self.dict_object)
        expected = ["a", "b"]
        self.assertEqual(expected, actual)

    def test_iter_list(self):
        """Tests the iter feature over a list"""
        actual = list(self.list_object)
        expected = ["abc", "def"]
        self.assertEqual(expected, actual)

    def test_len_dict(self):
        """Tests the length of a dict"""
        self.assertEqual(2, len(self.dict_object))

    def test_len_list(self):
        """Tests the length of a list"""
        self.assertEqual(2, len(self.list_object))

    def test_repr_dict(self):
        """Tests the repr of a dict"""
        self.assertEqual(repr(self.raw_dict), repr(self.dict_object))

    def test_repr_list(self):
        """Tests the repr of a list"""
        self.assertEqual(repr(self.raw_list), repr(self.list_object))


if __name__ == "__main__":
    unittest.main()
