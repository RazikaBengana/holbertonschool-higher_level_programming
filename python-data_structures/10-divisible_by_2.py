#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if my_list:
        list_copy = [n % 2 == 0 for n in my_list]
        return list_copy

    else:
        return False
