#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

number_digit = str(number)

last_digit = number_digit[-1]

digit = int(last_digit)

if (number <= -1):
    last_digit = "-" + last_digit

print(f"Last digit of {number}, is {last_digit} and is ", end=" ")

if (digit) > 5:
    print(f"greater than 5")
elif digit == 0:
    print(f"0")
else:
    print(f"less than 6 and not 0")
