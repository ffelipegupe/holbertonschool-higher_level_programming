#!/usr/bin/python3
import math


class MagicClass:
    '''Circle class'''

    def __init__(self, radius=0):
        '''Circle class instantiation'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''Method that returns the area'''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''Method that returns the circumference'''
        return (2 * math.pi * self.__radius)
