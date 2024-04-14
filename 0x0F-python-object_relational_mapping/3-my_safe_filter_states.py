#!/usr/bin/python3

"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, and is AFE from MySQL injection.
Parameters for script: mysql username, mysql password, database name
and state name searched.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Must use `format` to create the SQL query with the user input.
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
import sys
import re


if __name__ == "__main__":

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 5:
        u = "<username>"
        pw = "<password>"
        db = "<database>"
        print("Usage: {} {} {} {} <state_name>".format(sys.argv[0], u, pw, db))
        sys.exit(1)

    # Proceed with connecting to the database and executing the query...
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states matching the
    # provided name and sort by id
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    nameState = (re.match("^[a-zA-Z ]+$", state_name) is not None)
    cursor.execute(query, (nameState,))

    # Fetch all rows using fetchall() method
    data = cursor.fetchall()

    # Print the fetched result
    for row in data:
        if row[1][0] == 'N':
            print(row)

    # Disconnect from server
    cursor.close()
    db.close()
