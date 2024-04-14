#!/usr/bin/python3

"""
Script that lists all State objects that contain the letter `a`
from the database hbtn_0e_6_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `SQLAlchemy` module.
Must import `State` and `Base` from `model_state` -
`from model_state import Base, State`
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
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

    # Querying State Objects that contain the letter `a`
    states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
