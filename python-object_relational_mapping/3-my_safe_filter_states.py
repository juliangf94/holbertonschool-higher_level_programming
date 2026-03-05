#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed, safely from SQL injections.
Usage: ./3-my_safe_filter_states.py <user> <password> <database> <state_name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create cursor
    cursor = db.cursor()
    # Use parameterized query (%s) to prevent SQL injection.
    # We pass the query string and a tuple containing
    # the user input separately.
    # Execute the query passing the state_name as a tuple element
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    # Fetch and print results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    # Close resources
    cursor.close()
    db.close()
