#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.
    Links to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    
    name = Column(
        String(128),
        nullable=False
    )
