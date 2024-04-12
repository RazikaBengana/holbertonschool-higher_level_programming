#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database named hbtn_0e_6_usa and prints its id
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Entry point of the script
if __name__ == "__main__":

    # Create an engine connected to the MySQL database using credentials and database name from command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Start a session to interact with the database
    session = Session(engine)

    # Create a new State object for Louisiana and add it to the session
    new = State(name='Louisiana')
    session.add(new)

    # Retrieve the new State object from the database, to get the assigned ID, and print it
    newState = session.query(State).filter(State.name == 'Louisiana').first()
    print(str(newState.id))

    # Commit the transaction to the database and close the session
    session.commit()
    session.close()
