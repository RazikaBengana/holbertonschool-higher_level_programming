#!/usr/bin/python3

def remove_char_at(str, n):

    if 0 <= n <= len(str):
        str = str.replace(str[n], "")

    return str