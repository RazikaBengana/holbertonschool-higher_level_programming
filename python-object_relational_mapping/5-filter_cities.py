#!/usr/bin/python3
"""
This script retrieves all cities from a specific state provided as a command-line argument;
It connects to the 'hbtn_0e_4_usa' database to fetch this data
"""

import MySQLdb
from sys import argv


# Entry point of the script
if __name__ == "__main__":

    # Establish a database connection using credentials and database name provided as command-line arguments
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # SQL query to fetch names of cities in the state provided as the fourth command-line argument
    # Uses a LEFT JOIN to include states, and filters cities by the state's name
    cursor.execute("SELECT cities.name FROM cities\
                    LEFT JOIN states ON states.id = cities.state_id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (argv[4],))

    # Fetch all the rows returned from the executed SQL command
    rows = cursor.fetchall()

    # Print out city names joined by a comma
    print(", ".join([location[0] for location in rows]))
