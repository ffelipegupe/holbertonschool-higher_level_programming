#!/usr/bin/python3
"""write_file module
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and returns
        the number od characters written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
