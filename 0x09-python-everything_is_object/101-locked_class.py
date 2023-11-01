#!/usr/bin/python3
"""
class Square that defines a square
"""

class LockedClass:
    """class definition."""

    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
