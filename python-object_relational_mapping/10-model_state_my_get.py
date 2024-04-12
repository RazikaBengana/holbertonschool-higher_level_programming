#!/usr/bin/python3
"""This script prints the ID of a State object with the specified name from the database 'hbtn_0e_6_usa'"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Create an engine instance: Connect to the MySQL database using credentials provided as command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)  # use formatting to input command-line arguments

    # Create all tables in the database which are defined by Base's subclasses such as State
    Base.metadata.create_all(engine)

    # Create a session to handle transactions
    session = Session(engine)

    # Query the database for the State object whose name matches the command-line argument
    state = session.query(State).filter(
        State.name == argv[4]).first()  # .first() returns the first result or None if no match is found

    try:
        # Try to print the id of the state found
        print("{}".format(state.id))

    except Exception:
        # If the state object is None (not found), print "Not found"
        print("Not found")

    # Close the session to free resources
    session.close()
