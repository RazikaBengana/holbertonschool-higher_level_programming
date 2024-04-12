#!/usr/bin/python3
"""This script connects to a MySQL database and performs operations using SQLAlchemy"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Entry point of the script
if __name__ == "__main__":

    # Create an engine that connects to the MySQL database using credentials provided as command-line arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Generate database schema for defined models
    Base.metadata.create_all(engine)

    # Create a session to handle transactions
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new state object for California
    new_state = State(name="California")
    session.add(new_state)
    session.commit()  # Commit transaction to save the state in the database

    # Create a new city object for San Francisco associated with the state just created
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()  # Commit transaction to save the city in the database

    # Close the session
    session.close()
