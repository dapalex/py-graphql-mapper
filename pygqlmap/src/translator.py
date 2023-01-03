
import inspect
import keyword
from enum import Enum

from pygqlmap.helper import HandleRecursiveEx
from .utils import executeRegex, isEmptyField
from pygqlmap.gqlTypes import ID
from .consts import commaConcat


switchStrType = {
        'String': 'str',
        'Boolean': 'bool',
        'Int': 'int',
        'Float': 'float',
        'ID': 'ID'
    }

class Translate():

    def toGraphQLFieldName(pyVariableName: str):
        try:
            return pyVariableName if not pyVariableName.endswith('_') and pyVariableName.removesuffix('_') not in keyword.kwlist else  pyVariableName.removesuffix('_') 
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Error during formatting of graphql field name for ' + pyVariableName)
    
    def toPythonVariableName(gqlFieldName):
        try:
            return gqlFieldName if gqlFieldName not in keyword.kwlist else gqlFieldName + '_'
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Error during formatting of python variable name for ' + gqlFieldName)   
     
    def toGraphQLValue(pyVariable):
        try:     
            if type(pyVariable) == ID or type(pyVariable) == str:
                return '\"' + pyVariable + '\"'
            elif type(pyVariable) == int or type(pyVariable) == float or type(pyVariable) == list:
                return str(pyVariable).replace('\'', '\"')
            elif type(pyVariable) == type:
                return '\"' + str(pyVariable).replace('\'', '\"') + '\"'
            elif type(pyVariable) == bool:
                return str(pyVariable).lower()
            elif Enum in inspect.getmro(type(pyVariable)):
                return pyVariable.value
            elif type(pyVariable) == dict:
                output = ' { '
                for varKey, varValue in pyVariable.items():
                    output += Translate.toGraphQLFieldName(varKey) + ': ' + Translate.toGraphQLValue(varValue) + commaConcat
                    
                output = output.removesuffix(commaConcat)
                output += ' } '
                return output
            else:
                print('to manage')
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Error during formatting of graphql value for ' + pyVariable)
        
    def toJsonValue(pyVariable):
        try:     
            if type(pyVariable) == ID or type(pyVariable) == str:
                return '\"' + pyVariable + '\"'
            elif type(pyVariable) == int or type(pyVariable) == float or type(pyVariable) == list:
                return str(pyVariable).replace('\'', '\"')
            elif type(pyVariable) == type:
                return '\"' + str(pyVariable).replace('\'', '\"') + '\"'
            elif type(pyVariable) == bool:
                return str(pyVariable).lower()
            elif Enum in inspect.getmro(type(pyVariable)):
                return'\"' +  pyVariable.value + '\"'
            elif type(pyVariable) == dict:
                output = ' { '
                for varKey, varValue in pyVariable.items():
                    output += Translate.toGraphQLFieldName(varKey) + ': ' + Translate.toGraphQLValue(varValue) + commaConcat
                    
                output = output.removesuffix(commaConcat)
                output += ' } '
                return output
            else:
                print('to manage')
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Error during formatting of graphql value for ' + pyVariable)
        
    def toGraphQLType(pyVariable):
        if type(pyVariable) == str:
            return 'String'
        elif type(pyVariable) == int:
            return 'Int'
        elif type(pyVariable) == ID:
            return 'ID'
        elif type(pyVariable) == type: #should never get in
            return 'Type'  
        elif type(pyVariable) == bool:  
            return 'Boolean'
        elif type(pyVariable) == dict:  
            output = ' { '
            for varKey, varValue in pyVariable.items():
                output += '$' + Translate.toGraphQLFieldName(varKey) + ': ' + Translate.toGraphQLType(varValue) + commaConcat
            
            output = output.removesuffix(commaConcat)
            output += ' } '
            return output
        elif Enum in inspect.getmro(type(pyVariable)) or inspect.isclass(type(pyVariable)): 
            return type(pyVariable).__name__
        else:
            raise HandleRecursiveEx(None, 'type not managed!')
       
    def toPythonTypeOrOriginal(typeName):
        return switchStrType.get(typeName, typeName)     

    def toJsonVariables(fields: dict):
        output = ''
        try:
            for fieldName, fieldValue in fields.items():
                if isEmptyField(fieldValue): continue
                try:
                    from pygqlmap.components import GQLObject
                    output += ', ' if output.startswith('{') else '{ '
                    output += '\"' + Translate.toGraphQLFieldName(fieldName) +  '\" :'
                    if GQLObject in inspect.getmro(type(fieldValue)):
                        output += Translate.toJsonVariables(fieldValue.__dict__)
                    else:
                        output += Translate.toJsonValue(fieldValue)
                except:
                    raise Exception('Issue exporting variable for: ' + fieldName)
            
            output.removesuffix(commaConcat)
        except:
            raise HandleRecursiveEx(None, 'Issue with items exporting variable')   
        
        output += ' }'
        return output

    def graphQLize(inputSourceDict, argsToIgnore = None):
        try:
            output= ''
            for inputSourceKey, inputSourceValue in inputSourceDict.items():
                if type(inputSourceValue) == dict:
                    print('Getting into ' + inputSourceKey)
                    output += inputSourceKey + (argsToIgnore if argsToIgnore else '') + ' { ' + Translate.graphQLize(inputSourceValue) + ' } '
                elif type(inputSourceValue) == tuple:
                    if type(inputSourceValue[1]) == dict:
                        output += inputSourceKey + inputSourceValue[0] + ' { ' + Translate.graphQLize(inputSourceValue[1]) + ' } '
                else:
                    output += executeRegex(" " + inputSourceKey + " ")
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Exception during graphqlizing of ' + str(inputSourceDict))
        
        return output
    
    # ##works on the last dict
    # def excludeArgs(inputSourceDict: dict, argsToIgnore: list = []) -> str:
    #     stringifiedInputDict = str(inputSourceDict)
    #     output: str = ''
    #     wentThrough = False
        
    #     print('working on ' + stringifiedInputDict)
    #     try:
    #         if argsToIgnore:
    #             for args in argsToIgnore:
    #                 try:
    #                     if stringifiedInputDict.__contains__(args):
    #                         inputList = stringifiedInputDict.split(args)
    #                         output += args.join(Translate.excludeArgsSubstring(x, argsToIgnore) for x in inputList)
    #                         wentThrough = True    
    #                 except Exception as ex: 
    #                     raise HandleRecursiveEx(ex, 'Exception during args exclusion from graphqlize for ' + str(inputSourceDict))
                   
    #     except Exception as ex: 
    #         raise HandleRecursiveEx(ex, 'Exception during args exclusion from graphqlize for ' + str(inputSourceDict))
        
    #     return executeRegex(stringifiedInputDict) if not wentThrough else output

    def excludeArgsSubstring(input: str, argsToIgnore: list):
        for args in argsToIgnore:
            try:
                if str(input).__contains__(args):
                    print('splitting ' + input)
                    inputList = input.split(args)
                    return args.join(Translate.excludeArgsSubstring(x, argsToIgnore) for x in inputList)
            except Exception as ex: 
                raise HandleRecursiveEx(ex, 'Exception during args exclusion from graphqlize for substring ' + input)
        
        return executeRegex(input)
    
    def toGraphQLArgsSetDefinition(pyObject):
        output = ''
        
        try: 
            for field in pyObject.__dataclass_fields__:
                objectField = getattr(pyObject, field)
                if isEmptyField(objectField): continue
                try:
                    from pygqlmap.components import GQLObject
                    if GQLObject in inspect.getmro(type(objectField)):
                        output += field + ': { ' + Translate.toGraphQLArgsSetDefinition(objectField) + ' } ' 
                        output += commaConcat 
                    elif type(objectField) == list:
                        output += field + ': [ '
                        for elementList in objectField:
                            if GQLObject in inspect.getmro(type(elementList)):
                                output += ' { ' + Translate.toGraphQLArgsSetDefinition(elementList) + ' } ' + commaConcat
                            else:
                                output += Translate.toGraphQLValue(elementList) + commaConcat 
                        output = output.removesuffix(commaConcat)
                        output += ' ] ' + commaConcat
                    else:  
                        if hasattr(pyObject, field) and not objectField == None:
                            output += Translate.toGraphQLArgDefinition(field, objectField)
                except Exception as ex:
                    raise HandleRecursiveEx(ex, 'Issue during export of name and value for: ' + objectField)

            output = output.removesuffix(commaConcat)

        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Error during translation of argument set definition')
        return output
    
    def toGraphQLArgDefinition(fieldName, field):
        return Translate.toGraphQLFieldName(fieldName) + ': ' + Translate.toGraphQLValue(field) + commaConcat 
        