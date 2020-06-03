#!/usr/bin/python3
"""save_to_json_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
