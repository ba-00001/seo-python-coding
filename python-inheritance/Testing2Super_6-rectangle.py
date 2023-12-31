#!/usr/bin/python3
"""Module documented"""


class BaseGeometry:
    """Module documented"""

    def area(self):
        """Module documented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Module documented"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Module documented"""

    def __init__(self, width, height):
        """Module documented"""
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("{}".format(width), self.__width)
        self.integer_validator("{}".format(height), self.__height)
