#!/usr/bin/python3
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
