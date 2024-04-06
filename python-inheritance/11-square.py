#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle
# Import BaseGeometry class


class Square(Rectangle):
    """Define a class named Square, which inherits from Rectangle"""

    def __init__(self, size):
        # Constructor method for Square class --> it initializes a new Square instance with the size attribute

        self.integer_validator("size", size)
        # Validate 'size' using the inherited method from Rectangle or its parent, ensuring it's an integer

        super().__init__(size, size)
        # Call the constructor of the parent class (Rectangle) with 'size' as both the width and height,
        # since a square's sides are equal

        self.__size = size
        # Set the private attribute '__size' for the Square instance

    def area(self):
        # Method to calculate the area of the Square

        return self.__size ** 2  # Return the square of the 'size' attribute, which is the area of the Square

    def __str__(self):
        # Special method to return the string representation of the Square object

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
        # Return a string indicating the object is a Square along with its size
