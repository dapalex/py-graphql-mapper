
import inspect
import keyword
from enum import Enum
from .utils import executeRegex, getClassName
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
            raise Exception('Error during formatting of graphql field name for ' + pyVariableName + ' - ' + ex.args[0])
    
    def toPythonVariableName(gqlFieldName):
        try:
            return gqlFieldName if gqlFieldName not in keyword.kwlist else gqlFieldName + '_'
        except Exception as ex:
            raise Exception('Error during formatting of python variable name for ' + gqlFieldName + ' - ' + ex.args[0])
    
     
    def toGraphQLValue(pyVariable):
        try:     
            if getClassName(pyVariable) == 'ID' or type(pyVariable) == str:
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
            raise Exception('Error during formatting of graphql value for ' + pyVariable + ' - ' + ex.args[0])
        
    def toGraphQLType(pyVariable):
        if type(pyVariable) == str:
            return 'String'
        elif type(pyVariable) == int:
            return 'Int'
        elif getClassName(pyVariable) == 'ID':
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
        else:
            print('type not managed!')
       
    def toPythonTypeOrOriginal(typeName):
        return switchStrType.get(typeName, typeName)     

    def graphQLize(inputSchema: str, argsToIgnore: tuple = ()): ##argsToIgnore not necessary for mutations
        output= ''
        wentThrough = False
        if argsToIgnore:
            for args in argsToIgnore:
                if inputSchema.__contains__(args):
                    ##argument already graphQLized and to avoid further processing  
                    ##got to be just injected
                    inputList = inputSchema.split(args)
                    output =  executeRegex(inputList[0]) + ' ' + args + ' ' + executeRegex(inputList[1])
                    wentThrough = True
            
            return output if wentThrough else executeRegex(inputSchema)
        else:
            return executeRegex(inputSchema)
