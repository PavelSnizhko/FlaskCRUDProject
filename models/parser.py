from __future__ import annotations
import re
from math import fabs, tan

from typing import Optional

from injector import singleton, provider


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Parser] = None

    def __call__(self, string) -> Parser:
        if self._instance is None:
            self._instance = super().__call__(string)
        return self._instance


class Parser(object):
    def __init__(self):
        self.__input = ""
        self.__is_parsed = False
        self.__was_error = False
        self.__error_message = ""
        self.__arguments = []
        self.__name_polygon = ""


    def set_string(self, string):
        self.__input = string

    def argument_parser(self):
        try:
            arguments_ = [val for val in self.__input.split(" ")]
            self.__name_polygon = arguments_.pop(0)
            self.__arguments = [int(val) for val in arguments_]
            self.__is_parsed = True
        except:
            self.__was_error = True
            self.__error_message = "Error! Can't be parsed"
        return self

    def get_was_error(self):
        return self.__was_error

    def get_error_message(self):
        return self.__error_message

    def get_arguments(self):
        if self.__is_parsed:
            return self.__name_polygon, self.__arguments[0], self.__arguments[1], \
                   self.__arguments[2], self.__arguments[3]
        raise Exception
    def get_data(self):
        return "ok"

# class ParserModule(Module):
#
#     def configure(self, binder):
#         binder.bind(Parser, scope=singleton)
#
#     @singleton
#     @provider
#     def provide_thing(self) -> Parser:
#         return Parser()
