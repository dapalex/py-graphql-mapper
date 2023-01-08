
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
            if isinstance(pyVariable, ID) or isinstance(pyVariable, str):
                return '\"' + pyVariable + '\"'
            elif isinstance(pyVariable, int) or isinstance(pyVariable, float) or isinstance(pyVariable, list):
                return str(pyVariable).replace('\'', '\"')
            elif isinstance(pyVariable, type):
                return '\"' + str(pyVariable).replace('\'', '\"') + '\"'
            elif isinstance(pyVariable, bool):
                return str(pyVariable).lower()
            elif Enum in inspect.getmro(type(pyVariable)):
                return pyVariable.value
            elif isinstance(pyVariable, dict):
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
            if isinstance(pyVariable, ID) or isinstance(pyVariable, str):
                return '\"' + pyVariable + '\"'
            elif isinstance(pyVariable, int) or isinstance(pyVariable, float) or isinstance(pyVariable, list):
                return str(pyVariable).replace('\'', '\"')
            elif isinstance(pyVariable, type):
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
        if isinstance(pyVariable, str):
            return 'String'
        elif isinstance(pyVariable, int):
            return 'Int'
        elif isinstance(pyVariable, ID):
            return 'ID'
        elif isinstance(pyVariable, type): #should never get in
            return 'Type'
        elif isinstance(pyVariable, bool):
            return 'Boolean'
        elif isinstance(pyVariable, dict):
            output = ' { '
            for varKey, varValue in pyVariable.items():
                output += '$' + Translate.toGraphQLFieldName(varKey) + ': ' + Translate.toGraphQLType(varValue) + commaConcat

            output = output.removesuffix(commaConcat)
            output += ' } '
            return output
        elif Enum in inspect.getmro(type(pyVariable)) or inspect.isclass(type(pyVariable)):
            return type(pyVariable).__name__
        else:
            raise HandleRecursiveEx(Exception('type not managed!'), '')

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
                except Exception as ex:
                    raise HandleRecursiveEx(ex, 'Issue exporting variable for: ' + fieldName)

            output.removesuffix(commaConcat)
        except Exception as ex:
            raise HandleRecursiveEx(Exception('Issue with items exporting variable'), '')

        output += ' }'
        return output

    def graphQLize(inputSourceDict, argsToIgnore = None):
        try:
            output= ''
            for inputSourceKey, inputSourceValue in inputSourceDict.items():
                if isinstance(inputSourceValue, dict):
                    print('Getting into ' + inputSourceKey)
                    output += inputSourceKey + (argsToIgnore if argsToIgnore else '') + ' { ' + Translate.graphQLize(inputSourceValue) + ' } '
                elif isinstance(inputSourceValue, tuple):
                    if isinstance(inputSourceValue[1], dict):
                        output += inputSourceKey + inputSourceValue[0] + ' { ' + Translate.graphQLize(inputSourceValue[1]) + ' } '
                else:
                    output += executeRegex(" " + inputSourceKey + " ")
        except Exception as ex:
            raise HandleRecursiveEx(ex, 'Exception during graphqlizing of ' + str(inputSourceDict))

        return output

    def excludeArgsSubstring(dataInput: str, argsToIgnore: list):
        for args in argsToIgnore:
            try:
                if str(dataInput).__contains__(args):
                    print('splitting ' + dataInput)
                    inputList = dataInput.split(args)
                    return args.join(Translate.excludeArgsSubstring(x, argsToIgnore) for x in inputList)
            except Exception as ex:
                raise HandleRecursiveEx(ex, 'Exception during args exclusion from graphqlize for substring ' + dataInput)

        return executeRegex(dataInput)

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
                    elif isinstance(objectField, list):
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
