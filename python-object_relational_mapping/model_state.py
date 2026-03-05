#!/usr/bin/python3
"""Contains the State class and Base instance for SQLAlchemy ORM"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """State class linked to the states MySQL table"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )

    name = Column(
        String(128),
        nullable=False
    )
