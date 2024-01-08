#!/usr/bin/python3

def no_c(my_string):
    result_string = ''.join([char for char in my_string if char != 'c' and char != 'C'])
    return result_string
