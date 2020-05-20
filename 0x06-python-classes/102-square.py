#!/usr/bin/python3
'''Square class'''


class Square:
    '''Square class with an attribute'''
    def __init__(self, size=0):
        '''Private attribute size'''
        self.__size = size

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Instance method that returns the area of an Square'''
        return self.__size ** 2

    def __gt__(self, square2):
        '''Method: greater than comparison'''
        return self.area() > square2.area()

    def __ge__(self, square2):
        '''Method: greater than or equal comparison'''
        return self.area() >= square2.area()

    def __eq__(self, square2):
        '''Method: equal comparison'''
        return self.area() == square2.area()

    def __lt__(self, square2):
        '''Method: less than comparison'''
        return self.area() < square2.area()

    def __ne__(self, square2):
        '''Method: different comparison'''
        return self.area() != square2.area()

    def __le__(self, square2):
        '''Method: less than or equal comparison'''
        return self.area() <= square2.area()
