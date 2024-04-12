#!/usr/bin/python3
"""
This script establishes a connection to a MySQL database using SQLAlchemy and retrieves all states
and their associated cities, printing them to the console
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Entry point of the script
if __name__ == "__main__":

    # Create an engine connected to the MySQL database, with connection parameters supplied via command line
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)  # Create tables based on metadata

    Session = sessionmaker(bind=engine)  # Create a configured "Session" class
    session = Session()  # Instantiate a session
    states = session.query(State).order_by(State.id).all()  # Retrieve all states ordered by their IDs

    for state in states:
        print("{}: {}".format(state.id, state.name))  # Print each state's ID and name

        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))  # Print each city's ID and name, indented

    session.commit()  # Commit any changes
    session.close()  # Close the session
