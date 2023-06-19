#!/usr/bin/python3

"""Takes in a number n, returns the square of n"""


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
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
