#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed.
"""
import sys
import MySQLdb


def filter_by_input():
    """
    Connects to the database and fetches states matching the user input.
    """
    # Capture the 4 arguments from the command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish connection to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create cursor object
    cursor = db.cursor()

    # Construct the SQL query using format() as requested
    # BINARY ensures the match is case-sensitive (e.g., 'Arizona' != 'arizona')
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

    # Execute the formatted query
    cursor.execute(query)

    # Fetch and print the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Close resources
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_by_input()
