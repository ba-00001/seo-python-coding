#!/usr/bin/python3
"""
Module: base_geometry

This module provides a class called BaseGeometry
 that serves as a base class for geometry-related operations.

Classes:
    - BaseGeometry: A base class for geometry-related operations.

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
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Placeholder method for calculating the area of a shape."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
