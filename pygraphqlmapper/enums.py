
from enum import Enum

class ArgType(Enum):
    EmbeddedArgs = 0,
    Variables = 1

class ArgLocation(Enum):
    Operation = 0,
    Data = 1

class OperationType(Enum):
    query = 0,
    mutation = 1

class BuildingType(Enum):
    Standard = 0, #just keeps the hidden fields present with value None
    AlterClass = 1, #Standard + modify __dict__/__get__ (__set__ __delete__??) to not allow working with it
    CreateNewClass = 2 #Needs to create a new type