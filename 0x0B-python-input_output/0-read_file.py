#!/usr/bin/python3
""" read_file module
"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(f.read(), end="")
