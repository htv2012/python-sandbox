import unittest
from collections import Mapping


def key_path_join(path, key):
    # return '{}.{}'.format(path, key).lstrip('.')
    if path != "":
        return "{}.{}".format(path, key)
    return key


def compare_dicts(d1, d2, path=""):
    all_keys = set(d1.keys()).union(list(d2.keys()))
    for k in all_keys:
        if k not in d2:
            yield "missing", key_path_join(path, k)
        elif k not in d1:
            yield "extra", key_path_join(path, k)
        elif isinstance(d1[k], Mapping) and isinstance(d2[k], Mapping):
            for t in compare_dicts(d1[k], d2[k], key_path_join(path, k)):
                yield t
        elif d1[k] != d2[k]:
            yield "diff", key_path_join(path, k), d1[k], d2[k]


class CompareDictsTests(unittest.TestCase):
    longMessage = True

    def test_flat_missing(self):
        d1 = dict(a=1, b=2, c=3)
        d2 = dict(c=3)

        expected = set([("missing", "a"), ("missing", "b")])
        actual = set(compare_dicts(d1, d2))
        self.assertEqual(expected, actual)

    def test_flat_extra(self):
        d1 = dict(a=1, b=2, c=3)
        d2 = dict(c=3)

        expected = set([("extra", "a"), ("extra", "b")])
        actual = set(compare_dicts(d2, d1))
        self.assertEqual(expected, actual)

    def test_flat_values_differ(self):
        d1 = dict(a=1, b=2, c=3)
        d2 = dict(a=1, b=20, c=30)

        expected = set([("diff", "b", 2, 20), ("diff", "c", 3, 30)])
        actual = set(compare_dicts(d1, d2))
        self.assertEqual(expected, actual)

    def test_flat_dict_and_non_dict_values(self):
        d1 = dict(a=1, b=2)
        d2 = dict(a=1, b=dict(b1=20))

        expected = list([("diff", "b", 2, {"b1": 20})])
        actual = list(compare_dicts(d1, d2))
        self.assertEqual(expected, actual)

    def test_nested_missing(self):
        d1 = dict(a=1, b=dict(b1=20, b2=21))
        d2 = dict(a=1, b=dict(b1=20, b2=221))

        expected = set([("diff", "b.b2", 21, 221)])
        actual = set(compare_dicts(d1, d2))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
