#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) < n or n < 0:
        return str
    else:
        str2 = str.replace(str[n], '')
        return str2
