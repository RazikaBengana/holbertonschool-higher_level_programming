#!/usr/bin/python3


class Student:
    """Define a class called Student that represents a student"""

    def __init__(self, first_name, last_name, age):
        # This is the initializer method for the class automatically called when a new instance of the class is created
        # It initializes the instance with the provided first name, last name, and age

        self.first_name = first_name  # Instance variable for the student's first name
        self.last_name = last_name  # Instance variable for the student's last name
        self.age = age  # Instance variable for the student's age

    def to_json(self):
        # This method returns a dictionary representation of the Student instance
        # It uses the special __dict__ attribute which contains all the instance variables

        return self.__dict__  # Returns a dictionary containing all instance variables
