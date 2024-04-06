#!/usr/bin/python3


def class_to_json(obj):
    """
    Define a function that converts a class instance into a dictionary;
    It does this by returning the __dict__ attribute of the object,
    which contains all its attributes as key-value pairs
    """

    return obj.__dict__  # Return the dictionary containing all the attributes of the object
