#usr/bin/python3
"""Unittest for max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_integer(self):
        """Test with a list of integer: it should return the max"""
        l = [1, 2, 3, 5, 7]
        result = max_integer(l)
        self.assertEqual(result, 7)

    def test_empty(self):
        """Test with an empty list: it should return None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_none(self):
        """Test with None: it should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    def test_not_int(self):
        """Test with a list of non-ints and ints: it should raise a TypeError exception"""
        l = ["c", "z", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_float(self):
        """Test with a list of ints and floats: it should return the max"""
        l = [2, 3.5, 1]
        result = max_integer(l)
        self.assertEqual(result, 3.5)

    def test_negative(self):
        """Test with a list of negative values: it should return the max"""
        l = [-3, -7, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_unique(self):
        """Test with one int in list: it should return the value of this int"""
        l = [76]
        result = max_integer(l)
        self.assertEqual(result, 76)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        l = [5, 5, 5, 5, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value: it should return this max"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)


    if __name__ == '__main__':
        unittest.main()
