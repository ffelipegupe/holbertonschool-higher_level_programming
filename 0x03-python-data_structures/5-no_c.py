#!/usr/bin/python3
def no_c(my_string):
    l_string = list(my_string)
    str = ""
    if "c" in l_string:
        l_string.remove("c")
    if "C" in l_string:
        l_string.remove("C")
    str = str.join(l_string)
    return str
