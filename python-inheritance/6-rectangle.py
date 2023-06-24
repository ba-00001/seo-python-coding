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

class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class provides a placeholder method for
    calculating the area of a shape and a method for validating integer values.

    Public Methods:
        - area(self): Placeholder method for calculating the area of a shape.
        - integer_validator(self, name, value): Validates an integer value.

    Exceptions:
        - TypeError: Raised when the value is not an integer.
        - ValueError: Raised when the value is less than or equal to 0.
    """

    def area(self):
        """
        Placeholder method for calculating the area of a shape.

        Raises:
            Exception: Always raises an exception with
            the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from the BaseGeometry class and represents a rectangle shape.

    Attributes:
        - __width (int): The width of the rectangle.
        - __height (int): The height of the rectangle.
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
