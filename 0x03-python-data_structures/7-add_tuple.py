#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    padded_tuple_a = tuple_a + (0,) * (len(tuple_b) - len(tuple_a))
    padded_tuple_b = tuple_b + (0,) * (len(tuple_a) - len(tuple_b))

    new_tuple = tuple(a + b for a, b in zip(padded_tuple_a, padded_tuple_b))
    return (new_tuple)
