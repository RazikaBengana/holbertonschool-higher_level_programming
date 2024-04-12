#!/usr/bin/python3
"""
This script changes the name of a State object within the database specified;
It targets a database named 'hbtn_0e_6_usa' and updates the state name for the entry with ID 2 to 'New Mexico'
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Establishes connection to the database using credentials provided as command line arguments
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)

    # Generates database schema (creates tables if they don't already exist)
    Base.metadata.create_all(engine)

    # Creates a new session to handle transactions
    session = Session(engine)

    # Fetches the State object with ID 2 from the database
    state = session.query(State).filter(State.id == 2).first()

    # Updates the State name
    state.name = 'New Mexico'

    # Commits the changes to the database
    session.commit()

    # Closes the session
    session.close()
