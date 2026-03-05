#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Connects to the database and fetches states starting with N.
    """
    # Capture arguments from the command line
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Create a cursor to interact with the database
    cursor = db.cursor()
    
    # Execute SQL query to filter names starting with 'N'
    # 'LIKE BINARY' is used to ensure case sensitivity (Upper N)
    # '%' is a wildcard that matches any characters following 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch all records that match the query
    query_rows = cursor.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
