#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in my_list:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list
