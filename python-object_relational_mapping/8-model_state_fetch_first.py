#!/usr/bin/python3
"""
This script prints the first State object from the database named 'hbtn_0e_6_usa';
It uses SQLAlchemy to interact with the database
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Create an SQLAlchemy engine that will interface with the MySQL database
    # Credentials and database name are taken from command line arguments
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)

    # Create all tables in the database which are defined in Base's subclasses
    Base.metadata.create_all(engine)

    # Start a session to handle transactions
    session = Session(engine)

    # Query for the first state object by its ID in ascending order and retrieve it
    first = session.query(State).order_by(State.id).first()

    # Try to print the state's ID and name, or print "Nothing" if no state is found
    try:
        print(f"{first.id}: {first.name}")
    except Exception:
        print("Nothing")

    # Close the session to free resources
    session.close()
