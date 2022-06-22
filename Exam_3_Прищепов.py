# # exam_3_1
#
# def card_hide(number):
#
#     a = number % 10000
#     print("*" * 12, a, sep="")
#
# card_hide (5456789515658562)

# # exam_3_2
#
# word = input()
# def is_palindrome(word1):
#
#     return word1 == word1[::-1]
#
# print(is_palindrome(word))

# exam 3_3
from math import pi
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def figure_area(self):
        pass

class Circle(Figure):

    def __init__(self,radius):
        self.radius = radius

    def figure_area(self):
        return round(self.radius**2 * pi, 2)

class Square(Figure):

    def __init__(self, length):
        self.length = length

    def figure_area(self):
        return self.length**2

class Rectangle(Figure):

    def __init__(self,length1,length2 ):
        self.length1 = length1
        self.length2 = length2

    def figure_area(self):
        return self.length1 * self.length2

square = Square(4)
rectangle = Rectangle(2,6)
circle = Circle(3)

figurs = [square, rectangle, circle]

for i in figurs:
    print(i.figure_area())






