#!/usr/bin/python3
def roman_to_int(roman_string):
    c = 0
    nums = {"I": 1, "V": 5, "X" = 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    for i,c in enumerate(roman_string):
        if (i+1) == len(roman_string) or nums[c] >= nums[roman_string[i+1]]:
            c += nums[c]
        else:
            c -= nums[c]
    return c
