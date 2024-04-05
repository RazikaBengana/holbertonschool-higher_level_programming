#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """
    Square class;
    This class is designed to create Square objects
    """

    def __init__(self, size=0):
        """
        Constructor method for Square class;
        Initialize a new Square instance

        Args:
            size (int, optional): the size of one side of the square, defaults to 0;
                                  size must be an integer and non-negative

        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is negative
        """

        self.__size = size  # size = private instance attribute

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
