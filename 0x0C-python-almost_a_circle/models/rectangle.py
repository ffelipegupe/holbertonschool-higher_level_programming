#!/usr/bin/python3
""" Rectangle class module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle bass body
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Public method that returns the area of a Rectangle """
        return self.__height * self.__width

    def display(self):
        """ Public method that prints in stdout the Rectangle with # """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ __str__ method overriding """
        a = type(self).__name__
        b = self.id
        c = self.x
        d = self.y
        e = self.width
        f = self.height
        return "[{}] ({}) {}/{} - {}/{}".format(a, b, c, d, e, f)

    def update(self, *args, **kwargs):
        """ Public method that assigns an argument to each attribute """
        if len(args) != 0:
            i = 0
            attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, attrs[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Public method that returns the dictionary representation
            of a Rectangle
        """
        keys = ["id", "width", "height", "x", "y"]
        dict_square = {}
        for key in keys:
            dict_square[key] = getattr(self, key)
        return dict_square
