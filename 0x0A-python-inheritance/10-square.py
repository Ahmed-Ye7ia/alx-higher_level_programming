#!/usr/bin/python3
'''Module that Contains subclass Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''inherits from Rectangle.'''
    def __init__(self, size):
        Rectangle.__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area():
        return self.__size * self.__size
