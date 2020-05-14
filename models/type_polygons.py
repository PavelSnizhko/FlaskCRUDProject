from abc import ABCMeta, abstractmethod

from injector import inject

from models.point import Point


class IPolygon(Point, metaclass=ABCMeta):
    def __init__(self, x, y, side, n):
        super().__init__(x, y)
        self.side = side
        self.n = n

    @abstractmethod
    def get_type(self):
        """The Polygon interface """

    @property
    def get_side(self):
        return self.side

    @property
    def get_n(self):
        return self.n

    def set_side(self, side):
        self.side = side


class Triangle(IPolygon):

    def get_type(self):
        return "Triangle"


class Pentagon(IPolygon):

    def get_type(self):
        return "Pentagon"


class Rectangle(IPolygon):

    def get_type(self):
        return "Rectangle"
