#!/usr/bin/python3
""" Peak module """


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """
    if len(list_of_integers) == 0 or not list_of_integers:
        return
    new = sorted(list_of_integers)
    return new[len(new) - 1]
