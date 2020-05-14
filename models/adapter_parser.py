from __future__ import annotations
from models.service import CalculateService
from models.parser import Parser
from models.observer import Observable
from injector import inject, Module, InstanceProvider, BoundKey, Injector, ClassProvider, SingletonScope
import importlib



class AdapterPolygon(Observable, Module):
    @inject
    def __init__(self, parser: Parser):
        super().__init__()
        self.parser = parser




    def get_polygon(self, arg_string):
        """Get class using reflection and Dependency Injection with API Injector"""


        self.parser.set_string(arg_string)
        arguments = self.parser.argument_parser().get_arguments()

        # instead of abstract fabric have used reflection and assential injection
        TypePolygon = getattr(importlib.import_module("models.type_polygons"), arguments[0])
        InjectedPolygon = BoundKey(TypePolygon, x=InstanceProvider(arguments[1]), y=InstanceProvider(arguments[2]), side=InstanceProvider(arguments[3]),
                                  n=InstanceProvider(arguments[4]))

        injector = Injector()
        polygon = injector.get(InjectedPolygon)

        self.notify_observer(polygon)
        return polygon

