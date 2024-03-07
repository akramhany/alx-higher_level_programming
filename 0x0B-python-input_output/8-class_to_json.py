#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
"""

import json


def class_to_json(obj):
    """
    A function that returns the dictionary description of an object.
    """

    return json.dumps(obj.__dict__)
