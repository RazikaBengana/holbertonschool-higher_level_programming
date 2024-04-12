#!/usr/bin/python3
"""This script uses SQLAlchemy ORM to define a class representing a city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Definition of the City model which maps to the 'cities' table in the database"""

    __tablename__ = "cities"  # Name of the table in the database

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)  # Primary key, auto-incremented, unique ID

    name = Column(String(128), nullable=False)  # City name field, cannot be null

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)  # Foreign key linking to the 'states' table
