#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        results = 0
        results = a / b
    except ZeroDivisionError:
        results = None

    finally:
        print("Inside result: {:}".format(results))
        return results
