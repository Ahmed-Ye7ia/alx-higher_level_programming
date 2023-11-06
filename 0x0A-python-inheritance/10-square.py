#!/usr/bin/python3
'''Module that Contains subclass Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''inherits from Rectangle.'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super.__init__(size, size)

    def area(self):
        return self.__size ** 2