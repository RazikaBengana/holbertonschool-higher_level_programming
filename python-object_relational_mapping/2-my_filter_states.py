#!/usr/bin/python3
"""
This script takes an argument and displays all values in the 'states' table
of the 'hbtn_0e_0_usa' database where the name matches the given argument;
It sorts the results by state ID in ascending order
"""

import MySQLdb
from sys import argv


# Entry point of the script
if __name__ == "__main__":

    # Connect to the MySQL database using credentials and database name provided as command-line arguments
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SQL query to find states that match the specified name exactly, case-sensitively
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                    ORDER BY states.id ASC".format(argv[4]))

    # Fetch all the rows returned by the SQL query
    rows = cursor.fetchall()

    # Iterate over each row and print it
    for state in rows:
        print(state)
