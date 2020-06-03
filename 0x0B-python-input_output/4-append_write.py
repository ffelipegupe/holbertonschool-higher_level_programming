#!/usr/bin/python3
"""append_write module
"""


def append_write(filename="", text=""):
    """Function that appends a string to a text file and returns
        the number od characters written
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
