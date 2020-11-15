from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * pi * self.radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width


def print_info(shape: Shape):
    return f'Perimeter: {shape.calculate_perimeter()}\n' \
           f'Area: {shape.calculate_area()}'
