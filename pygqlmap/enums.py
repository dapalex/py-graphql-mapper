
from enum import Enum

class ArgType(Enum):
    LITERAL_VALUES = 0
    VARIABLES = 1

class OperationType(Enum):
    QUERY = "query"
    MUTATION = "mutation"
    GENERIC_TYPE = "generic"
