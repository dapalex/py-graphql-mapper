
from enum import Enum

class ArgType(Enum):
    LiteralValues = 0,
    Variables = 1

class OperationType(Enum):
    query = 0,
    mutation = 1,
    genericType = 2
