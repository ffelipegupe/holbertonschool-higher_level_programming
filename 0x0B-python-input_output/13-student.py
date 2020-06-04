#!/usr/bin/python3
"""Student class module
"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieces a dictionary representation
            of a Student instance
        """
        a_dict = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if attr in self.__dict__:
                    a_dict[attr] = self.__dict__.get(attr)
            return a_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Public method that replaces all attributes of the Student instance
        """
        for i, x in json.items():
            self.__dict__[i] = x
