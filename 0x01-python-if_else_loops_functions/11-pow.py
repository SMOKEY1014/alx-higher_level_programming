#!/usr/bin/env python3
def pow(a, b):
    # Initialize result to 1
    result = 1

    # case when the exponent is negative
    if b < 0:
        a = 1 / a
        b = -b

    # Calculating the power using a loop
    for _ in range(b):
        result *= a

    # Return the result
    return result
