#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """A class that represents a rectangle"""
    number_of_instances = 0  # Class variable to track the number of Rectangle instances
    print_symbol = "#"  # Class variable that defines the symbol used for representing the rectangle in a string form

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance

        Args:
            width (int, optional): the width of the rectangle, defaults to 0
            height (int, optional): the height of the rectangle, defaults to 0

        This method sets up the rectangle with width and height, and increments the number of instances
        """
        self.width = width  # Set the width of the rectangle, using the width property setter
        self.height = height  # Set the height of the rectangle, using the height property setter
        type(self).number_of_instances += 1  # Increment the class variable tracking the number of instances

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

        return rect[:-1]  # Return a string representation of the rectangle

    def __repr__(self):
        """
        Provide an 'official' string representation of the Rectangle which can be used
        to recreate a new instance with the same size
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Special method called when an instance is about to be destroyed"""
        type(self).number_of_instances -= 1  # Decrement the class variable tracking the number of instances
        print("Bye rectangle...")  # Print a message indicating the Rectangle instance is being deleted

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determine the bigger or equal rectangle by area

        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle

        Returns:
            Rectangle: the rectangle with the bigger or equal area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")  # Ensure rect_1 is a Rectangle

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")  # Ensure rect_2 is a Rectangle

        if rect_1.area() >= rect_2.area():
            return rect_1  # Return rect_1 if its area is bigger or equal to rect_2's

        else:
            return rect_2  # Otherwise, return rect_2
