#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description of an object.
    """

    return obj.__dict__
