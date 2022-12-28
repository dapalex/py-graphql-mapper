from dataclasses import dataclass

from pygqlmap.helper import ManageException
from .src.gqlInit import subClassInit
from .src.components import FSTree
from .src.base import FieldsShow, GQLExporter, GQLBaseArgsSet
from .src.consts import commaConcat, argsDeclaration
from .src.utils import getObjectClassName, primitives, isEmptyField
from .enums import ArgType, OperationType
from .src.translator import Translate

class GQLOperationArgs(GQLBaseArgsSet):
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = subClassInit

    def exportArgKey(self, fieldName, fieldValue):
        return '$' + Translate.toGraphQLFieldName(fieldName) + ': ' + Translate.toGraphQLType(fieldValue)

    @property
    def exportGQLVariables(self):
        """Return the json variables to send to a server

        Returns:
            str: json variables exported
        """
        output = ''
        try:
            for field in self.__dataclass_fields__:
                if isEmptyField(getattr(self, field)): continue
                try:
                    output += ', ' if output.startswith('{') else '{ '
                    output += '\"' + Translate.toGraphQLFieldName(field) +  '\"'

                    if not getattr(self, field) is None:  output += ': ' + Translate.toGraphQLValue(getattr(self, field))
                except:
                    raise Exception('Issue exporting variable for: ' + field)
                
            output.removesuffix(commaConcat)
        except:
            raise ManageException(None, 'Issue with items exporting variable')

        output += ' }'
        return output

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

class GQLOperation(GQLExporter):
    name: str
    operationType: OperationType
    fieldShowTree: FSTree
    argumentsRetrieved: False

    def __init__(self, operationType: OperationType, dataType, operationName: str = None, argsType: ArgType = ArgType.LiteralValues): #, rootName: str = None, inputFieldName: str = None
        """_summary_

        Args:
            operationType (OperationType): _description_
            dataType (_type_): _description_
            hasArgsAsInput (bool, optional): _description_. Defaults to True.
            name (str, optional): _description_. Defaults to 'myQuery'.
            logProgress (bool, optional): _description_. Defaults to False.

        Raises:
            Exception: _description_
        """
        self.name = operationName if operationName else ''

        self.operationType = operationType
        self._argsType = argsType
        self.fieldsShowTree = FSTree(self.type)
        self.logProgress = False

    def setShow(self, keys: str or list[str], isVisible: bool):
        """_summary_

        Args:
            keys (strorlist[str]): GraphQL field path or list of GraphQL field paths
            isVisible (bool): set visibility (default at true)

        Raises:
            Exception: _description_
        """
        kType = type(keys)
        if kType == str:
            self.fieldsShowTree.setFieldShow(keys, isVisible)
        elif kType == list:
            print('list of keys with same value')
            for key in keys:
                self.fieldsShowTree.setFieldShow(key, isVisible)
        else:
            raise ManageException(None, 'setShow accepts only ''str'' or ''list'' types') ##why not throwing?

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
            self.propagateArgsType(self.type)
            rootName = getObjectClassName(self)
            # self.setArgsLocations(self.type, None, rootName, '')

            if self._argsType == ArgType.Variables:
                self.argumentsRetrieved = self.retrieveArgs(self.type)
                if hasattr(self, argsDeclaration):
                    prefix += '(' + self._args.exportGQLArgKeys + ')'
                    
            return prefix + ' { ' + rootName + self.type.exportGqlSource + ' } '
        except Exception as ex:
            raise ManageException(ex, 'Issue during export of ' + self.name)

    @property
    def exportGQLVariables(self):
        """Return the json variables to send to a server

        Returns:
            str: json variables exported 
        """
        if self._args:
            return  self._args.exportGQLVariables
        else:
            raise Exception('No variables to export')

    def retrieveArgs(self, currentObj) -> bool:
        try:
            #if obj contains field with arg name, add arg
            if type(currentObj) in primitives or not hasattr(currentObj, '__dataclass_fields__'):
                return

            if hasattr(currentObj, argsDeclaration):
                currentObjArgs = getattr(currentObj, argsDeclaration)
                for argument in currentObjArgs.__dataclass_fields__:
                    setattr(self, argument, getattr(currentObjArgs, argument))

            for subObj in currentObj.__dataclass_fields__:
                if subObj == argsDeclaration: continue
                self.retrieveArgs(getattr(currentObj, subObj))
        
            return True
        except Exception as ex:
            raise ManageException(ex, 'Error during args type propagation - ')

    def propagateArgsType(self, currentObj):
        try:
            #if obj contains field with arg name, add arg
            if type(currentObj) in primitives or not hasattr(currentObj, '__dataclass_fields__'):
                return

            if hasattr(currentObj, argsDeclaration):
                currentObj._args._argsType = self._argsType

            for subObj in currentObj.__dataclass_fields__:
                if subObj == argsDeclaration:  continue
                self.propagateArgsType(getattr(currentObj, subObj))
        except Exception as ex:
            raise ManageException(ex, 'Error during args type propagation - ')

    # def setArgsLocations(self, currentObj, parentName, fieldName, currentLocation):
    #     try:
    #         #if obj contains field with arg name, add arg
    #         if type(currentObj) in primitives: return

            
    #         currentLocation += '.' + fieldName
    #         if hasattr(currentObj, argsDeclaration):
    #             currentObj._args.location = currentLocation

    #         if GQLObject in inspect.getmro(type(currentObj)):
    #             for subObj in currentObj.__dataclass_fields__:
    #                     self.setArgsLocations(getattr(currentObj, subObj), fieldName, subObj, currentLocation)
    #     except Exception as ex:
    #         raise Exception('Error during args type propagation - ' + ex.args[0])
