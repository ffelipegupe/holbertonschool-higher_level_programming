#!/usr/bin/python3
"""
Addition of two numbers
"""


def add_integer(a, b=98):
    """ Function that adds two integers """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a + b == float('inf'):
        return float('inf')
    if a + b == -float('inf'):
        return -float('inf')
    return int(a + b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")