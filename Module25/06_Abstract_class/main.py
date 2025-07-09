from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """
    Абстрактный класс Shape.
    """
    @abstractmethod
    def area(self) -> None:
        pass


class Circle(Shape):
    """
    Класс Circle. Родительский класс Shape.
    """
    def __init__(self, value):
        self.value: int = value


    def area(self):
        """
        Вычисляет площадь круга.
        :return: площадь круга
        :rtype: float
        """
        return pi * self.value ** 2


class Rectangle(Shape):
    def __init__(self, value_1, value_2):
        self.value_1: int = value_1
        self.value_2: int = value_2


    def area(self):
        return self.value_1 * self.value_2


class Triangle(Shape):
    def __init__(self, value_1, value_2):
        self.value_1: int = value_1
        self.value_2: int = value_2


    def area(self):
        return self.value_1 * self.value_2 / 2


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)


# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()


# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
