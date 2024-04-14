#!/usr/bin/python3
"""
Script that lists all State objects from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # if your password contains special charecter like '@',
    # replace it with '%40' in your terminal argument
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Connection string for SQLAlchemy
    connection_string = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    # Create SQLAlchemy engine
    engine = create_engine(connection_string)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and sort them by id
    state = session.query(State).order_by(State.id).first()

    # Print the results
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
