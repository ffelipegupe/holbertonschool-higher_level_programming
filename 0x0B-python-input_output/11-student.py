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
    
    def to_json(self):
        """Public method that retrieces a dictionary representation
            of a Student instance
        """
        return self.__dict__
