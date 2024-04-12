#!/usr/bin/python3
"""
This script lists all State objects from the 'hbtn_0e_6_usa' database that contain the letter 'a' in their names
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Connect to the database using credentials and database name passed as command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the database (safe to call if tables already exist)
    Base.metadata.create_all(engine)

    # Create a session to handle database transactions
    session = Session(engine)

    # Query the database for states containing the letter 'a', ordered by state ID
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    # Print each state's ID and name that contains the letter 'a'
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session to release database connections
    session.close()
