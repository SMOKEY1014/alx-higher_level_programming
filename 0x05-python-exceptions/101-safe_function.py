#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        results = fct(*args)
        return results
    except Exception as c:
        print("Exception:", c, file=sys.stderr)
        return None
