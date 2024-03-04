#!/usr/bin/python3
"""
a function that returns True if the object is
an instance of the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    checks if an obj is an instance of a class
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
