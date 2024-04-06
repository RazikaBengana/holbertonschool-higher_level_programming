#!/usr/bin/python3
"""Define a class for BaseGeometry"""


class BaseGeometry:
    """A base class for geometry objects"""

    def area(self):
        """
        Raise an exception with a message indicating the method is not implemented

        This method is expected to calculate the area;
        However, since this is a base class, it simply raises an Exception indicating
        that this method should be implemented by subclasses
        """

        raise Exception("area() is not implemented")
