#!/usr/bin/python3
"""A script to display cities with their corresponding state from a database using SQLAlchemy ORM"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Entry point of the script
if __name__ == "__main__":

    # Create a connection to the database using MySQL with credentials provided as command line arguments
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the database (this will have no effect if tables are already present)
    Base.metadata.create_all(engine)

    # Create a session to manage transactions
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all cities in ascending order by city ID and print them with their related state
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Commit changes and close the session
    session.commit()
    session.close()
