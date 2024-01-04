#!/usr/bin/python3
import sys

""" This code works both for command-line and can be imported to another function"""

def sum_of_args(string):
    # Split the string into a list of substrings
    args_list = string.split()

    # Initial sum is 0
    total_sum = 0

    # Iterating over the substrings and add their integer values to the sum
    for arg in args_list:
        try:
            total_sum += int(arg)
        except ValueError:
            print("Invalid argument: {}".format(arg))

    return total_sum

# Get the command-line arguments as a single string
args_string = ' '.join(sys.argv[1:])

# Calculate the sum of the arguments
result = sum_of_args(args_string)

# Print the result
print(result)
