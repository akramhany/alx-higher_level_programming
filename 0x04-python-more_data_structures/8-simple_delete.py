#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return
    del a_dictionary[key]
