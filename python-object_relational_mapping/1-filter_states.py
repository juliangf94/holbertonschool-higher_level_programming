#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Establish connection to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create a cursor to interact with the database
    cursor = db.cursor()
    # Execute SQL query to filter names starting with 'N'
    # 'LIKE BINARY' is used to ensure case sensitivity (Upper N)
    # '%' is a wildcard that matches any characters following 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY states.id ASC")
    # Fetch all records that match the query
    query_rows = cursor.fetchall()
    # Display the results
    for row in query_rows:
        print(row)
    # Close the cursor and the database connection
    cursor.close()
    db.close()
