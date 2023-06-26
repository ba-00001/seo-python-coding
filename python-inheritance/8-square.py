#!/usr/bin/python3
"""
Module
"""


Rectangle = __import__('7-rectangle.py').Rectangle


class Square(Rectangle):

    """
    Square class inherits  the Rectangle
     class and represents a square shape.

    Methods:
        N/A

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
            - A string describing the square
            in the format: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
