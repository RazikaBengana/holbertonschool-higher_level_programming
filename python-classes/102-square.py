#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        # Constructor for the Square class with an optional size parameter
        # If no size is given, it defaults to 0

        self.__size = size  # Initialize a private variable __size with the given size

    @property
    def size(self):
        # Property decorator to make the size attribute "readable"
        # This allows for getting the size of the square without directly accessing the private variable

        return self.__size  # Return the value of the private __size attribute

    @size.setter
    def size(self, value):
        # Setter for the size property to allow setting the size of the square
        # This method also validates the input before setting the size

        if type(value) is not int:
            raise TypeError('size must be an integer')  # Ensure the size is an integer

        elif value < 0:
            raise ValueError('size must be >= 0')  # Ensure the size is non-negative

        else:
            self.__size = value  # Set the size if the input is valid

    def area(self):
        # Method to calculate the area of the square
        return self.__size ** 2

    # Magic methods to support comparison operations between Square instances based on their sizes
    def __eq__(self, other):
        # Check equality
        return self.size == other.size

    def __ne__(self, other):
        # Check inequality
        return self.size != other.size

    def __gt__(self, other):
        # Check greater than
        return self.size > other.size

    def __lt__(self, other):
        # Check less than
        return self.size < other.size

    def __ge__(self, other):
        # Check greater than or equal to
        return self.size >= other.size

    def __le__(self, other):
        # Check less than or equal to
        return self.size <= other.size
