#!/usr/bin/python3
"""
Module: <module_name>
This module contains the implementation of classes for geometric shapes.

Classes:
- BaseGeometry: A base class for geometric shapes.
- Rectangle: Represents a rectangle shape.
- Square: Represents a square shape.
"""

class BaseGeometry:
    """
    BaseGeometry class provides a base for geometric shapes.

    Methods:
        - area(self): Raises an Exception with the message "area() is not implemented"
        - integer_validator(self, name, value): Validates the value as an integer.

    Attributes:
        None
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented"

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Args:
            - name (str): The name of the value.
            - value: The value to be validated.

        Raises:
            - TypeError: If the value is not an integer.
            - ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from the BaseGeometry class and represents a rectangle shape.

    Methods:
        - area(self): Calculates and returns the area of the rectangle.

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
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            - The area of the rectangle (int).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            - A string describing the rectangle in the format: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Square class inherits from the Rectangle class and represents a square shape.

    Methods:
        None

    Attributes:
        - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            - size (int): The size of the square.

        Raises:
            - TypeError: If size is not an integer.
            - ValueError: If size is less than or equal to 0.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            - A string describing the square in the format: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)