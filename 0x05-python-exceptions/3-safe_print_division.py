#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        if b != 0:
            res = a/b
        else:
            res = None
    except:
        pass
    finally:
        print("Inside result: {}".format(res))
        return res
