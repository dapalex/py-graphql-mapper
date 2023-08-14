from abc import ABC, abstractmethod
from dataclasses import asdict
import inspect
import logging as logger
from pygqlmap.helper import handle_recursive_ex
from .consts import COMMA_CONCAT, ARGS_DECLARE
from ..enums import ArgType

from .utils import is_empty_field
from .translator import Translate

class FieldsShow(ABC):

    @property
    def fieldsshow(self):
        return self._fieldsshow

    def init_fieldshow(self):
        """ For internal use only """
        try:
            self._fieldsshow = asdict(self)
            try:
                for field in self._fieldsshow:
                    self._fieldsshow[field] = True
            except Exception as ex:
               raise handle_recursive_ex(ex, 'Error during fieldShow initialization for field ' + field)
        except Exception as ex:
           raise handle_recursive_ex(ex, 'Error during fieldShow initialization')

class Builder():
    @abstractmethod
    def build(self, dataInput, pyObject):
        pass

    @abstractmethod
    def set_py_fields(self, dataInput, opObject, customObject=None):
        pass

    def build(self, inputDict: dict, pyObject: any):
        """  for internal use only    """

        try:
            if self.log_progress: logger.info('Started building of python object: ' + pyObject.__class__.__name__)
            item = inputDict.popitem() ##extract the KV pair containing object name and content

            if not item[1] == None:
                self.set_py_fields(item[1], pyObject)
            else:
                pyObject = item[1]
                logger.info(item[0] + ' has no content')

        except Exception as ex:
            logger.error('Building of python object failed - ' + ex.args[0])

        return pyObject

class GQLExporter():

    log_progress: bool

    @property
    def export_gql_source(self):
        gqlArgs, outputGqlDict = self.export_gql_dict
        return gqlArgs + ' { ' + Translate.graphqlize(outputGqlDict) + ' } '

    @property
    def export_gql_dict(self):
        """Return the GraphQL syntax for the current object

        Returns:
            str: GraphQL object exported
        """
        if hasattr(self, 'log_progress') and self.log_progress: logger.info('Started GQL extraction of python: ' + self.__class__.__name__)

        gqlDict = asdict(self)
        outputGqlDict = {}

        from pygqlmap.src.arg_builtin import ArguedBuiltin
        try:
            for field in gqlDict.keys():
                try:
                    if field == ARGS_DECLARE: continue
                    if self._fieldsshow[field]:
                        fieldObject = getattr(self, field)
                        if fieldObject == None: continue
                        if ArguedBuiltin in inspect.getmro(type(fieldObject)):
                                builtinArgs = fieldObject._args.export_args
                                outputGqlDict[Translate.to_graphql_field_name(field)] = builtinArgs, Translate.to_graphql_field_name(field)
                        elif FieldsShow in inspect.getmro(type(fieldObject)):
                            outputGqlDict[Translate.to_graphql_field_name(field)] = fieldObject.export_gql_dict
                        elif list in inspect.getmro(type(fieldObject)):
                            for list_el in fieldObject:
                                if FieldsShow in inspect.getmro(type(list_el)):
                                    outputGqlDict[Translate.to_graphql_field_name(field)] = list_el.export_gql_dict
                                else:
                                    pass
                        else:
                            if not fieldObject == None:
                                outputGqlDict[Translate.to_graphql_field_name(field)] = fieldObject

                except Exception as ex:
                    raise handle_recursive_ex(ex, 'Issue exporting field ' + self.__class__.__name__ + '.' + field)

        except Exception as ex:
            raise handle_recursive_ex(ex, 'Issue during export of gql dictionary')

        gqlArgs = ''
        #Arguments management START - after check of fields requested
        if hasattr(self, ARGS_DECLARE):
            try:
                if hasattr(self, 'log_progress') and self.log_progress: logger.info('Started GQL extraction of args for: ' + self.__class__.__name__)
                gqlArgs = self._args.export_args
            except Exception as ex:
                raise handle_recursive_ex(ex, 'Issue exporting _args for ' + str(self.__class__.__name__))

        #Arguments management END

        if len(outputGqlDict) == 0:
            return None, None

        return gqlArgs, outputGqlDict

class GQLBaseArgsSet():

    @abstractmethod
    def export_arg_key(self, field_name, field_value, field_type):
        """ For internal use only """
        raise handle_recursive_ex(Exception('exportArg function not implemented'), '')

    @property
    def export_args(self):
        arguments = ''
        try:
            if self._args_type == ArgType.LITERAL_VALUES:
                arguments = self.export_gqlargs_and_values
                if len(arguments) > 0:
                    return '(' + arguments + ')'
            elif self._args_type == ArgType.VARIABLES:
                arguments = self.export_gqlarg_keys
                if len(arguments) > 0:
                    return '(' + arguments + ')'
            else:
                raise handle_recursive_ex(Exception('No valid argType for '), '')
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Issue during export arguments for ' + self.__class__.__name__)

        return arguments

    @property
    def export_gqlarg_keys(self):
        """ For internal use only """
        output = ''
        try:
            for field in self.__dataclass_fields__:
                if is_empty_field(getattr(self, field)): continue
                try:
                    output += self.export_arg_key(field, getattr(self, field), self.__dataclass_fields__[field].type) + COMMA_CONCAT
                except:
                    raise handle_recursive_ex(Exception('Issue exporting arg key for: ' + field), '')

            output = output.removesuffix(COMMA_CONCAT)
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Issue exporting arg keys for ' + str(self.__class__))

        return output
