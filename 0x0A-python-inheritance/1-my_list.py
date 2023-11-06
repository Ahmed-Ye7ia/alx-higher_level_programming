#!/usr/bin/python3
"""
Contains class MyList that inherits from list
"""


class MyList(list):
    """
    inherits from list
    """
    def print_sorted(self):
        """prints list sorted in ascending order"""
        print(sorted(self))
