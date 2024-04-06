#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """
    Define a function that opens a file to search for a given string,
    and inserts a new string right after every occurrence of that search string
    """

    with open(filename, "r", encoding="utf-8") as f:  # Open the file in read mode with UTF-8 encoding

        lines = f.readlines()  # Read all lines in the file and store them in the list

        i = 0  # Initialize a counter to iterate through the list of lines

        while i < len(lines):  # Iterate over each line in the list

            if search_string in lines[i]:  # Check if the current line contains the search string
                lines[i:i + 1] = [lines[i], new_string]  # If found, insert the new string right after the current line
                i += 1  # Increment counter to skip the newly added string
            i += 1

    with open(filename, "w", encoding="utf-8") as f:  # Open the file in write mode to update it
        f.writelines(lines)  # Write the updated list of lines back to the file
