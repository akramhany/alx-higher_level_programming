#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding="utf-8") as f:
        obj = f.read()
        json_obj = json.loads(obj)
    return json_obj
