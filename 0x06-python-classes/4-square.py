#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Property for the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns:
            The size squared.
        """
        return self.__size ** 2
