#!/usr/bin/python3
"""
This script lists all states with names starting with the letter 'N' (uppercase) from the 'hbtn_0e_0_usa' database
"""

import MySQLdb
from sys import argv


# Entry point of the script
if __name__ == "__main__":

    # Connect to the MySQL database using credentials and database name passed as command-line arguments
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Execute SQL query to retrieve all states, sorted by their IDs in ascending order
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
    rows = cursor.fetchall()

    # Iterate through the result and print states that start with 'N'
    for state in rows:
        if state[1][0] == 'N':
            print(state)
