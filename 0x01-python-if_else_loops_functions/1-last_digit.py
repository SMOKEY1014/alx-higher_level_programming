#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10

if (num > 5):
    print("{} and is greater than 5".format(num), end="\n")
elif (num == 0):
    print("{} and is zero".format(num), end="\n")
else:
    print("{} and is less than 6 and not 0".format(num), end="\n")
