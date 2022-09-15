#!/usr/bin/python3
from decimal import DivisionByZero


def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(res))
