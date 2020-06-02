#!/usr/bin/python3
'''Rectangle class from BaseGeometry class'''


class Rectangle(BaseGeometry):
    '''BaseGeometry subclass'''
    def __init__(self, width, height):
        '''Instantiation'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
