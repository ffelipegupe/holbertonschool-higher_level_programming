#!/usr/bin/python3
""" read_file module
"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")

read_file("my_file_0.txt")