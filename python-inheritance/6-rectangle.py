#!/usr/bin/python3
"""
Module: rectangle

This module provides a class called Rectangle, which inherits
from the BaseGeometry class. The Rectangle class represents
a rectangle shape and provides functionality for calculating its area.

Classes:
    - Rectangle: A class representing a rectangle shape.

Exceptions:
    - TypeError: Raised when the value is not an integer.
    - ValueError: Raised when the value is less than or equal to 0.
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from the BaseGeometry class and represents a rectangle shape.

    Attributes:
        - __ width (int): The width of the rectangle.
        - __ height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.

        Args:
            - width (int): The width of the rectangle.
            - height (int): The height of the rectangle.

        Raises:
            - TypeError: If width or height is not an integer.
            - ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("{}".format(width), self.__width)
        self.integer_validator("{}".format(height), self.__height)
