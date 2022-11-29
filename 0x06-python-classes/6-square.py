#!/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        area = self.__size ** 2
        return (area)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) and type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="") # spaces
                for e in range(self.size):
                    print("#", end="") # hashes
                print("")


my_square_1 = Square(3) 
my_square_1.my_print() 
 
print("--") 
 
my_square_2 = Square(3, (1, 1)) 
my_square_2.my_print() 
 
print("--") 
 
my_square_3 = Square(3, (3, 0)) 
my_square_3.my_print() 
 
print("--") 
