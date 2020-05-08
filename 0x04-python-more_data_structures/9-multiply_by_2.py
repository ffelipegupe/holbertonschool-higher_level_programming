#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {x: y * 2 for x, y in a_dictionary.items()}
    return new
