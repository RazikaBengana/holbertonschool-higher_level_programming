#!/usr/bin/python3
"""Unit tests for the Square class"""

import unittest
from unittest import mock
import io
import os
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Define test cases for the Square class"""

    def test_instance(self):
        """Test Square instance creation and attribute validation"""
        s = Square(5)

        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

        with self.assertRaises(TypeError):
            Square(5, "1")

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(ValueError):
            Square(-5, 3, 4)

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

    def test_dictionary(self):
        """Test converting Square instances to dictionaries"""
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_case_normal(self):
        """Test normal case behavior of Square properties"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_load_from_file(self):
        """Test loading Square instances from a file"""
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile('Square.json'))

        load_file = Square.load_from_file()
        self.assertEqual(len(load_file), 0)

    def test_area(self):
        """Test the area calculation of a Square"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s = Square(1, 2)
        self.assertEqual(s.area(), 1)

    def test_display(self):
        """Test the STDOUT display of a Square's representation"""
        s = Square(5)

        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "#####\n#####\n#####\n#####\n#####\n"

        s = Square(1, 2)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "  #\n"

    def test_string(self):
        """Test the string representation of a Square"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), '[Square] (4) 2/3 - 1')

    def test_update(self):
        """Test updating Square attributes"""
        s1 = Square(2)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(size=1, id=89, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 2)

    def test_created(self):
        """Test creating a Square from a dictionary"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file(self):
        """Test saving Square instances to a file"""
        Square.save_to_file([Square(1)])

        with open("Square.json", mode="r") as read_file:
            s = read_file.read()
            self.assertEqual(len(s), 39)

    def test_save_to_file_list_empty(self):
        """Test saving an empty list of Squares to a file"""
        Square.save_to_file([])

        with open("Square.json", mode="r") as read_file:
            s = read_file.read()
            self.assertEqual(s, "[]")

    def test_save_to_file_empty(self):
        """Test saving None (no Squares) to a file"""
        Square.save_to_file(None)

        with open("Square.json", mode="r") as read_file:
            s = read_file.read()
            self.assertEqual(len(s), 2)
        os.remove("Square.json")

    def test_save_to_file_none(self):
        """Test error raised when save_to_file is called without arguments"""
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_r(self):
        """Test saving Rectangle instances to the Square.json file by mistake"""
        Rectangle.save_to_file([Rectangle(1, 2)])

        with open("Square.json", mode="r") as read_file:
            s = read_file.read()
            self.assertEqual(len(s), 2)
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
