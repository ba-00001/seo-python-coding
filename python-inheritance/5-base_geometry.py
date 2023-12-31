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
