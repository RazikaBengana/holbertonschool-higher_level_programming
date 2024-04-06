#!/usr/bin/python3
"""
This script processes a log file from standard input, keeping track of file sizes and HTTP status codes;
It outputs statistics every 10 lines and when the program is interrupted or finishes
"""

import sys


if __name__ == "__main__":  # Ensures this script runs only if it's the main program and not being imported as a module

    size = [0]  # Initializes a list to keep track of the cumulative file size

    # Initializes a dictionary to track the counts of HTTP status codes
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


    def check_match(log_line):
        """Processes a single line of input, updating the file size and the count of HTTP status codes"""

        try:
            log_line = log_line[:-1]  # Remove the last character from the line, usually a newline

            words = log_line.split(" ")  # Split the line into words using space as a delimiter

            size[0] += int(words[-1])  # Update the cumulative size with the last word converted to an integer

            code = int(words[-2])  # Retrieve the second last word as the status code

            if code in codes:  # Check if the status code is one we're tracking
                codes[code] += 1  # Update the count for this status code

        except (ValueError, IndexError):
            pass  # Ignore any errors encountered while processing a line

    def print_stats():
        """Prints the current statistics of file size and HTTP status codes"""

        print("File size: {}".format(size[0]))  # Output the cumulative file size

        for k in sorted(codes.keys()):  # Iterate through the status codes in sorted order
            if codes[k]:
                print("{}: {}".format(k, codes[k]))  # Print the count for each status code if it's non-zero

    i = 1  # Initialize a counter to track the number of lines processed

    try:
        for line in sys.stdin:  # Read each line from the standard input
            check_match(line)  # Process the line to update statistics

            if i % 10 == 0:  # Every 10 lines, print the current statistics
                print_stats()

            i += 1  # Increment the line counter

    except KeyboardInterrupt:  # Catch the interrupt signal (Ctrl+C)
        print_stats()  # Print the current statistics before exiting
        raise  # Re-raise the KeyboardInterrupt to terminate the program

    print_stats()  # Ensure statistics are printed one final time when the input ends
