#!/usr/bin/python3
''''101-add_attribute module'''


def add_attribute(object, name, value):
    '''Function that adds a new attribute if possible'''
    if "__dict__" in dir(object):
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
