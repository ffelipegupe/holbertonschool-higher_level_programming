#!/usr/bin/python3
"""number_of_lines
"""


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file
    """
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
