from dataclasses import dataclass
from pygqlmap.src.gqlObjectInit import operationInit, subClassInit
from .src.components import FSTree # GQLEdge,
from .src.base import FieldsShow, GQLExporter, GQLBaseArgsSet
from .src.consts import commaConcat, argsDeclaration
from .src.utils import getObjectClassName, redirectOutputToFile, restoreOutput, primitives
from .enums import ArgType, OperationType
from .src.translator import Translate

class GQLOperationArgs(GQLBaseArgsSet):
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = subClassInit

    def setArgKey(self, fieldName, fieldValue):
        output = '$' + Translate.toGraphQLFieldName(fieldName)
        if not fieldValue is None: output += ': ' + Translate.toGraphQLType(fieldValue)
        output += commaConcat
        return output

    @property
    def exportGQLArgKeys(self):
        """ For internal use only """
        output = ''
        try:
            for field in self.__dataclass_fields__:
                try:
                    output += self.setArgKey(field, getattr(self, field))
                except:
                    raise Exception('Issue exporting arg key for: ' + field)
                
                output.removesuffix(commaConcat)
        except Exception as ex:
            raise Exception('Issue with items exporting arg keys: ' + ex.args[0])

        return output

    @property
    def exportGQLVariables(self):
        """Return the json variables to send to a server

        Returns:
            str: json variables exported
        """
        output = ''
        try:
            for field in self.__dataclass_fields__:
                try:
                    output += ', ' if output.startswith('{') else '{ '
                    output += '\"' + Translate.toGraphQLFieldName(field) +  '\"'

                    if not getattr(self, field) is None:  output += ': ' + Translate.toGraphQLValue(getattr(self, field))
                except:
                    raise Exception('Issue exporting variable for: ' + field)
        except:
            raise Exception('Issue with items exporting variable')

        output += ' }'
        return output

class GQLArgsSet(GQLBaseArgsSet):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = subClassInit

    def setArgKey(self, fieldName, fieldValue):
        """ For internal use only """
        output = Translate.toGraphQLFieldName(fieldName) + ': $' + Translate.toGraphQLFieldName(fieldName)
        output += commaConcat
        return output

    @property
    def exportGQLArgsAndValues(self):
        """ For internal use only """
        return Translate.toGraphQLDefinition(self, self._argsType)

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
    obj: any
    fieldShowTree: FSTree

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
        self.obj = dataType
        dataType._argsType = self._argsType

        self.propagateArgsType()

        self.fieldsShowTree = FSTree(self.obj)
        self.logProgress = False

    def propagateArgsType(self, obj = None):
        try:
            currentObj = self.obj if obj == None else obj

            if hasattr(currentObj, argsDeclaration):
                currentObj._args._argsType = self._argsType

            if type(currentObj) in primitives or not hasattr(currentObj, '__dataclass_fields__'):
                return

            for subObj in currentObj.__dataclass_fields__:
                if type(getattr(currentObj, subObj)) in primitives or subObj == argsDeclaration:
                    continue
                self.propagateArgsType(getattr(currentObj, subObj))
        except Exception as ex:
            raise Exception('Error during args type propagation - ' + ex.args[0])

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
            raise Exception('setShow accepts only ''str'' or ''list'' types') ##why not throwing?

    @property
    def exportGqlSource(self):
        """Return the GraphQL syntax for the current operation

        Returns:
            str: GraphQL Query exported
        """
        try:
            prefix = self.operationType.name + ' ' + self.name + ' '
            self.obj.logProgress = self.logProgress

            # rootName = self.rootName if self.rootName else getClassName(self.obj)
            rootName = getObjectClassName(self.obj)

            if hasattr(self, argsDeclaration):
                if self._argsType == ArgType.Variables:
                    prefix += '(' + self._args.exportGQLArgKeys + ')'

            return prefix + ' { ' + rootName + self.obj.exportGqlSource[0] + ' } '
        except Exception as ex:
            raise Exception('Issue during export of ' + self.name + ' - ' + ex.args[0])

class GQLQuery(GQLOperation):
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = operationInit

    def __init__(self):
        if hasattr(self, 'args'):
            self._args = self.args
        super().__init__(OperationType.query, self.type, ArgType.LiteralValues)

class GQLMutation(GQLOperation):
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = operationInit

    # def __init__(self):
    #     if hasattr(self, 'args'):
    #         self._args = self.args
    #     super().__init__(operationType=OperationType.mutation, dataType=self.type, argsType=ArgType.LiteralValues)

