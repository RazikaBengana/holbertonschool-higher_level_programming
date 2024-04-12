#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a' from the 'hbtn_0e_6_usa' database
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Create an engine connection to the MySQL database using credentials and database name provided via command line
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Generates database schema for models derived from Base, if not already present
    Base.metadata.create_all(engine)

    # Establish a session with the database
    session = Session(engine)

    # Query to find all states with 'a' in their names
    states = session.query(State).filter(State.name.like('%a%'))

    # Iterate over the filtered states and delete each
    for state in states:
        session.delete(state)

    # Commit the transaction to make the deletion permanent
    session.commit()

    # Close the session to free up resources
    session.close()
