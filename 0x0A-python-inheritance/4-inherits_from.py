#!/usr/bin/python3
'''inherits_from module'''


def inherits_from(obj, a_class):
    '''Function that checks object inheritance'''
    return (isinstance(obj, a_class) and (type(obj) is not a_class))
