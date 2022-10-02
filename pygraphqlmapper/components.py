from abc import ABC
from dataclasses import asdict
import inspect
from enums import ArgLocation, ArgType
from logger import Logger
from utils import getDotNotationInfo, graphQLize, getClassName, isNoneOrBuiltinPrimitive

class GQLList(list):
    
    sampleElement: any
    
    def __init__(self, sampleElement=None):
        if sampleElement:
            self.sampleElement = sampleElement
    
class FieldsShow(ABC):
    
    @property
    def fieldsShow(self):
        return self._fieldsShow
    
    # @abstractmethod
    def initFieldsShow(self):
        self._fieldsShow = asdict(self)
        for field in self._fieldsShow:
            self._fieldsShow[field] = True
        
    # @abstractmethod
    def copyFieldsShow(self, fieldsShow):
        self._fieldsShow = fieldsShow
        
class GQLExporter():                

    gqlArgsList = []
    logProgress: bool
    
    @property
    def exportGqlSource(self):
        if self.logProgress: Logger.logInfoMessage('Started GQL extraction of python: ' + getClassName(self))
        gqlDict = asdict(self) 
        outputGqlDict = {}
        
        for field in gqlDict.keys():
            if self.fieldsShow[field]:
                if FieldsShow in inspect.getmro(type(getattr(self, field))):
                    outputGqlDict[field], self.gqlArgsList = getattr(self, field).exportGqlSource
                else:
                    outputGqlDict[field] = getattr(self, field)
        
        if len(outputGqlDict) == 0: return ''
        
        gqlArgs = ''
        #Arguments management START
        if hasattr(self, '_args'): 
            if self.logProgress: Logger.logInfoMessage('Started GQL extraction of args for: ' + getClassName(self))
            if self._argsType == ArgType.EmbeddedArgs:
                 gqlArgs = self._args.exportGQLArgsAndValues
            elif self._argsType == ArgType.Variables:
                 gqlArgs = self._args.exportGQLArgKeys
            if not self.gqlArgsList.__contains__(gqlArgs): self.gqlArgsList.append(gqlArgs)
        
        gqlResult = gqlArgs + graphQLize(str(outputGqlDict), self.gqlArgsList) #
        
        return gqlResult, self.gqlArgsList
     
    @property
    def exportGQLVariables(self):
        if self._args:
            return  self._args.exportGQLVariables
        else:
            raise Exception('No variables to export')
         
class GQLBaseArgs():
    location: str
    scope: ArgLocation
    arguments: list
    
    def __init__(self, location=None) -> None:
        self.location = location
        self.arguments = []
    
    @property
    def updateArg(self, key, value):
        try:
            for argument in self.arguments:
                if argument.name == key:
                    argument.value == value
                else:
                    raise Exception("Key not present") 
        except:
            raise Exception("Key not valid")            

    @property
    def exportGQLArgsAndValues(self):
        output = ''
        
        if self.scope == ArgLocation.Data:
            try: 
                for argument in self.arguments:
                    try:
                        output += ', ' if output.startswith('(') else '('

                        output += argument.name
                        if argument.value:
                            if getClassName(argument.value) == 'ID':
                                output += ': \"' + argument.value + '\"'
                            elif type(argument.value) == str:
                                output += ': \"' + argument.value + '\"'
                            elif type(argument.value) == int or type(argument.value) == list:
                                output += ': ' + str(argument.value).replace('\'', '\"')
                            elif type(argument.value) == type:
                                output += ': \"' + str(argument.value).replace('\'', '\"') + '\"'
                    except:
                        raise Exception('Issue exporting arg and value for: ' + argument)
            except:
                raise Exception('Issue with items exporting args and values')

            output += ')'

        return output

    @property
    def exportGQLArgKeys(self):
        output = ''
        try: 
            for argument in self.arguments:
                try: 
                    output += ', ' if output.startswith(' (') else ' ('
                    if self.scope == ArgLocation.Operation:
                        output += '$' + argument.name
                        if argument.value:
                            if type(argument.value) == str:
                                output += ': String'
                            elif type(argument.value) == int:
                                output += ': Int'
                            elif getClassName(argument.value) == 'ID':
                                output += ': ID'
                            elif type(argument.value) == type:
                                output += ': Type'  
                            else:
                                print('type not managed!')
                    elif self.scope == ArgLocation.Data:
                        output += argument.name + ': $' + argument.name
                except:
                    raise Exception('Issue exporting arg key for: ' + argument)
        except:
            raise Exception('Issue with items exporting arg keys')
        output += ')'

        return output

    @property
    def exportGQLVariables(self):
        output = ''
        try: 
            for argument in self.arguments:
                try: 
                    output += ', ' if output.startswith('{') else '{ '

                    output += '\"' + argument.name +  '\"' 
                    if argument.value:
                        if getClassName(argument.value) == 'ID':
                            output += ': \"' + argument.value + "\""
                        elif type(argument.value) == str:
                            output += ': \"' + argument.value + "\""
                        elif type(argument.value) == int:
                            output += ': \"' + str(argument.value) + "\""
                except:
                    raise Exception('Issue exporting variable for: ' + argument)
        except:
            raise Exception('Issue with items exporting variable')
        output += ' }'
        return output

class FSTree():
    def __init__(self, obj, fieldName: str = None):
        if list in inspect.getmro(type(obj)):
            self.name = fieldName if fieldName else 'dummyList'
            if hasattr(obj, 'fieldsShow'):
                self.fieldsShow = obj.fieldsShow
            for element in obj:
                if isNoneOrBuiltinPrimitive(element): continue
                if hasattr(element, 'fieldsShow'):
                    if not hasattr(element, 'children'): self.children = []
                    self.children.append(FSTree(element))
        else:
            self.name =  fieldName if fieldName else getClassName(obj)
            if hasattr(obj, 'fieldsShow'):
                self.fieldsShow = obj.fieldsShow
                for field in obj.fieldsShow.keys():
                    objField = getattr(obj, field)
                    if isNoneOrBuiltinPrimitive(objField): continue
                    if not hasattr(self, 'children'): self.children = []
                    self.children.append(FSTree(objField, field))
        
     ##connection stuff......
    def getFSEdgeContainer(self):
        for childBranch in self.children:
            if childBranch.name == 'GQLEdge':
                return childBranch       
          
    def setFieldShow(self, property: str, show: bool):
        info = getDotNotationInfo(property)
        path = info[0]
        variable = info[1]
        
        if len(path) == 0:
            print('trying to hide the entire object...')
            return
        
        attrContainer = self.findBranchContainer(path)
        if variable in attrContainer.fieldsShow.keys():
            attrContainer.fieldsShow[variable] = show
        else: 
            raise Exception('field ' + variable + ' not found!')
       
    def findBranchContainer(self, path: str):
        attrContainer = self
        
        for field in path:
            if attrContainer.name == field: ##container object
                continue
            else:
                for child in attrContainer.children:
                    if child.name == field:  
                        attrContainer = child
                        if attrContainer.name == 'edges': 
                            attrContainer = attrContainer.getFSEdgeContainer()
        return attrContainer
        