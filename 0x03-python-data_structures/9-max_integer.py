#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for x in my_list:
            if x > max:
                max = x
        return max


my_list = [1, 2, 3, 90, 34, 5, -13, 40]
max_value = max_integer(my_list)
min = max_integer()
print("Max: {}".format(max_value))
print(min)
