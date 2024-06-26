#!/usr/bin/python3
"""Define a function that prints a given name"""


def say_my_name(first_name, last_name=""):

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
