#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    else:
        my_list.sort()
        return str(my_list[-1])
