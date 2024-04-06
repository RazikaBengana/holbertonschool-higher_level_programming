#!/usr/bin/python3


def add_attribute(obj, attribute, value):
    """
    Function that dynamically adds an attribute to an object;
    It checks if the object can accept new attributes by looking into its __dict__ or __slots__
    """

    if hasattr(obj, "__dict__"):
        # Check if the object has a __dict__ attribute, which stores its attributes

        setattr(obj, attribute, value)
        # If yes, use setattr to add or update the attribute

    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        # If the object doesn't have __dict__, check if it has __slots__
        # __slots__ is used in objects to declare a fixed set of attributes, reducing memory usage

        setattr(obj, attribute, value)
        # If the attribute is allowed in __slots__, set the attribute
    else:
        raise TypeError("can't add new attribute")
        # If neither conditions are met, it means the object cannot accept new attributes
        # Raise a TypeError to indicate that new attributes can't be added
