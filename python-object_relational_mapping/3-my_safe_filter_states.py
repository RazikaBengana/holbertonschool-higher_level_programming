#!/usr/bin/python3
"""
A Python script that securely queries the database using command line arguments;
This script takes command line arguments and fetches all entries from the 'states'
table in the specified database where the name matches the given argument;
It is designed to prevent SQL injection vulnerabilities by using parameterized queries
"""

import MySQLdb
from sys import argv


# Entry point of the script
if __name__ == "__main__":

    # Connecting to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Creating a cursor object using the cursor() method
    cursor = db.cursor()

    # Executing SQL query using parameterized statement for security
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id ASC", (argv[4],))

    # Fetching all rows from the executed SQL command
    rows = cursor.fetchall()

    # Printing the fetched data
    for state in rows:
        print(state)
