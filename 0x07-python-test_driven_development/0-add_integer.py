#!/usr/bin/python3

def add_integer(a, b=98):


    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer".format(a))
    else:
        a = int(a)

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer".format(b))
    else:
        b = int(b)

    return int(a) + int(b)