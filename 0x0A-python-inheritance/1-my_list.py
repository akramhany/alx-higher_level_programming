#!/usr/bin/python3
"""
a class that inheirts from list class.
"""


class MyList(list):
    """ a simple class that inherits from list class """

    def print_sorted(self):
        sortedL = self[:]
        sortedL.sort()
        print(sortedL)
        return sortedL
