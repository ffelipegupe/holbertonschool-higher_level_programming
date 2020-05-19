#!/usr/bin/python3
'''Square class'''


class Square:
    '''Square class with an attribute'''
    def __init__(self, size=0, position=(0, 0)):
        '''Private attribute size'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @property
    def position(self):
        '''position getter'''
        return self.__position

    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        '''position setter'''
        if type(value) is not tuple and len(value) != 2 and value <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        '''Instance method that returns the area of an Square'''
        return self.__size ** 2

    def my_print(self):
        '''Instance method that prints in stdout the square #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if self.__position[0] > 0:
                        print("")
                        print("#", end="")
                print()
