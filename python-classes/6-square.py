#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """
    Square class

    Attributes:
        __size (int): the size of a side of the square --> private attribute
        __position (tuple): the position of the square as coordinates (x, y) --> private attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor method for Square class;
        Initialize a new Square instance

        Args:
            size (int): the size of a side of the square, defaults to 0
            position (tuple): the position of the square, defaults to (0, 0)

        Raises:
            TypeError: if `size` is not an integer or `position` is not a tuple of 2 positive integers
            ValueError: if `size` is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

        if type(position) is not tuple or len(position) != 2 \
                or type(position[0]) is not int or position[0] < 0 \
                or type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = position

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

    @property
    def position(self):
        """tuple: Property for the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position property;
        Set position of the square

        Args:
            value (tuple): the position of the square

        Raises:
            TypeError: if `value` is not a tuple of 2 positive integers
        """

        if type(value) is not tuple or len(value) != 2 \
                or type(value[0]) is not int or value[0] < 0 \
                or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the '#' character;
        Print blank lines for the `position` before printing the square itself
        """
        if self.__size == 0:
            print()

        else:
            for line in range(self.__position[1]):
                print()

            for size1 in range(self.__size):
                for space1 in range(self.__position[0]):
                    print(" ", end="")

                for diez in range(self.__size):
                    print("#", end="")
                print()
