#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py that contains
the class definition of a City.
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City


# Entry point of the script
if __name__ == "__main__":

    # Create an engine to connect to the MySQL database using credentials and database name provided as command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)  # pool_pre_ping tests connections for liveness

    # Create all tables in the database if not already existing
    Base.metadata.create_all(engine)

    # Start a session to handle transactions
    session = Session(engine)

    # Query the database for all cities and their respective states
    locations = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()  # Join City and State tables on state_id

    # Print each city with its state name and city ID
    for city, state in locations:
        print("{}: ({}) {}".format(state.name, city.id, city.name))  # Format: State_name: (City_id) City_name

    # Close the session
    session.close()
