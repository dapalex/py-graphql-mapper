from abc import ABC, abstractmethod
from dataclasses import asdict
import inspect
from .consts import commaConcat, argsDeclaration
from ..enums import ArgType
from .logger import Logger
from .utils import getObjectClassName, isEmptyField
from .translator import Translate

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

    # gqlExportedTuple = () #base class
    gqlExportedArgs = set() #base class
    logProgress: bool
    
    @property
    def exportGqlSource(self):
        """Return the GraphQL syntax for the current object

        Returns:
            str: GraphQL object exported 
        """
        print('Starting ' + self.__class__.__name__)
        if hasattr(self, 'logProgress') and self.logProgress: Logger.logInfoMessage('Started GQL extraction of python: ' + getObjectClassName(self))
        
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
                            
                            # outputGqlDict[field], tempExportedArgsTuple = fieldObject.exportGqlSource
                            # self.gqlExportedArgsTuple = mergeTupleUniqueArguments(self.gqlExportedArgsTuple, tempExportedArgsTuple)
                            outputGqlDict[field], tempExportedArgs = fieldObject.exportGqlSource
                            if tempExportedArgs: self.gqlExportedArgs = self.gqlExportedArgs.union(tempExportedArgs)
                        elif ArguedBuiltin in inspect.getmro(type(fieldObject)):
                                builtinArgs = fieldObject._args.exportArgs
                                outputGqlDict[Translate.toGraphQLFieldName(field)] = Translate.toGraphQLFieldName(field) + builtinArgs
                                # if len(builtinArgs) > 0: self.gqlExportedArgsTuple = addTupleUniqueArgument(self.gqlExportedArgsTuple, builtinArgs, fieldObject._args.location)
                                if len(builtinArgs) > 0: self.gqlExportedArgs.add(builtinArgs)
                        else:
                            outputGqlDict[Translate.toGraphQLFieldName(field)] = fieldObject
                            
                except Exception as ex:
                    raise Exception('Issue exporting field ' + self.__class__.__name__ + '.' + field + " - " + ex.args[0])
            
        except Exception as ex:
            raise ex
        
        gqlArgs = ''
        #Arguments management START - after check of fields requested
        if hasattr(self, argsDeclaration): 
            try:
                if hasattr(self, 'logProgress') and self.logProgress: Logger.logInfoMessage('Started GQL extraction of args for: ' + getObjectClassName(self))
                gqlArgs = self._args.exportArgs
            except Exception as ex:
                raise Exception('Issue exporting _args for ' + str(self.__class__.__name__) + " - " + ex.args[0])
            
            # if len(gqlArgs) > 0: self.gqlExportedArgsTuple = addTupleUniqueArgument(self.gqlExportedArgsTuple, gqlArgs, self._args.location)
            if len(gqlArgs) > 0: self.gqlExportedArgs.add(gqlArgs)
                        
        #Arguments management START
            
        if len(outputGqlDict) == 0 and len(gqlArgs) == 0: 
            # return '', self.gqlExportedArgsTuple
            return '', self.gqlExportedArgs
        
        gqlResult = gqlArgs + (Translate.graphQLize(str(outputGqlDict), self.gqlExportedArgs) if outputGqlDict else '') # + str(translatedGqlDict)
        
        print('Ending ' + self.__class__.__name__)
        # return gqlResult, self.gqlExportedArgsTuple
        return gqlResult, self.gqlExportedArgs
    
class GQLBaseArgsSet():
    
    @abstractmethod
    def exportArgKey(self, fieldName, fieldValue):
        """ For internal use only """
        raise Exception('exportArg function not implemented')
    
    @property
    def exportArgs(self):
        arguments = ''
        try:
            if self._argsType == ArgType.LiteralValues:
                    arguments = self.exportGQLArgsAndValues
                    if len(arguments) > 0:
                        return '(' + arguments + ')'
            elif self._args._argsType == ArgType.Variables:
                        arguments = self.exportGQLArgKeys
                        if len(arguments) > 0:
                            return '(' + arguments + ')'
            else:
                raise Exception('No valid argType for ')
        except Exception as ex:
            raise ex
        
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
                    raise Exception('Issue exporting arg key for: ' + field + " - " + ex.args[0])
        
            output = output.removesuffix(commaConcat)
        except Exception as ex:
            raise Exception('Issue exporting arg keys for ' + str(self.__class__) + " - " + ex.args[0])

        return output
