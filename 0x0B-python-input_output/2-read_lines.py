#!/usr/bin/python3
"""read_lines module
"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file and prints
        it to the stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            for line in lines:
                print("{}".format(line), end="")
        else:
            for line in lines[:nb_lines]:
                print("{}".format(line), end="")
