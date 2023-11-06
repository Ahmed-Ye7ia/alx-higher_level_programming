#!/usr/bin/python3
'''Module that Contains subclass Square.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    '''inherits from Rectangle.'''
    def __init__(self, size):
        Rectangle.__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area():
        return self.__size * self.__size
