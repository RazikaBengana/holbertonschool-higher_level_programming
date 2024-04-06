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

    def integer_validator(self, name, value):
        """
        Validates that the 'value' is an integer and greater than 0

        Parameters:
        - name (str): the name of the parameter, used for creating an error message
        - value (int): the value to validate

        Raises:
        - TypeError: if 'value' is not an integer
        - ValueError: if 'value' is less than or equal to 0

        This method ensures that geometric dimensions are positive integers,
        as expected in most geometric calculations
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
