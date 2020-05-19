#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)        
    except Exception as e:
        res = None
        print("Exception:", e.args[0], file=sys.stderr)
    return res
