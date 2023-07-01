
from dataclasses import asdict
import inspect
from types import GenericAlias
import keyword
from enum import Enum
import logging as logger
from pygqlmap.helper import handle_recursive_ex
from .utils import execute_regex, is_empty_field
from pygqlmap.gql_types import ID
from .consts import COMMA_CONCAT, NON_NULL_PREFIX, PRIMITIVES


switch_gql_py_type = {
        'String': 'str',
        'Boolean': 'bool',
        'Int': 'int',
        'Float': 'float',
        'ID': 'ID'
    }

switch_py_gql_type = {v: k for k, v in switch_gql_py_type.items()}

class Translate():

    def to_graphql_field_name(py_var_name: str):
        try:
            return py_var_name if not py_var_name.endswith('_') and py_var_name.removesuffix('_') not in keyword.kwlist else  py_var_name.removesuffix('_')
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during formatting of graphql field name for ' + py_var_name)

    def to_python_var_name(gql_field_name):
        try:
            return gql_field_name if gql_field_name not in keyword.kwlist else gql_field_name + '_'
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during formatting of python variable name for ' + gql_field_name)

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
            curr_type = pyVariable.__class__
            is_non_null = False

            if type(pyVariable) == GenericAlias:
                if pyVariable.__name__.startswith(NON_NULL_PREFIX):
                    is_non_null = True
                    curr_type = inspect.getmro(pyVariable.__origin__)[1] #get parent
            if pyVariable.__class__.__name__.startswith(NON_NULL_PREFIX):
                is_non_null = True
                curr_type = inspect.getmro(type(pyVariable))[1]

            if curr_type == ID or curr_type == str:
                return '\"' + pyVariable + '\"'
            elif curr_type == bool:
                return str(pyVariable).lower()
            elif curr_type == int or  curr_type == float:
                    return str(pyVariable).replace('\'', '\"')
            elif curr_type == list: #works only for simple lists
                elements = pyVariable if not is_non_null else pyVariable.__args__
                from pygqlmap.components import GQLObject
                if all([type(el) in PRIMITIVES or ID in inspect.getmro(type(el)) for el in elements]):
                    return str(pyVariable).replace('\'', '\"')
                elif all([GQLObject in inspect.getmro(type(el)) for el in elements]):
                    return ' [ ' + ', '.join([Translate.to_json_vars(asdict(el)) for el in elements]) + ' ] '
                elif any([type(el) in PRIMITIVES for el in elements]):
                    logger.warning('List of hybrid types')
                    pass #pita
                else:
                    pass #what
            elif  curr_type == type:
                return '\"' + str(pyVariable).replace('\'', '\"') + '\"'
            elif Enum in inspect.getmro(curr_type):
                return'\"' +  pyVariable.value + '\"'
            elif curr_type == dict:
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

    def to_graphql_type(pyVariable, var_type = None):
        curr_type = pyVariable.__class__ if not var_type else var_type
        graphql_type = ''
        is_non_null = False
        if type(pyVariable) == GenericAlias:
            if pyVariable.__name__.startswith(NON_NULL_PREFIX):
                is_non_null = True
                curr_type = inspect.getmro(pyVariable.__origin__)[1] #get parent
                curr_type_el = pyVariable.__args__[0]
        if curr_type.__name__.startswith(NON_NULL_PREFIX):
            is_non_null = True
            curr_type = inspect.getmro(curr_type)[1]
        if graphql_type := switch_py_gql_type.get(curr_type.__name__, None):
            pass
        elif curr_type == list: #when calling to_graphql_type non null object is already expected because of check_arg_
            graphql_type = '[' + Translate.to_graphql_type(pyVariable[0] if not is_non_null else curr_type_el) + ']'
        elif curr_type == type: #should never get in
            graphql_type = 'Type'
        elif curr_type == dict:
            output = ' { '
            for varKey, varValue in pyVariable.items():
                output += '$' + Translate.to_graphql_field_name(varKey) + ': ' + Translate.to_graphql_type(varValue) + COMMA_CONCAT

            output = output.removesuffix(COMMA_CONCAT)
            output += ' } '
            return output
        elif Enum in inspect.getmro(curr_type) or inspect.isclass(curr_type):
            graphql_type = curr_type.__name__
        else:
            raise handle_recursive_ex(Exception('type not managed!'), '')

        return graphql_type + ('!' if is_non_null else '')

    def to_python_type(typeName):
        return switch_gql_py_type.get(typeName, typeName)

    def to_json_vars(fields: dict):
        output = ''
        try:
            for fieldName, fieldValue in fields.items():
                if is_empty_field(fieldValue): continue
                try:
                    output += ', ' if output.startswith('{') else '{ '
                    output += '\"' + Translate.to_graphql_field_name(fieldName) +  '\" :'
                    from pygqlmap.components import GQLObject
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
                    if isinstance(objectField, list):
                        output += field + ': [ '
                        for elementList in objectField:
                            if GQLObject in inspect.getmro(type(elementList)):
                                output += ' { ' + Translate.to_graphql_argsset_definition(elementList) + ' } ' + COMMA_CONCAT
                            else:
                                output += Translate.to_graphql_value(elementList) + COMMA_CONCAT
                        output = output.removesuffix(COMMA_CONCAT)
                        output += ' ] ' + COMMA_CONCAT
                    elif GQLObject in inspect.getmro(type(objectField)):
                        output += field + ': { ' + Translate.to_graphql_argsset_definition(objectField) + ' } '
                        output += COMMA_CONCAT
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
