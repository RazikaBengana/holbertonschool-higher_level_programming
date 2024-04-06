#!/usr/bin/python3


class MyInt(int):
    """Define a class named MyInt, which inherits from Python's built-in int class"""

    def __eq__(self, other):
        # Overriding the equality method (__eq__)
        # This method is called when the '==' operator is used
        # Instead of checking for equality, it checks for inequality between the MyInt instance and another value
        return int(self) != int(other)  # Return True if the values are not equal.

    def __ne__(self, other):
        # Overriding the inequality method (__ne__)
        # This method is called when the '!=' operator is used
        # Surprisingly, it checks for equality, opposite of the standard behavior
        return int(self) == int(other)  # Return True if the values are equal
