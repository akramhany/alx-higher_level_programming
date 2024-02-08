#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num_of_ints = 0
    try:
        while i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                num_of_ints += 1
            i += 1
        print()
        return num_of_ints
    except IndexError:
        raise
