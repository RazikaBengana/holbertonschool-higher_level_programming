#!/usr/bin/python3
""" Define a class named 'MyList' that inherits from the built-in list class"""


class MyList(list):
    # Inherits all the methods and properties from Python's list class
    # Define an empty pass statement as a placeholder
    pass

    # Define a method called 'print_sorted'
    def print_sorted(self):
        # This method prints the list in a sorted order without altering the original list
        print(sorted(self))