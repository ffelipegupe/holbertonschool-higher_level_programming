#!/usr/bin/python3
'''BaseGeometry Module'''


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        '''Instance method that raises an Exepcetion with a message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Function that validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
