#!/usr/bin/python3
"""
Define the class Rectangle that inherits from Base;
This class represents a rectangle and inherits from the Base class;
It includes properties for width, height, x, and y coordinates, and the rectangle's id
"""


from models.base import Base


class Rectangle(Base):
    """A class that defines a rectangle, inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): The x coordinate of the rectangle, defaults to 0
            y (int, optional): The y coordinate of the rectangle, defaults to 0
            id (int, optional): An id for this rectangle, defaults to None
        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        int: The width of the rectangle;
        Setting this also validates that it is an integer and greater than 0
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating it"""
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """
        int: The height of the rectangle;
        Must be an integer and greater than 0
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating it"""

        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """
        int: The x coordinate of the rectangle;
        Must be an integer and at least 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle after validating it"""

        self.__x = value

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """
        int: The y coordinate of the rectangle;
        Must be an integer and at least 0
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle after validating it"""

        self.__y = value

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """Print the rectangle with the character '#'"""

        if self.y > 0:
            print("\n" * self.y, end="")

        for i in range(self.height):
            print(" " * self.x, end="")

            for j in range(self.width):
                print("#", end="")

            print("")

    def __str__(self):
        """Provide an informal string representation of the rectangle"""

        id, x, y, wid, hei = self.id, self.x, self.y, self.width, self.height

        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, wid, hei)

    def update(self, *args, **kwargs):
        """
        Update the rectangle's attributes;

        Args can be used to update attributes in the following order: id, width, height, x, y;
        Alternatively, kwargs can be used to specify the attributes to update by name
        """

        if len(args) != 0:
            attributes = ["id", "width", "height", "x", "y"]

            for i in range(len(args)):
                setattr(self, attributes[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the Rectangle instance into a dictionary representation

        Returns:
            dict: A dictionary representation of the rectangle
        """

        rect_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

        return rect_dict
