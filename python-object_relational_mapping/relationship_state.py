#!/usr/bin/python3
"""This script is using SQLAlchemy ORM for database interactions"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class State(Base):
    """Model class for State, representing the 'states' table in the database"""

    __tablename__ = 'states'  # Specifies the name of the table in the database

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)  # Primary key column, auto-increments and must be unique

    name = Column(String(128), nullable=False)  # Column for the state's name, cannot be null

    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)  # Relationship to the City model, includes cascade options and back referencing
