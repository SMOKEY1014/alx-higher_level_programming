#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `cities.id`.
Can only use `execute()` once
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

    # Execute SQL query to select all cities and sort by id
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id ASC"""
        )

    # Fetch all rows using fetchall() method
    data = cursor.fetchall()

    # Print the fetched result
    for row in data:
        print(row)

    # Disconnect from server
    cursor.close()
    db.close()
