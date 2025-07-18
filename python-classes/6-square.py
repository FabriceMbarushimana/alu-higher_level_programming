#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    Creates a square class.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of variables."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Accesssize."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0, position=(0, 0)):
        """Initializetion of data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """check condition and set  position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for n in range(self.__size):
                for m in range(self.__position[0]):
                    print(' ', end="")
                for o in range(self.__size):
                    print("#", end="")
                print()
