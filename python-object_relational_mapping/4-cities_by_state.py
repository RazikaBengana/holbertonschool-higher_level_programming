#!/usr/bin/python3
"""Script to list all cities from the database 'hbtn_0e_4_usa' along with their state names"""

import MySQLdb
from sys import argv


# Entry point of the script
if __name__ == "__main__":

    # Connect to the MySQL database using parameters from command-line arguments
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()  # Create a cursor object to execute SQL queries

    # SQL query to fetch city and state names, joining 'cities' and 'states' tables
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    LEFT JOIN states ON states.id = cities.state_id\
                    ORDER BY cities.id ASC")

    rows = cursor.fetchall()  # Fetch all rows from the query result

    # Loop through each row to print city and state details
    for location in rows:
        print(location)  # Print each city's ID, name, and corresponding state name
