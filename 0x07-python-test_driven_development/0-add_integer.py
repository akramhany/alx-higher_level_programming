#!/usr/bin/python3

""" A module that contains the add_integer function """


def add_integer(a, b=98):
    """
    A function that takes 2 integers or floats (a, b) and returns their sum
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        a = int(a)
    
    if isinstance(b, float):
        b = int(b)

    return a + b
