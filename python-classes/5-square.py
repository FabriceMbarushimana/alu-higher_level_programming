#!/usr/bin/python3
"""We don't need module"""


class Square:
    """ Define class that represents a square class """
    def __init__(self, size=0):
        """Initialization a new instance of class. """
        self.size = size

    @property
    def size(self):
        """
        Method to retrieve the size of the square
        .
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define method to set the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
