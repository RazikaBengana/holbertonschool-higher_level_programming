#!/usr/bin/python3
"""
Module for Square class;
Define the Square class that inherits from the Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class that extends the Rectangle class

    Attributes:
        size (int): The size of the square's sides
        x (int): The horizontal margin from the left edge
        y (int): The vertical margin from the top edge
        id (int): An identifier for instances, inherited from the Base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance

        Args:
            size (int): The size of the square's sides
            x (int): The horizontal margin from the left edge, defaults to 0
            y (int): The vertical margin from the top edge, defaults to 0
            id (int): An identifier for instances, inherited from the Base class, defaults to None
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Override the default string representation of the Square instance.=

        Returns:
            str: A string representation of the Square
        """

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        """
        Retrieve the size of the square

        Returns:
            int: The size of the square
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): The new size of the square
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square instance

        Args:
            *args: Variable length argument list for id, size, x, and y attributes
            **kwargs: Arbitrary keyword arguments for attributes
        """

        if len(args) != 0:
            attr = ["id", "size", "x", "y"]

            for i in range(len(args)):
                setattr(self, attr[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Provide a dictionary representation of a Square instance

        Returns:
            dict: A dictionary with id, size, x, and y keys
        """

        square_dict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

        return square_dict
