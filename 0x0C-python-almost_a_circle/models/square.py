#!/usr/bin/python3
""" Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class body
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """size getter"""
        return self.width
    
    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
    
    def __str__(self):
        """__str__ overriding"""
        a = type(self).__name__
        b = self.id
        c = self.x
        d= self.y
        e = self.size
        return "[{}] ({}) {}/{} - {}".format(a, b, c, d, e)

    def update(self, *args, **kwargs):
        """ Public method that assigns an argument to each attribute """
        if len(args) != 0:
            i = 0
            attrs = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, attrs[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Public method that returns the dictionary representation
            of a Square
        """
        keys = ["id", "size", "x", "y"]
        dict_square = {}
        for key in keys:
            dict_square[key] = getattr(self, key)
        return dict_square
