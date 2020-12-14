import unittest
from getValue import findvalue


class TestgetValue(unittest.TestCase):

    def test_valid_pair_1(self):
        obj = {"x": {"y": {"z": "a"}}}
        key = "x/y/z"
        result = findvalue(obj, key)
        self.assertEqual(result, "a")

    def test_valid_pair_2(self):
        obj = {"x": {"y": {"z": "a"}}}
        key = "x/y/"
        result = findvalue(obj, key)
        self.assertEqual(result, {'z': 'a'})

    def test_invalid_pair_1(self):
        obj = {"x": {"y": {"z": "a"}}}
        key = "x/y/b"
        result = findvalue(obj, key)
        self.assertEqual(result, "Key value pair not found!!")

    def test_invalid_pair_2(self):
        obj = {"x": {"y": {"z": "a"}}}
        key = "x/y/z/a"
        result = findvalue(obj, key)
        self.assertEqual(result, "Key value pair not found!!")


if __name__ == '__main__':
    unittest.main()
