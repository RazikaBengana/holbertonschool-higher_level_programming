#!/usr/bin/python3
"""This script defines the 'City' class using SQLAlchemy ORM"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    A class that represents a City in the database;
    Inherits from Base which connects class definitions to their corresponding tables
    """

    __tablename__ = 'cities'  # Defines the table name in the database
    id = Column(Integer, primary_key=True, nullable=False)  # Primary key column, cannot be null
    name = Column(String(128), nullable=False)  # Name column, cannot be null
    state_id = Column(Integer, ForeignKey('states.id'))  # Foreign key referencing 'states.id'
