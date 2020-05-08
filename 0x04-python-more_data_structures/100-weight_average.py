#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        new = sum([(x[0] * x[1]) for x in my_list])
        extra = sum([x[1] for x in my_list])
        return (new/extra)
    else:
        return 0
