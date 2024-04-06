#!/usr/bin/python3
"""Module defining the Base class, which serves as the foundation for other classes in this project"""


import json


class Base:
    """
    This class provides a base for other classes to build upon;
    It handles id assignment and JSON serialization
    """

    __nb_objects = 0  # Counter for new id assignment when no id is provided

    def __init__(self, id=None):
        """
        Initialize a new Base instance;
        Assign a unique id automatically if none is provided

        Args:
            id (int, optional): The id of the instance;
                                If None, an id is generated automatically
        """

        if id is not None:
            self.id = id  # Use provided id

        else:
            Base.__nb_objects += 1  # Increment the count to generate a new id
            self.id = Base.__nb_objects  # Assign the new id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string

        Args:
            list_dictionaries (list): A list of dictionaries representing instances

        Returns:
            str: The JSON string representation of list_dictionaries;
                 Returns an empty list as JSON if input is empty
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file named after the class name

        Args:
            list_objs (list): A list of instances that are subclass of Base
        """

        n_file = "{}.json".format(cls.__name__)
        list_of_dic = []

        if list_objs is not None:
            for element in list_objs:
                list_of_dic.append(cls.to_dictionary(element))

        with open(n_file, mode="w", encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_of_dic))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string

        Args:
            json_string (str): String representing a list of dictionaries

        Returns:
            list: The list represented by json_string;
                  Returns an empty list if json_string is None or empty
        """

        if json_string is None or json_string == "":
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set based on the dictionary provided

        Args:
            **dictionary: Arbitrary keyword arguments containing attributes for the instance

        Returns:
            Instance of cls with attributes set according to the dictionary
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)

            else:
                dummy = cls(1)
            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Read from a file named <cls.__name__>.json and returns instances based on the file content

        Returns:
            list: A list of instances created from the file content
                  Returns an empty list if the file does not exist
        """

        name_of_file = cls.__name__ + ".json"
        json_obj = []

        try:
            with open(name_of_file, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])

        except FileNotFoundError:
            pass

        return json_obj
