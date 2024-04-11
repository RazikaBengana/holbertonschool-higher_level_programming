#!/usr/bin/python3
"""Unit tests for the Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define test cases for the Base class"""

    def test_constantId(self):
        """Test for explicitly setting a constant id"""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_autoId(self):
        """Test for automatic id assignment"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_string(self):
        """Test for setting a string as an id"""
        b = Base("string")
        self.assertEqual(b.id, "string")

    def test_to_json_string(self):
        """Test for converting dictionaries to a JSON string"""
        dic = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_dic = Base.to_json_string([dic])

        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(json_dic, str))
        self.assertCountEqual(
            json_dic, '{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}')
        json_d_1 = Base.to_json_string(None)

        self.assertEqual(json_d_1, "[]")

        err = ("to_json_string() missing 1 required positional argument: " +
               "'list_dictionaries'")

        with self.assertRaises(TypeError) as i:
            Base.to_json_string()

        self.assertEqual(err, str(i.exception))
        err = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as i:
            Base.to_json_string([{1, 2}], [{3, 4}])

        self.assertEqual(err, str(i.exception))

    def test_from_json_string(self):
        """Test for converting a JSON string to dictionaries"""
        string = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'
        json_str = Base.from_json_string(string)

        self.assertTrue(isinstance(string, str))
        self.assertTrue(isinstance(json_str, list))
        self.assertCountEqual(
            json_str, [{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}])

        json_s_1 = Base.from_json_string(None)

        self.assertEqual(json_s_1, [])

        err = ("from_json_string() missing 1 required positional argument: " +
               "'json_string'")

        with self.assertRaises(TypeError) as i:
            Base.from_json_string()

        self.assertEqual(err, str(i.exception))
        err = "from_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as i:
            Base.from_json_string('[1]', '[2]')

        self.assertEqual(err, str(i.exception))


if __name__ == "__main__":
    unittest.main()
