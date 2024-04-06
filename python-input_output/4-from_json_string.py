#!/usr/bin/python3


def from_json_string(my_str):
    """Define a function that converts a JSON string to a Python object"""

    import json

    return json.loads(my_str)
