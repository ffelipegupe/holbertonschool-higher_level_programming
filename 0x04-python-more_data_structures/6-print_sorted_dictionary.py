#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.items())
    for i, j in new:
        print("{}: {}".format(i, j))
