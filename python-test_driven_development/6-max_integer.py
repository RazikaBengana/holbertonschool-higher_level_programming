#!/usr/bin/python3
"""
Module to find the maximum integer in a list;
If the list is empty, it returns None
"""


def max_integer(list=[]):

    if len(list) == 0:
        return None

    result = list[0]
    i = 1

    while i < len(list):
        if list[i] > result:
            result = list[i]

        i += 1

    return result
