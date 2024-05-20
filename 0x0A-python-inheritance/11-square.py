#!/usr/bin/python3
"""Inherits from Rectangle  class 9-rectangle.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class definition"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
