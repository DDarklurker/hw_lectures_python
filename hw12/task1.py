# task1
"""
Написати програму Що складає, віднімає, робить скалярний і векторний додаток над векторами
асерти пишите самі
"""
from typing import Union

#task2
"""
Реальзувати метод підрахунку довжин ліній. зробити метод компаре, який буде зрівнювати лінії і казатит яка довша
"""
from math import sqrt

Point = [int, int]

"""
"""


class Line():

    def __init__(self, point1: Point, point2: Point, point3=0):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    def __add__(self, other: 'Line') -> 'Line':
        return Line(self.calc_vector().p1 + other.calc_vector().p1, self.calc_vector().p2 + other.calc_vector().p2, 0)

    def __sub__(self, other: 'Line') -> 'Line':
        return Line(self.calc_vector().p1 - other.calc_vector().p1, self.calc_vector().p2 - other.calc_vector().p2, 0)

    def __mul__(self, other: 'Line') -> Union[int,float]:
        return self.calc_vector().p1 * other.calc_vector().p1 + self.calc_vector().p2 * other.calc_vector().p2

    def compare(self, other: 'Line') -> str:
        if self.length_line() > other.length_line():
            return "Перша лінія довша"
        elif self.length_line() < other.length_line():
            return  "Друга лінія довша"
        else:
            "Лінії рівні"

    def calc_vect_dob(self, other: 'Line') -> 'Line':
        return Line((self.calc_vector().p2 * other.calc_vector().p3 - self.calc_vector().p3 * other.calc_vector().p2), (
                self.calc_vector().p1 * other.calc_vector().p3 - self.calc_vector().p3 * other.calc_vector().p1), (
                            self.calc_vector().p1 * other.calc_vector().p2 - self.calc_vector().p2 * other.calc_vector().p1))

    def length_line(self) -> Union[int,float]:
        return  sqrt(self.calc_vector().p1**2+self.calc_vector().p2**2)

    def calc_vector(self) -> 'Line':
        return Line(self.p2.x - self.p1.x, self.p2.y - self.p1.y, 0)

    def calc_slope(self) -> Union[int,float]:
        return (self.p1.x - self.p2.x) / (self.p1.y - self.p2.y)

    def is_on_line(self, p3: 'Point') -> bool:
        if self.calc_slope() == Line(self.p1, p3).calc_slope():
            return True
        else:
            return False


class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


p1 = Point(3, 6)
p2 = Point(5, 9)
p3 = Point(2, 7)
p4 = Point(5, 10)
line1 = Line(p1, p2)
line2 = Line(p3, p4)
line3 = Line(line1.__add__(line2).p1, line1.__add__(line2).p2)
line4 = Line(line1.__sub__(line2).p1, line1.__sub__(line2).p2)
line5 = Line(line1.calc_vect_dob(line2).p1, line1.calc_vect_dob(line2).p2, line1.calc_vect_dob(line2).p3)
line = line1.length_line()


assert (line1.__mul__(line2)) == 15
assert (line3.p1, line3.p2) == (5, 6)
assert (line4.p1, line4.p2) == (-1, 0)
assert (line5.p1, line5.p2, line5.p3) == (0, 0, -3)
assert float(f'{line2.length_line():.2f}') == 4.24
assert line1.compare(line2) == 'Друга лінія довша'
