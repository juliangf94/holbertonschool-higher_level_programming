#!/usr/bin/python3
"""
Start link class to table in database
This script connects to a MySQL server and creates the table
defined in model_state.py in the specified database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    # The engine is the source of connectivity to the database
    # Format: mysql+mysqldb://user:password@host/database_name
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Base.metadata.create_all(engine) is the magical line that:
    # 1. Scans all classes that inherit from Base (like State)
    # 2. Generates the SQL "CREATE TABLE" commands
    # 3. Executes them on the MySQL server
    Base.metadata.create_all(engine)
