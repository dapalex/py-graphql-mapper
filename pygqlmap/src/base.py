from abc import ABC, abstractmethod
from dataclasses import asdict
import inspect
from .consts import commaConcat
from ..enums import ArgType
from .logger import Logger
from .utils import addTupleUniqueElement, getDotNotationInfo, getClassName, isNoneOrBuiltinPrimitive, mergeTupleUniqueElements
from .translator import Translate

class GQLList(list):
    
    sampleElement: any
    
    def __init__(self, sampleElement=None):
        if sampleElement:
            self.sampleElement = sampleElement
    
class FieldsShow(ABC):
    
    @property
    def fieldsShow(self):
        return self._fieldsShow
    
    def initFieldsShow(self):
        """ For internal use only """
        self._fieldsShow = asdict(self)
        for field in self._fieldsShow:
            self._fieldsShow[field] = True
        
    def copyFieldsShow(self, fieldsShow):
        """ For internal use only """
        self._fieldsShow = fieldsShow
        
class GQLExporter(Logger):                

    gqlExportedArgsTuple = ()
    logProgress: bool
    
    @property
    def exportGqlSource(self):
        """Return the GraphQL syntax for the current object

        Returns:
            str: GraphQL object exported 
        """
        if hasattr(self, 'logProgress') and self.logProgress: Logger.logInfoMessage('Started GQL extraction of python: ' + getClassName(self))
        gqlDict = asdict(self) 
        outputGqlDict = {}
        
        for field in gqlDict.keys():
            if self.fieldsShow[field]:
                if FieldsShow in inspect.getmro(type(getattr(self, field))):
                    
                    outputGqlDict[field], tempExportedArgsTuple = getattr(self, field).exportGqlSource
                    self.gqlExportedArgsTuple = mergeTupleUniqueElements(self.gqlExportedArgsTuple, tempExportedArgsTuple)
                else:
                    outputGqlDict[Translate.toGraphQLFieldName(field)] = getattr(self, field)
        
        if len(outputGqlDict) == 0: return ''
        
        gqlArgs = ''
        #Arguments management START
        if hasattr(self, '_args'): 
            if hasattr(self, 'logProgress') and self.logProgress: Logger.logInfoMessage('Started GQL extraction of args for: ' + getClassName(self))
            if self._argsType == ArgType.LiteralValues:
                 gqlArgs = '(' + self._args.exportGQLArgsAndValues + ')'
            elif self._argsType == ArgType.Variables:
                 gqlArgs = '(' + self._args.exportGQLArgKeys + ')'
            
            self.gqlExportedArgsTuple = addTupleUniqueElement(self.gqlExportedArgsTuple, gqlArgs)
        #Arguments management START
        
        gqlResult = gqlArgs + Translate.graphQLize(str(outputGqlDict), self.gqlExportedArgsTuple) #
        
        return gqlResult, self.gqlExportedArgsTuple
    
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
         
class GQLBaseArgsSet():
    location: str
    arguments: dict
    
    def __init__(self):
        self.arguments = {}
    
    @abstractmethod
    def setArgKey(self, fieldName, fieldValue):
        """ For internal use only """
        raise Exception('setArgKey function not implemented')
    
    @property
    def updateArg(self, key, value):
        """Updates an existing argument

        Args:
            key: name of the argument
            value: value of the argument, it can be a scalar mapped type or a dict for structured objects

        Raises:
            Exception: if key not present
            Exception: if key not valid
        """
        try:
            if key in self.arguments.keys():
                    self.arguments[key] = value
            else:
                raise Exception("Key not present") 
        except:
            raise Exception("Key not valid")            

    @property
    def exportGQLArgKeys(self):
        """ For internal use only """
        output = ''
        try: 
            for argKey, argValue in self.arguments.items():
                try:  
                    output += self.setArgKey(argKey, argValue)
                except:
                    raise Exception('Issue exporting arg key for: ' + argKey, argValue)
        except:
            raise Exception('Issue with items exporting arg keys')
        
        output = output.removesuffix(commaConcat)

        return output
