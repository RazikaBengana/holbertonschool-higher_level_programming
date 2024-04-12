#!/usr/bin/python3
"""This script defines the State class which is used to represent states in a database"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    A class to represent a State in a database;
    Maps to the 'states' table in the database
    """

    __tablename__ = 'states'  # Name of the table in the database
    id = Column(Integer, primary_key=True, nullable=False)  # An integer column for the primary key
    name = Column(String(128), nullable=False)  # A string column to store state names, cannot be null
