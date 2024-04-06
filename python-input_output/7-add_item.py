#!/usr/bin/python3
"""
This script adds all arguments passed to it on the command line to a list, and then saves that list to a file;
The file used for storage is 'add_item.json';
If the file already exists, the script loads the existing data and appends the new items;
If the file doesn't exist, it starts with an empty list;
This is useful for creating or updating a JSON file with a list of items from command line arguments
"""


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # Attempts to load an existing list from 'add_item.json'
    # If the file doesn't exist, it raises an exception
    my_list = load_from_json_file("add_item.json")

except FileNotFoundError:
    # If the file doesn't exist or another error occurs, it starts with an empty list
    my_list = []

# Adds the command line arguments (excluding the script name) to the list and saves back to 'add_item.json'
save_to_json_file(my_list + argv[1:], "add_item.json")
