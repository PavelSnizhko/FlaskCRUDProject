from abc import ABCMeta, abstractmethod
from math import fabs, tan

from models.observer import Observer


class Command(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def calculate():
        raise NotImplementedError()


class CalculateService(Command, Observer):
    def update(self, obj):
        self.obj = obj

    def calculate(self):
        return self.obj.get_n * self.obj.get_side ** 2 / 4.0 * fabs(tan(180 / float(self.obj.get_n)))


class Decorator(Command, metaclass=ABCMeta):

    def __init__(self, decorated_result) -> None:
        self.decorated_result = decorated_result

    @abstractmethod
    def calculate(self):
        pass


class Meters(Decorator):

    def __init__(self, decorated_result):
        super().__init__(decorated_result)

    def calculate(self):
        return self.decorated_result.calculate() * 0.01
