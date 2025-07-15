#!/usr/bin/python3
"""
Defines a Rectangle class with attributes and methods for geometry operations.
"""

class Rectangle:
    """A class to represent rectangles, tracking active instances."""

    number_of_instances = 0  # Class variable to track active instances

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return a string visualization of the rectangle with '#' characters.

        Returns:
            str: Visual representation or empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Return a string that can be used to recreate this rectangle object.

        Returns:
            str: String in the form 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor called when the instance is deleted.
        Decreases instance count and outputs a message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
