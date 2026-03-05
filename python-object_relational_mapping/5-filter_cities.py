#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa. Safe from SQL injections.
Usage: ./5-filter_cities.py <user> <password> <database> <state_name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Capture arguments from the command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
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
    # Construct the SQL query using JOIN and a placeholder (%s) for safety
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    # Execute the query passing the state_name safely as a tuple
    cursor.execute(query, (state_name,))
    # Fetch all the matching rows
    query_rows = cursor.fetchall()
    # Extract just the city names from the list of tuples
    # row[0] represents the first (and only) column we selected: cities.name
    city_names = [row[0] for row in query_rows]
    # Print the city names joined by a comma and a space
    print(", ".join(city_names))
    # Clean up resources
    cursor.close()
    db.close()
