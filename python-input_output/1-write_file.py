#!/usr/bin/python3


def write_file(filename="", text=""):
    """Define a function that writes text to a file"""

    with open(filename, "w", encoding="utf-8") as file_w:
        return file_w.write(text)
