#!/usr/bin/python3
"""
Define a function that adds two numbers together;
The function specifically handles integer and float types, converting floats to integers before addition
"""


def add_integer(a, b=98):
    """Add two integers or floats, converting them to integers if necessary

    Args:
        a: the first number, must be an integer or float
        b: the second number, defaults to 98, must be an integer or float

    Returns:
        the sum of `a` and `b` after converting them to integers

    Raises:
        TypeError: if either `a` or `b` is neither an integer nor a float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b
