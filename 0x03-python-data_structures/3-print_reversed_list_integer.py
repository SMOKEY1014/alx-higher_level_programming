#!/usr/bin/python3

def print_list_integer(my_list=[]):
    my_list.reverse()
    # ensure the function doesn't raise any errors if list is empty
    if not my_list:
        return
    for i in my_list:
        print("{:d}".format(i))
