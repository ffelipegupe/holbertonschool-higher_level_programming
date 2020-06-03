#!/usr/bin/python3
"""add_item module
"""

import sys

save = __import__('7-save_to_json_file').save_to_json_file

load = __import__('8-load_from_json_file').load_from_json_file
try:
    a_list = load('add_item.json')
    a_list.extend(sys.argv[1:])
    save(a_list, 'add_item.json')

except FileNotFoundError:
    save(sys.argv[1:], 'add_item.json')
