#!/usr/bin/python3


def load_from_json_file(filename):
    """Define a function that loads and returns data from a JSON file"""

    import json

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
