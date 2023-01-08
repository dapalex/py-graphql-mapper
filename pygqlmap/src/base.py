from abc import ABC, abstractmethod
from dataclasses import asdict
import inspect
import logging as logger

from pygqlmap.helper import HandleRecursiveEx
from .consts import commaConcat, argsDeclaration
from ..enums import ArgType

from .utils import getObjectClassName, isEmptyField
from .translator import Translate

class FieldsShow(ABC):
    
    @property
    def fieldsShow(self):
        return self._fieldsShow
    
    def initFieldsShow(self):
        """ For internal use only """
        try:
            self._fieldsShow = asdict(self)
            try:
                for field in self._fieldsShow:
                    self._fieldsShow[field] = True
            except Exception as ex:
               raise HandleRecursiveEx(ex, 'Error during fieldShow initialization for field ' + field)
        except Exception as ex:
           raise HandleRecursiveEx(ex, 'Error during fieldShow initialization')
        
    def copyFieldsShow(self, fieldsShow):
        """ For internal use only """
        self._fieldsShow = fieldsShow
        
class GQLExporter():                

    logProgress: bool
    
    @property
    def exportGqlSource(self):
        gqlArgs, outputGqlDict = self.exportGqlDict
        return gqlArgs + ' { ' + Translate.graphQLize(outputGqlDict) + ' } '
    
    @property
    def exportGqlDict(self):
        """Return the GraphQL syntax for the current object

        Returns:
            str: GraphQL object exported 
        """
        if hasattr(self, 'logProgress') and self.logProgress: logger.info('Started GQL extraction of python: ' + getObjectClassName(self))
        
        gqlDict = asdict(self) 
        outputGqlDict = {}
        
        from pygqlmap.src.gqlArgBuiltin import ArguedBuiltin
        try:
            for field in gqlDict.keys():
                try:
                    if field == argsDeclaration: continue
                    if self.fieldsShow[field]:
                        fieldObject = getattr(self, field)
                        if FieldsShow in inspect.getmro(type(fieldObject)):
                            outputGqlDict[field] = fieldObject.exportGqlDict
                        elif ArguedBuiltin in inspect.getmro(type(fieldObject)):
                                builtinArgs = fieldObject._args.exportArgs
                                outputGqlDict[Translate.toGraphQLFieldName(field)] = builtinArgs, Translate.toGraphQLFieldName(field)
                        else:
                            if not fieldObject == None:
                                outputGqlDict[Translate.toGraphQLFieldName(field)] = fieldObject
                            
                except Exception as ex:
                    raise HandleRecursiveEx(ex, 'Issue exporting field ' + self.__class__.__name__ + '.' + field)
            
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Issue during export of gql dictionary')
        
        gqlArgs = ''
        #Arguments management START - after check of fields requested
        if hasattr(self, argsDeclaration): 
            try:
                if hasattr(self, 'logProgress') and self.logProgress: logger.info('Started GQL extraction of args for: ' + getObjectClassName(self))
                gqlArgs = self._args.exportArgs
            except Exception as ex:
                raise HandleRecursiveEx(ex, 'Issue exporting _args for ' + str(self.__class__.__name__))
            
        #Arguments management END
            
        if len(gqlArgs) == 0 and len(outputGqlDict) == 0: 
            return None, None
        
        return gqlArgs, outputGqlDict

class GQLBaseArgsSet():
    
    @abstractmethod
    def exportArgKey(self, fieldName, fieldValue):
        """ For internal use only """
        raise HandleRecursiveEx(message='exportArg function not implemented')
    
    @property
    def exportArgs(self):
        arguments = ''
        try:
            if self._argsType == ArgType.LiteralValues:
                    arguments = self.exportGQLArgsAndValues
                    if len(arguments) > 0:
                        return '(' + arguments + ')'
            elif self._argsType == ArgType.Variables:
                        arguments = self.exportGQLArgKeys
                        if len(arguments) > 0:
                            return '(' + arguments + ')'
            else:
                raise HandleRecursiveEx(message='No valid argType for ')
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Issue during export arguments for ' + self.__class__.__name__)
        
        return arguments
    
    @property
    def exportGQLArgKeys(self):
        """ For internal use only """
        output = ''
        try: 
            for field in self.__dataclass_fields__:
                if isEmptyField(getattr(self, field)): continue
                try:  
                    output += self.exportArgKey(field, getattr(self, field)) + commaConcat
                except:
                    raise HandleRecursiveEx(message='Issue exporting arg key for: ' + field)
        
            output = output.removesuffix(commaConcat)
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Issue exporting arg keys for ' + str(self.__class__))

        return output
