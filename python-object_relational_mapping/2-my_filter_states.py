#!/usr/bin/python3
"""Displays all states matching the name argument from hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Establish connection to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create cursor object
    cursor = db.cursor()
    # Construct the SQL query using format() as requested
    # BINARY ensures the match is case-sensitive (e.g., 'Arizona' != 'arizona')
    # Execute the formatted query
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )
    # Fetch and print the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    # Close resources
    cursor.close()
    db.close()
