#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry class provides a base class for geometric shapes.

    Methods:
        - area(): Calculates the area of the geometric shape.
        - integer_validator(name, value): Validates that a value is an integer and greater than 0.
    """

    def area(self):
        """
        Calculates the area of the geometric shape.

        Raises:
            - Exception: When area() is not implemented in the derived class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and greater than 0.

        Args:
            - name (str): The name of the value.
            - value (int): The value to be validated.

        Raises:
            - TypeError: If the value is not an integer.
            - ValueError: If the value is less than or equal to 0.
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
        super().__init__()  # Call the parent class constructor
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)


print(issubclass(Rectangle, BaseGeometry))
