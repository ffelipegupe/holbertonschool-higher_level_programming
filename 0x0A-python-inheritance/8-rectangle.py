#!/usr/bin/python3
'''Rectangle class from BaseGeometry class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''BaseGeometry subclass'''
    def __init__(self, width, height):
        '''Instantiation'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
