#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    Define a function that opens a file in append mode and writes the given text to it;
    If the file doesn't exist, it will be created
    """

    with open(filename, "a", encoding="utf-8") as file_a:
        return file_a.write(text)
