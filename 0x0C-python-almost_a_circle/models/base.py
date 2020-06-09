#!/usr/bin/python3
""" Base class module
"""
import json


class Base:
    """ Base class body
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self. __nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation"""
        new_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the
            JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.dumps(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with
            all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        new_list = []
        try:
            with open(filename, 'r') as file:
                new_list = cls.from_json_string(file.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        except:
            pass
        return new_list
