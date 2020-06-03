#!/usr/bin/python3
"""from_json_string module
"""


import json


def from_json_string(my_str):
    """Function an object represented by a JSON string
    """
    return json.loads(my_str)
