#!/usr/bin/python3
"""add_item module
"""

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    a_list = load_from_json_file('add_item.json')
    a_list.extend(sys.argv[1:])
    save_to_json_file(a_list, 'add_item.json')

except FileNotFoundError:
    save_to_json_file(sys.argv[1:], 'add_item.json')
