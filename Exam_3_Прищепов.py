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


class Mathematics(ABC):

    @abstractmethod
    def figure_area(self):
        pass

class Figure(Mathematics):

    def __init__(self,radius=None,lenth_1=None,lenth_2=None):
        self.radius = radius
        self.lenth_1 = lenth_1
        self.lenth_2 = lenth_2


class Circle(Figure):

    def __init__(self,radius,lenth_1,lenth_2):
        super().__init__(radius, lenth_1,lenth_2)

    def figure_area(self):
        return round(self.radius * pi, 2)

class Square(Figure):

    def __init__(self,radius,lenth_1,lenth_2):
        super().__init__(lenth_1, radius, lenth_2)

    def figure_area(self):
        return self.lenth_1**2

class Rectangle(Figure):

    def __init__(self,radius,lenth_1,lenth_2):
        super().__init__(radius, lenth_1, lenth_2)

    def figure_area(self):
        return self.lenth_1 * self.lenth_2

# не получилось вводить атрибутов разное количество в разных объектах
square = Square(4)
rectangle = Rectangle(2,6)
circle = Circle(3)

figurs = [square, rectangle, circle]

for i in figurs:
    print(i.figure_area())






