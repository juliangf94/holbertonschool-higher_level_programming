#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed, safely from SQL injections.
Usage: ./3-my_safe_filter_states.py <user> <password> <database> <state_name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Capture arguments from command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    # Establish connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )
    # Create cursor
    cursor = db.cursor()
    # Use parameterized query (%s) to prevent SQL injection.
    # We pass the query string and a tuple containing the user input separately.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    # Execute the query passing the state_name as a tuple element
    cursor.execute(query, (state_name,))
    # Fetch and print results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    # Close resources
    cursor.close()
    db.close()
