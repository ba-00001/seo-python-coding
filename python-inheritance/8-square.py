#!/usr/bin/python3
"""
Module documented
"""


Rectangle = __import__('7-rectangle.py').Rectangle


class Square(Rectangle):
    """
    Module documented
    """

    def __init__(self, size):
        """
        Module documented
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Module documented
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
