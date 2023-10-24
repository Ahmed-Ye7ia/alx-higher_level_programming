#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """
    class Square definition
    Args:
        size: size of a side in square
    """

    def __init__(self, size=0):
        """
        constructor
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates area of square
        Returns:
            area
        """
        return (self.__size)**2
