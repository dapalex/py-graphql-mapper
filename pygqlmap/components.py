from dataclasses import dataclass
from .helper import handle_recursive_ex
from .src.gql_init import _sub_class_init
from .src.components import FSTree
from .src.base import FieldsShow, GQLExporter, GQLBaseArgsSet
from .src.consts import COMMA_CONCAT, ARGS_DECLARE, PRIMITIVES
from .src.utils import is_empty_field
from .enums import ArgType, OperationType
from .src.translator import Translate

class GQLOperationArgs(GQLBaseArgsSet):

    @property
    def export_gqlarg_keys(self):

        """ For internal use only """
        output = ''
        try:
            for fieldName, fieldValue in self.arguments.items():
                if is_empty_field(fieldValue[0]): continue
                try:
                    output += self.export_arg_key(fieldName, fieldValue[0], fieldValue[1]) + COMMA_CONCAT
                except Exception as ex:
                    raise handle_recursive_ex(ex, 'Issue exporting arg key for: ' + fieldName)

            output = output.removesuffix(COMMA_CONCAT)
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Issue exporting arg keys')

        return output

    @property
    def export_gqlvariables(self):
        """Return the json variables to send to a server

        Returns:
            str: json variables exported
        """
        if self._args_type == ArgType.VARIABLES:
            if self.arguments:
                json_fields = dict((key, val[0]) for key, val in self.arguments.items())
                return Translate.to_json_vars(json_fields)

    def export_arg_key(self, field_name, field_value, field_type):
        return '$' + Translate.to_graphql_field_name(field_name) + ': ' + Translate.to_graphql_type(field_value, field_type)

class GQLArgsSet(GQLBaseArgsSet):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = _sub_class_init

    def export_arg_key(self, field_name, field_value, field_type):
        """ For internal use only """
        return Translate.to_graphql_field_name(field_name) + ': $' + Translate.to_graphql_field_name(field_name)

    @property
    def export_gqlargs_and_values(self):
        """ For internal use only """
        return Translate.to_graphql_argsset_definition(self)

@dataclass
class GQLObject(FieldsShow, GQLExporter):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = _sub_class_init

class GQLOperation(GQLExporter, GQLOperationArgs):
    name: str
    obj_type: OperationType
    fieldShowTree: FSTree
    type: GQLObject
    ##key: field name
    ##value: (field value, field original type)
    arguments: dict = None

    # argumentsRetrieved: False

    def __init__(self, op_type: OperationType, dataType, operationName: str = None, argsType: ArgType = ArgType.LITERAL_VALUES): #, rootName: str = None, inputFieldName: str = None
        """_summary_

        Args:
            op_type (OperationType): _description_
            hasArgsAsInput (bool, optional): _description_. Defaults to True.
            name (str, optional): _description_. Defaults to 'myQuery'.
            log_progress (bool, optional): _description_. Defaults to False.
        """
        self.name = operationName if operationName else ''

        self.obj_type = op_type
        self.type = dataType
        self._args_type = argsType
        self.fieldsshowTree = FSTree(self.type, self.__class__.__name__)
        self.log_progress = False

    def set_show(self, keys: str or list[str], isVisible: bool):
        """_summary_

        Args:
            keys (strorlist[str]): GraphQL field path or list of GraphQL field paths
            isVisible (bool): set visibility (default at true)

        Raises:
            Exception: keys not string or list of strings
        """
        kType = type(keys)
        if kType == str:
            self.fieldsshowTree.set_fieldshow(keys, isVisible)
        elif kType == list:
            print('list of keys with same value')
            for key in keys:
                self.fieldsshowTree.set_fieldshow(key, isVisible)

    @property
    def export_gql_source(self):
        """Return the GraphQL syntax for the current operation

        Returns:
            str: GraphQL Query exported
        """
        try:
            prefix = self.obj_type.value + ' ' + self.name + ' '
            self.type.log_progress = self.log_progress

            ##Arguments of the operation are arguments of the root object
            if hasattr(self, ARGS_DECLARE):
                setattr(self.type, ARGS_DECLARE, getattr(self, ARGS_DECLARE))

            #Update all payload arguments (NESTED ARGUMENTS) with the argument type requested
            self.manage_nested_args(self.type)
            # self.setArgsLocations(self.type, None, rootName, '')

            if self._args_type == ArgType.VARIABLES:
                if hasattr(self, ARGS_DECLARE) and self.arguments:
                    prefix += '(' + self.export_gqlarg_keys + ')'

            return prefix + ' { ' + self.__class__.__name__ + self.type.export_gql_source + ' } '
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Issue during export of ' + self.name)

    def manage_nested_args(self, currentObj):
        if not self.arguments: self.arguments = {}
        try:
            if isinstance(currentObj, list): #if it is I have to set the elements as well?
                for list_el in currentObj:
                    self.manage_nested_args(list_el)

            #if obj contains field with arg name, add arg
            if type(currentObj) in PRIMITIVES or not hasattr(currentObj, '__dataclass_fields__'):
                return

            if hasattr(currentObj, ARGS_DECLARE):
                currentObj._args._args_type = self._args_type
                for arg in currentObj._args.__dataclass_fields__:
                    argValue = getattr(currentObj._args, arg)
                    if is_empty_field(argValue): continue
                    self.arguments.update({arg: (argValue, currentObj._args.__dataclass_fields__[arg].type)})

            for subObj in currentObj.__dataclass_fields__:
                if subObj == ARGS_DECLARE:  continue
                self.manage_nested_args(getattr(currentObj, subObj))
        except Exception as ex:
            raise handle_recursive_ex(ex, 'Error during args type propagation - ')
