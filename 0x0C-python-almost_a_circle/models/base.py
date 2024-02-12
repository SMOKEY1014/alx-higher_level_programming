#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:

            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    @staticmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file"""
        if cls is None:
            cls = Base
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries from JSON string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set using a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy_instance = Rectangle(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = Square(1)  # Create a dummy Square instance
        else:
            raise ValueError("Invalid class name")

        dummy_instance.update(**dictionary)  # Update attributes using the dictionary
        return dummy_instance