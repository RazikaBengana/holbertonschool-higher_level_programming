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
        Returns a dictionary representation of the Student instance;
        This method allows for filtering which attributes are included in the resulting dictionary

        Parameters:
        attrs (list): Optional;
                      A list of strings representing the names of the attributes
                      that should be included in the resulting dictionary;
                      If None, all attributes are included

        Returns:
        dict: A dictionary containing key/value pairs of attributes
        """

        if attrs is None:
            return self.__dict__  # Returns the full dictionary representation if no attrs specified

        new_dict = {}

        for i in attrs:
            if i in self.__dict__:
                new_dict[i] = getattr(self, i)  # Adds attribute to new_dict if it's specified in attrs

        return new_dict

    def reload_from_json(self, json):
        """
        Updates the attributes of the Student instance based on a dictionary input
        (typically from a JSON structure)

        Parameters:
        json (dict): A dictionary where keys are attribute names and values are
                     the corresponding values to set on the instance
        """

        for key, value in json.items():
            setattr(self, key, value)  # Sets each attribute to the corresponding value found in the json dictionary
