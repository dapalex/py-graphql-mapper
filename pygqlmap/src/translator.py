
import inspect
import keyword
from enum import Enum
import logging as logger
from pygqlmap.helper import handle_recursive_ex
from .utils import execute_regex, is_empty_field
from pygqlmap.gql_types import ID
from .consts import COMMA_CONCAT


switchStrType = {
        'String': 'str',
        'Boolean': 'bool',
        'Int': 'int',
        'Float': 'float',
        'ID': 'ID'
    }

class Translate():

    def to_graphql_field_name(pyVariableName: str):
        try:
            return pyVariableName if not pyVariableName.endswith('_') and pyVariableName.removesuffix('_') not in keyword.kwlist else  pyVariableName.removesuffix('_')
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during formatting of graphql field name for ' + pyVariableName)

    def to_python_var_name(gqlFieldName):
        try:
            return gqlFieldName if gqlFieldName not in keyword.kwlist else gqlFieldName + '_'
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during formatting of python variable name for ' + gqlFieldName)

    def to_graphql_value(pyVariable):
        try:
            if isinstance(pyVariable, ID) or isinstance(pyVariable, str):
                return '\"' + pyVariable + '\"'
            elif isinstance(pyVariable, bool):
                return str(pyVariable).lower()
            elif isinstance(pyVariable, int) or isinstance(pyVariable, float) or isinstance(pyVariable, list):
                return str(pyVariable).replace('\'', '\"')
            elif isinstance(pyVariable, type):
                return '\"' + str(pyVariable).replace('\'', '\"') + '\"'
            elif Enum in inspect.getmro(type(pyVariable)):
                return pyVariable.value
            elif isinstance(pyVariable, dict):
                output = ' { '
                for varKey, varValue in pyVariable.items():
                    output += Translate.to_graphql_field_name(varKey) + ': ' + Translate.to_graphql_value(varValue) + COMMA_CONCAT

                output = output.removesuffix(COMMA_CONCAT)
                output += ' } '
                return output
            else:
                logger.warning('to manage')
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during formatting of graphql value for ' + pyVariable)

    def to_json_value(pyVariable):
        try:
            if isinstance(pyVariable, ID) or isinstance(pyVariable, str):
                return '\"' + pyVariable + '\"'
            elif isinstance(pyVariable, bool):
                return str(pyVariable).lower()
            elif isinstance(pyVariable, int) or isinstance(pyVariable, float) or isinstance(pyVariable, list):
                return str(pyVariable).replace('\'', '\"')
            elif isinstance(pyVariable, type):
                return '\"' + str(pyVariable).replace('\'', '\"') + '\"'
            elif Enum in inspect.getmro(type(pyVariable)):
                return'\"' +  pyVariable.value + '\"'
            elif isinstance(pyVariable, dict):
                output = ' { '
                for varKey, varValue in pyVariable.items():
                    output += Translate.to_graphql_field_name(varKey) + ': ' + Translate.to_graphql_value(varValue) + COMMA_CONCAT

                output = output.removesuffix(COMMA_CONCAT)
                output += ' } '
                return output
            else:
                logger.warning('to manage')
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during formatting of graphql value for ' + pyVariable)

    def to_graphql_type(pyVariable):
        if isinstance(pyVariable, ID):
            return 'ID'
        elif isinstance(pyVariable, str):
            return 'String'
        elif isinstance(pyVariable, bool):
            return 'Boolean'
        elif isinstance(pyVariable, int):
            return 'Int'
        elif isinstance(pyVariable, type): #should never get in
            return 'Type'
        elif isinstance(pyVariable, dict):
            output = ' { '
            for varKey, varValue in pyVariable.items():
                output += '$' + Translate.to_graphql_field_name(varKey) + ': ' + Translate.to_graphql_type(varValue) + COMMA_CONCAT

            output = output.removesuffix(COMMA_CONCAT)
            output += ' } '
            return output
        elif Enum in inspect.getmro(type(pyVariable)) or inspect.isclass(type(pyVariable)):
            return type(pyVariable).__name__
        else:
            raise handle_recursive_ex(Exception('type not managed!'), '')

    def to_python_type(typeName):
        return switchStrType.get(typeName, typeName)

    def to_json_vars(fields: dict):
        output = ''
        try:
            for fieldName, fieldValue in fields.items():
                if is_empty_field(fieldValue): continue
                try:
                    from pygqlmap.components import GQLObject
                    output += ', ' if output.startswith('{') else '{ '
                    output += '\"' + Translate.to_graphql_field_name(fieldName) +  '\" :'
                    if GQLObject in inspect.getmro(type(fieldValue)):
                        output += Translate.to_json_vars(fieldValue.__dict__)
                    else:
                        output += Translate.to_json_value(fieldValue)
                except Exception as ex:
                    raise handle_recursive_ex(ex, 'Issue exporting variable for: ' + fieldName)

            output.removesuffix(COMMA_CONCAT)
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Issue with items exporting variable')

        output += ' }'
        return output

    def graphqlize(inputSourceDict, argsToIgnore = None):
        try:
            output= ''
            for inputSourceKey, inputSourceValue in inputSourceDict.items():
                if isinstance(inputSourceValue, dict):
                    print('Getting into ' + inputSourceKey)
                    output += inputSourceKey + (argsToIgnore if argsToIgnore else '') + ' { ' + Translate.graphqlize(inputSourceValue) + ' } '
                elif isinstance(inputSourceValue, tuple):
                    if isinstance(inputSourceValue[1], dict):
                        output += inputSourceKey + inputSourceValue[0] + ' { ' + Translate.graphqlize(inputSourceValue[1]) + ' } '
                else:
                    output += execute_regex(" " + inputSourceKey + " ")
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Exception during graphqlizing of ' + str(inputSourceDict))

        return output

    def exclude_args_substring(dataInput: str, argsToIgnore: list):
        for args in argsToIgnore:
            try:
                if str(dataInput).__contains__(args):
                    logger.info('splitting ' + dataInput)
                    inputList = dataInput.split(args)
                    return args.join(Translate.exclude_args_substring(x, argsToIgnore) for x in inputList)
            except Exception as ex:
                raise handle_recursive_ex(ex, 'Exception during args exclusion from graphqlize for substring ' + dataInput)

        return execute_regex(dataInput)

    def to_graphql_argsset_definition(pyObject):
        output = ''

        try:
            for field in pyObject.__dataclass_fields__:
                objectField = getattr(pyObject, field)
                if is_empty_field(objectField): continue
                try:
                    from pygqlmap.components import GQLObject
                    if GQLObject in inspect.getmro(type(objectField)):
                        output += field + ': { ' + Translate.to_graphql_argsset_definition(objectField) + ' } '
                        output += COMMA_CONCAT
                    elif isinstance(objectField, list):
                        output += field + ': [ '
                        for elementList in objectField:
                            if GQLObject in inspect.getmro(type(elementList)):
                                output += ' { ' + Translate.to_graphql_argsset_definition(elementList) + ' } ' + COMMA_CONCAT
                            else:
                                output += Translate.to_graphql_value(elementList) + COMMA_CONCAT
                        output = output.removesuffix(COMMA_CONCAT)
                        output += ' ] ' + COMMA_CONCAT
                    else:
                        if hasattr(pyObject, field) and not objectField == None:
                            output += Translate.to_graphql_arg_definition(field, objectField)
                except Exception as ex:
                    raise handle_recursive_ex(ex, 'Issue during export of name and value for: ' + objectField)

            output = output.removesuffix(COMMA_CONCAT)

        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during translation of argument set definition')
        return output

    def to_graphql_arg_definition(fieldName, field):
        return Translate.to_graphql_field_name(fieldName) + ': ' + Translate.to_graphql_value(field) + COMMA_CONCAT
