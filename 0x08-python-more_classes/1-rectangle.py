#!/usr/bin/python3
"""Rectangle Class source"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """width value setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
