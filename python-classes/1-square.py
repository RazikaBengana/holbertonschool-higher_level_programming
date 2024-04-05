#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """
    Square class;
    This class is designed to create Square objects
    """

    def __init__(self, size):
        """
        Constructor method for Square class;
        Initialize a new Square instance

        Args:
            size (float|int): the size of the square's side --> it must be a number
        """

        self.__size = size  # size = private instance attribute
