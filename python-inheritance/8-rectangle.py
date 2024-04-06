#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry
# Import BaseGeometry class


class Rectangle(BaseGeometry):
    """Define a class named Rectangle, which inherits from BaseGeometry"""

    def __init__(self, width, height):
        # Constructor method with parameters for width and height

        super().integer_validator("width", width)
        # Call the integer_validator method from the parent class (BaseGeometry) to validate 'width'

        self.__width = width
        # Set the private attribute '__width' to the validated 'width'

        super().integer_validator("height", height)
        # Call the integer_validator method from the parent class (BaseGeometry) to validate 'height'

        self.__height = height
        # Set the private attribute '__height' to the validated 'height'
