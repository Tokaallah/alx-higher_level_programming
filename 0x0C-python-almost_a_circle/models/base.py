#!/usr/bin/python3
""" Defines the Base class """

import json

class Base:
    """ Represents the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a Base instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            return None

        dummy.update(**dictionary)  # Update the dummy instance with the provided dictionary
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a JSON file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                instance_list = []
                for dictionary in dict_list:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []

