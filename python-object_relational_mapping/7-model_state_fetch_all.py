#!/usr/bin/python3
"""
This script lists all State objects from the database specified by the user;
It uses SQLAlchemy ORM to interact with the database.
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Create an engine instance. Connection details are taken from command line arguments
    # The 'mysql+mysqldb' specifies the database dialect and driver to use
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the database which are defined in Base's subclasses
    Base.metadata.create_all(engine)

    # Start a session to handle transactions
    session = Session(engine)

    # Query the database to retrieve all State objects, ordered by their id
    for state in session.query(State).order_by(State.id).all():
        # Print the state's id and name
        print("{}: {}".format(state.id, state.name))

    # Close the session to free resources
    session.close()
