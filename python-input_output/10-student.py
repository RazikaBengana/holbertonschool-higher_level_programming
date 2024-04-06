#!/usr/bin/python3


class Student:
    """Define a class called Student that represents a student"""

    def __init__(self, first_name, last_name, age):
        # This is the initializer method for the class automatically called when a new instance of the class is created
        # It initializes the instance with the provided first name, last name, and age

        self.first_name = first_name  # Instance variable for the student's first name
        self.last_name = last_name  # Instance variable for the student's last name
        self.age = age  # Instance variable for the student's age

    def to_json(self, attrs=None):
        """
        Convert student instance to a dictionary for serialization

        Parameters:
        - attrs: Optional list of strings specifying which attributes to include in the resulting dictionary

        Returns:
        A dictionary representation of the instance;
        If 'attrs' is provided, only the specified attributes are included;
        otherwise, all attributes are included
        """

        if attrs is None:
            return self.__dict__  # Return all instance attributes if 'attrs' is None

        new_dict = {}

        for i in attrs:
            if i in self.__dict__:
                new_dict[i] = self.__dict__[i]  # Add specified attribute to the new dictionary if it exists

        return new_dict  # Return the filtered dictionary
