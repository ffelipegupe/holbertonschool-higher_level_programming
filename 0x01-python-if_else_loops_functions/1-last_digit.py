#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = digit * -1
if digit > 5:
    str = "and is greater than 5"
elif digit == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, digit, str))
