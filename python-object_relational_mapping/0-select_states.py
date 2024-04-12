#!/usr/bin/python3
"""This script lists all states from the database 'hbtn_0e_0_usa'"""

import MySQLdb
from sys import argv


# Main section to execute if the script is run as the main program
if __name__ == '__main__':

    # Connect to the MySQL database using credentials provided as command-line arguments
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to perform database operations
    cur = db.cursor()

    # Execute a query to select all records from the 'states' table
    cur.execute("SELECT * FROM states")

    # Fetch all rows from the last executed query
    rows = cur.fetchall()

    # Print each row in the result set
    for row in rows:
        print(row)
