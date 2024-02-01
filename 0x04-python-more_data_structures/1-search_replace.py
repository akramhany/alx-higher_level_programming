#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = map(lambda item: (replace if item == search else item),my_list)
    return list(new_list)
