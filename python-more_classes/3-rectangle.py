#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """A class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance

        Args:
            width (int, optional): the width of the rectangle, defaults to 0
            height (int, optional): the height of the rectangle, defaults to 0
        """
        self.width = width  # Set the width of the rectangle, using the width property setter
        self.height = height  # Set the height of the rectangle, using the height property setter

    @property
    def width(self):
        """
        int: gets or sets the width of the rectangle;
        The setter ensures the width is an integer and greater than or equal to 0
        """
        return self.__width  # Return the width of the rectangle, encapsulating the value

    @property
    def height(self):
        """
        int: gets or sets the height of the rectangle;
        The setter ensures the height is an integer and greater than or equal to 0
        """
        return self.__height  # Return the height of the rectangle, encapsulating the value

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Validate the width is an integer

        if value < 0:
            raise ValueError("width must be >= 0")  # Validate the width is not negative

        else:
            self.__width = value  # Set the width if validations pass

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Validate the height is an integer

        if value < 0:
            raise ValueError("height must be >= 0")  # Validate the height is not negative

        else:
            self.__height = value  # Set the height if validations pass

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle, or 0 if either side is 0
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Special method to return a string representation of the rectangle"""

        if self.__height == 0 or self.__width == 0:
            return ""  # Return an empty string if either width or height is 0

        rect = "\n".join(["#" * self.__width for _ in range(self.__height)])

        return rect  # Return a string that represents the rectangle using "#" characters
