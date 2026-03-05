#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


def list_cities():
    """
    Connects to the database and fetches all cities with their respective
    state names, using an INNER JOIN.
    """
    # Capture the 3 arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query using JOIN to combine cities and states
    # We select city id, city name, and state name.
    # We match them where the state_id in cities matches the id in states.
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    # Execute the query (Only once, as required)
    cursor.execute(query)

    # Fetch all the rows
    query_rows = cursor.fetchall()

    # Print the results in the exact format required
    for row in query_rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
