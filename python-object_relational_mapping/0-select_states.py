#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
#   Allows Python to send the commands to MySQL
import MySQLdb


def list_states():
    """
    Connects to the database and fetches all states sorted by id.
    """
    # Get database credentials from command line arguments
    # sys.argv[1]: user, sys.argv[2]: password, sys.argv[3]: database name
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to the MySQL server
    # Running on localhost at port 3306 as required
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the last executed statement
    # query_rows is a list of tuples
    query_rows = cursor.fetchall()

    # Iterate through the result set and print each row
    for row in query_rows:
        print(row)

    # Clean up: close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure the code is not executed when the module is imported
    list_states()
