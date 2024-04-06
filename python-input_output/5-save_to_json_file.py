#!/usr/bin/python3


def save_to_json_file(my_obj, filename):
    """Define a function that saves a Python object to a file in JSON format"""

    import json

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
