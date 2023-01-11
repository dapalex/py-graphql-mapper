
from enum import Enum

class BuildingType(Enum):
    STANDARD = 0, #just keeps the hidden fields present with value None
    ALTERCLASS = 1, #Standard + modify __dict__/__get__ (__set__ __delete__??) to not allow working with it
    CREATENEWCLASS = 2 #Needs to create a new type