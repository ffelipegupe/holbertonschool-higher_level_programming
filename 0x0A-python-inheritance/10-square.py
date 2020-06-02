#!/usr/bin/python3
'''Square class from Rectangle class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square subclass'''
    def __init__(self, size):
        '''Instantiation'''
        super().integer_validator("size", size)
        super().__init__(size, size)
