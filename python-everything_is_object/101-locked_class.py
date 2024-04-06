#!/usr/bin/python3
"""
define a class with no class or object attribute,
that prevents the user from dynamically creating
new instance attributes, except if the new instance
attribute is called 'first_name'
"""


class LockedClass:
    """
    This class is designed to prevent the creation of instance attributes,
    except for a single attribute named 'first_name';
    This is achieved through the use of __slots__;

    __slots__ is a special attribute that explicitly declares which instance attributes are allowed;
    Here, it restricts instance attributes to only 'first_name';
    Attempting to create other attributes will result in an AttributeError
    """

    __slots__ = "first_name"
