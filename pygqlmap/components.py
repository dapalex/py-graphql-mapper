from dataclasses import dataclass
from .helper import HandleRecursiveEx
from .src.gqlInit import subClassInit
from .src.components import FSTree
from .src.base import FieldsShow, GQLExporter, GQLBaseArgsSet
from .src.consts import commaConcat, argsDeclaration
from .src.utils import getObjectClassName, primitives, isEmptyField
from .enums import ArgType, OperationType
from .src.translator import Translate

class GQLOperationArgs(GQLBaseArgsSet):
    
    @property
    def exportGQLArgKeys(self):
       
        """ For internal use only """
        output = ''
        try: 
            for fieldName, fieldValue in self.arguments.items():
                if isEmptyField(fieldValue): continue
                try:  
                    output += self.exportArgKey(fieldName, fieldValue) + commaConcat
                except Exception as ex:
                    raise HandleRecursiveEx(ex, 'Issue exporting arg key for: ' + fieldName)
        
            output = output.removesuffix(commaConcat)
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Issue exporting arg keys')

        return output
    
    @property
    def exportGQLVariables(self):
        """Return the json variables to send to a server

        Returns:
            str: json variables exported
        """
        if self._argsType == ArgType.Variables:
            if self.arguments:
                return Translate.toJsonVariables(self.arguments)
        
    def exportArgKey(self, fieldName, fieldValue):
        return '$' + Translate.toGraphQLFieldName(fieldName) + ': ' + Translate.toGraphQLType(fieldValue)

class GQLArgsSet(GQLBaseArgsSet):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = subClassInit

    def exportArgKey(self, fieldName, fieldValue):
        """ For internal use only """
        return Translate.toGraphQLFieldName(fieldName) + ': $' + Translate.toGraphQLFieldName(fieldName)

    @property
    def exportGQLArgsAndValues(self):
        """ For internal use only """
        return Translate.toGraphQLArgsSetDefinition(self)

@dataclass
class GQLObject(FieldsShow, GQLExporter):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = subClassInit

    def __post_init__(self, logProgress: bool = False):
        self.initFieldsShow() ##still working???
        self.logProgress = logProgress

class GQLOperation(GQLExporter, GQLOperationArgs):
    name: str
    operationType: OperationType
    fieldShowTree: FSTree
    # argumentsRetrieved: False

    def __init__(self, operationType: OperationType, dataType, operationName: str = None, argsType: ArgType = ArgType.LiteralValues): #, rootName: str = None, inputFieldName: str = None
        """_summary_

        Args:
            operationType (OperationType): _description_
            hasArgsAsInput (bool, optional): _description_. Defaults to True.
            name (str, optional): _description_. Defaults to 'myQuery'.
            logProgress (bool, optional): _description_. Defaults to False.
        """
        self.name = operationName if operationName else ''

        self.operationType = operationType
        self.type = dataType
        self._argsType = argsType
        self.fieldsShowTree = FSTree(self.type, getObjectClassName(self))
        self.logProgress = False

    def setShow(self, keys: str or list[str], isVisible: bool):
        """_summary_

        Args:
            keys (strorlist[str]): GraphQL field path or list of GraphQL field paths
            isVisible (bool): set visibility (default at true)

        Raises:
            Exception: keys not string or list of strings
        """
        kType = type(keys)
        if kType == str:
            self.fieldsShowTree.setFieldShow(keys, isVisible)
        elif kType == list:
            print('list of keys with same value')
            for key in keys:
                self.fieldsShowTree.setFieldShow(key, isVisible)

    @property
    def exportGqlSource(self):
        """Return the GraphQL syntax for the current operation

        Returns:
            str: GraphQL Query exported
        """
        try:
            prefix = self.operationType.name + ' ' + self.name + ' '
            self.type.logProgress = self.logProgress

            ##Arguments of the operation are arguments of the root object
            if hasattr(self, argsDeclaration):
                setattr(self.type, argsDeclaration, getattr(self, argsDeclaration))
            
            #Update all objects args with the argument type requested
            self.manageArgs(self.type)
            rootName = getObjectClassName(self)
            # self.setArgsLocations(self.type, None, rootName, '')

            if self._argsType == ArgType.Variables:
                # self.argumentsRetrieved = self.retrieveArgs(self.type)
                if hasattr(self, argsDeclaration) and self.arguments:
                    prefix += '(' + self.exportGQLArgKeys + ')'
                    
            return prefix + ' { ' + rootName + self.type.exportGqlSource + ' } '
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Issue during export of ' + self.name)

    arguments: dict = None

    def manageArgs(self, currentObj):
        if not self.arguments: self.arguments = {}
        try:
            #if obj contains field with arg name, add arg
            if type(currentObj) in primitives or not hasattr(currentObj, '__dataclass_fields__'):
                return

            if hasattr(currentObj, argsDeclaration):
                currentObj._args._argsType = self._argsType
                for arg in currentObj._args.__dataclass_fields__:
                    argValue = getattr(currentObj._args, arg)
                    if isEmptyField(argValue): continue
                    self.arguments.update({arg: argValue})
                    
            for subObj in currentObj.__dataclass_fields__:
                if subObj == argsDeclaration:  continue
                self.manageArgs(getattr(currentObj, subObj))
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Error during args type propagation - ')
