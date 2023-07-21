#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position
    
    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value,tuple): 
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0],int) or not isinstance(position[1],int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))