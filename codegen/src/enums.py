
from enum import Enum

class TypeKind(Enum):
    SCALAR = "SCALAR", #'Indicates this type is a scalar.'
    OBJECT = "OBJECT", #'Indicates this type is an object. `fields` and `interfaces` are valid fields.',
    ENUM = "ENUM", #'Indicates this type is an enum. `enumValues` is a valid field.',
    LIST = "LIST", #'Indicates this type is a list. `ofType` is a valid field.',
    INTERFACE = "INTERFACE", #'Indicates this type is an interface. `fields`, `interfaces`, and `possibleTypes` are valid fields.',
    UNION = "UNION", #'Indicates this type is a union. `possibleTypes` is a valid field.',
    INPUT_OBJECT = "INPUT_OBJECT", #'Indicates this type is an input object. `inputFields` is a valid field.',
    NON_NULL = "NON_NULL" #'Indicates this type is a non-null. `ofType` is a valid field.',
    
class TemplateType(Enum): 
    SCALAR_TEMPLATE = 'scalarTemplate.py'
    ENUM_TEMPLATE = 'enumTemplate.py'
    FREE_TYPE_TEMPLATE = 'simpleTypeTemplate.py'
    QUERY_TEMPLATE = 'queryTemplate.py'
    MUTATION_TEMPLATE = 'mutationTemplate.py'
    TYPE_TEMPLATE = 'typeTemplate.py'
    CIRCULAR_REFS_TEMPLATE = 'circularRefsTemplate.py'
