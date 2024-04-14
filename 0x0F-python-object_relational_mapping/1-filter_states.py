#!/usr/bin/python3

"""
Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select all states and sort by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows using fetchall() method
    data = cursor.fetchall()

    # Print the fetched result
    for row in data:
        if row[1][0] == 'N':
            print(row)

    # Disconnect from server
    cursor.close()
    db.close()
