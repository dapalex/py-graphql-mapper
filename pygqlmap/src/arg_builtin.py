
from dataclasses import dataclass
from .gql_init import _sub_class_init

class ArguedBuiltin():
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = _sub_class_init

class ArguedInt(ArguedBuiltin, int):

    def __new__(cls, number):
        arguedInt = super().__new__(cls, number)
        return arguedInt

class ArguedStr(ArguedBuiltin, str):

    def __new__(cls, *args, **kw):
        return str.__new__(cls, *args, **kw)

class ArguedBool(ArguedBuiltin):

    self = False

class ArguedFloat(ArguedBuiltin, float):

    def __init__(self,value): #Constructor like method
        self.value = value

    def __add__(self, other): #rounds results to the higher number of decimal places
        return round(self.value +other.value, max(self.count_decimal_places(self.value), self.count_decimal_places(other.value)))