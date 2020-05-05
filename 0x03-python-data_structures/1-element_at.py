#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if my_list.index(i) == idx:
            return i
