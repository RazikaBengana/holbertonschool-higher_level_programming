#!/usr/bin/python3


def read_file(filename=""):
    """Define a function that reads content from a file and prints it"""

    with open(filename, "r", encoding="utf-8") as file_r:
        print(file_r.read(), end='')
