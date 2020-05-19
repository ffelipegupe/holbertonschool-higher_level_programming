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

    def my_print(self):
        '''Instance method that prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
