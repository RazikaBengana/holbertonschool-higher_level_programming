#!/usr/bin/python3
"""
Define a function that formats a text by inserting two newlines after each punctuation mark ('.', '?', ':');
It also strips leading and trailing spaces from each split segment of the text
"""


def text_indentation(text):

    if type(text) is not str:
        raise TypeError("text must be a string")

    for special_char in ".?:":
        if special_char == '.' or special_char == '?' or special_char == ':':
            text = (special_char + "\n\n").join(
                [lines.strip(' ') for lines in text.split(special_char)])

    print("{}".format(text), end="")
