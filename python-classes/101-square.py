#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""

    def __str__(self):
        # Method to return the string representation of the square
        # It removes the last newline character from the string representation
        return self.generate_square_visual_representation()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        # Initialize the Square instance with optional size (default 0) and position (default (0,0))

        self.size = size  # Call the size setter
        self.position = position  # Call the position setter

    @property
    def size(self):
        # Property getter for the size
        return self.__size

    @size.setter
    def size(self, value):
        # Property setter for the size
        # Validates that the size is an integer and greater than or equal to 0

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        # Property getter for the position
        return self.__position

    @position.setter
    def position(self, value):
        # Property setter for the position
        # Validates that the position is a tuple of 2 positive integers

        if not isinstance(value, tuple) or len(value) != 2 or \
                len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        # Return the area of the square
        return self.__size ** 2

    def generate_square_visual_representation(self):
        # Return the string representation of the square for printing
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
            ret += "\n"

        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "

            for j in range(self.size):
                ret += "#"
            ret += "\n"

        return ret

    def my_print(self):
        # Print the square to stdout
        print(self.generate_square_visual_representation(), end="")
