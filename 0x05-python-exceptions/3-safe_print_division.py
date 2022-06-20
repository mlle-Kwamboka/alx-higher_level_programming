#!/usr/bin/python3
def safe_print_division(a, b):
    Inside result = a / b
    try:
        print("Inside result: {:d}".format(Inside result))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        print("{:d} / {:d} = {:d}".format(a, b, Inside result))
    return Inside result
