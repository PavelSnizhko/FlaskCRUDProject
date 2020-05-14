from injector import singleton

from models.parser import Parser

def configure(binder):
    binder.bind(Parser, to=Parser, scope=singleton)