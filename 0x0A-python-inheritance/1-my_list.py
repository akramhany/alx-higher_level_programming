#!/usr/bin/python3
"""
a class that inheirts from list class.
"""


class MyList(list):
    """ a simple class that inherits from list class """

    def print_sorted(self):
        self.sort()
        print(self)