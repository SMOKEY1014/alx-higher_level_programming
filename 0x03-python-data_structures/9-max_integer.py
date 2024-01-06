#!/usr/bin/python3

def max_integer(my_list=[]):
    a = 0
    
    my_list.sort()
    for i in my_list:
        if a >= i:
            max_int = a
        else:
            max_int = i

    return(max_int)
        
