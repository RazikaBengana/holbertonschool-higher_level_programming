#!/usr/bin/python3
"""Define a function that prints a square of a given size using the '#' character"""


def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if type(size) is not int and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
