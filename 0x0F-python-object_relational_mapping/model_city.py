#!/usr/bin/python3

"""
Module that contains the class definition of a State and an instance
Base = declarative_base():
Links to the MySQL table `states`
Class attribute `id` that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key.
class attribute `name` that represents a column of a string with maximum
128 characters and can’t be null.
Must use the module SQLAlchemy.
Script should connect to a MySQL server running on localhost at port 3306
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Creating an instance of declarative_base
Base = declarative_base()


class City(Base):
    """
    Class representing the cities table.
    Linked to MySQL table "cities"
    """
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    state_id = Column(
                Integer,
                foreign_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
