#!/usr/bin/python3
"""We don't need to import module"""


class Square:
    """Define class that represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of class.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates area of the square.
        """
        return self.__size ** 2
