from .enums import TypeKind
from .base_class import SchemaTypeManager

class SCEnumValue():
    name: str
    description: str
    isDeprecated: bool

class SCOfType(SchemaTypeManager):
    kind: str
    name: str
    ofType: any #SCOfType

class SCArgType(SchemaTypeManager):
    kind: TypeKind
    name: str
    ofType: SCOfType

class SCArg(SchemaTypeManager):
    name: str
    description: str
    type: SCArgType

class SCFieldType(SchemaTypeManager):
    kind: str
    ofType: SCOfType

class SCField(SchemaTypeManager):
    name: str
    description: str
    args: list[SCArg]
    type: SCFieldType
    isDeprecated: bool

class SCInterface(SchemaTypeManager):
    kind: TypeKind
    name: str
    ofType: SCOfType

class SCInputField(SchemaTypeManager):
    name: str
    description: str
    type: SCInterface
    defaultValue: str

class SCType(SchemaTypeManager):
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


