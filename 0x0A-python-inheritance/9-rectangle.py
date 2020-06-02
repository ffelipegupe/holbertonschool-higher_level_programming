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

    def area(self):
        '''Returns the area of a rectangle'''
        return self.__width * self.__height
    
    def __str__(self):
        '''Returns a string represenation'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
