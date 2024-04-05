#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """
    Square class;
    This class defines a square with properties like size and methods to calculate its area
    """

    def __init__(self, size=0):
        """
        Constructor method for Square class;
        Initialize a new Square instance

        Args:
         size (int, optional): the size of a side of the square, defaults to 0
        """

        self.__size = size  # size = private instance attribute

    @property
    def size(self):
        """
        Property method to get the size of the square

        Returns:
            int: the current size of the square
        """
        return self.__size  # Return the value of the private instance attribute __size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property;
        Set the size of the square to a given value, with checks for type and value constraints

        Args:
            value (int): the new size of the square

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is negative
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # Set the size if all checks pass

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2  # Return the square of the size as the area
