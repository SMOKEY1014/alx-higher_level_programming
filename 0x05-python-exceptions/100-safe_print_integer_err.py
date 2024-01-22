#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except (ValueError, TypeError) as b:
        print("Exception:", b, file=sys.stderr)
        return False
