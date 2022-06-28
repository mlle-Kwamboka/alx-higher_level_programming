#!/usr/bin/python3
"""
module add_integer
Adds two integers

"""
def add_integer(a, b=98):
    """Adds two integers or floats and returns the result
    or an error if a and b are not of type float or integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
