#!/usr/bin/python3
"""
Contains MyInt class
"""


class MyInt(int):
    '''Contains class MyInt that inherits from int'''
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
