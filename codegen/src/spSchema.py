from .enums import TypeKind
from .baseClass import TypeManager

class SCEnumValue():
    name: str
    description: str
    isDeprecated: bool

class SCOfType(TypeManager):
    kind: str
    name: str
    ofType: any #SCOfType || SCType

class SCArgType(TypeManager):
    kind: TypeKind
    name: str
    ofType: SCOfType

class SCArg(TypeManager):
    name: str
    description: str
    type: SCArgType

class SCFieldType(TypeManager):
    kind: str
    ofType: SCOfType

class SCField(TypeManager):
    name: str
    description: str
    args: list[SCArg]
    type: SCFieldType
    isDeprecated: bool

class SCInterface(TypeManager):
    kind: TypeKind
    name: str
    ofType: SCOfType

class SCInputField(TypeManager):
    name: str
    description: str
    type: SCInterface
    defaultValue: str

class SCType(TypeManager):
    kind: str
    name: str
    description: str
    ofType: SCOfType
    fields: list[SCField]
    interfaces: list[SCInterface]
    enumValues: list[SCEnumValue]
    possibleTypes: list['SCType']
    inputFields: list[SCInputField]

class SCOperationType():
    name: str

class SCDirective():
    name: str
    description: str
    locations: list[str]
    args: list[SCArg]

class GQLSchema():
    types: dict[str, SCType]
    directives: list[SCDirective]
    queryType: SCOperationType = SCOperationType()
    mutationType: SCOperationType = SCOperationType()
    subscriptionType: SCOperationType = SCOperationType()


