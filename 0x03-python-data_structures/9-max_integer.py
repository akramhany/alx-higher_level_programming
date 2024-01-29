#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxInt = 0
    for integer in my_list:
        if integer > maxInt:
            maxInt = integer
    return maxInt
