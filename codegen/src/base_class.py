import copy
import logging as logger
from pygqlmap.src.consts import GQLLIST_PREFIX, NON_NULL_PREFIX, STRING_GQLLIST_BUILTIN
from pygqlmap.src.translator import Translate
from .enums import TypeKind
from .utils import gqlTypeKinds, typesByName

class SchemaTypeManager():

    def compose_py_type(self, is_arg: bool = False) -> str:
        is_list = False
        type_out = ''
        is_nonnull = False

        if not self.type_defs:
            logger.error('Need to extract type definition first')
        for type_def in self.type_defs:
            try:
                py_type = Translate.to_python_type(type_def)
                if py_type == TypeKind.NON_NULL.name:
                    is_nonnull = True
                    continue
                elif py_type == TypeKind.LIST.name:
                    is_list = True
                    type_out += (NON_NULL_PREFIX if is_nonnull else '') + GQLLIST_PREFIX
                    if is_nonnull: is_nonnull = False
                    continue

                if is_list:
                    if py_type in STRING_GQLLIST_BUILTIN or 'ENUM' in self.get_used_typekinds():
                        type_out = type_out.removesuffix('_')
                        type_out += '['
                    else:
                        type_out += py_type + '['
                if is_nonnull:
                    if is_arg: ##if it is not an argument we can ignore the nonnullability, it is responsibility of the server
                        type_out += NON_NULL_PREFIX
                    else:
                        pass

                type_out += py_type

            except Exception as ex:
                raise Exception('Error during composition of type ' + type_def + ' for ' + self.name + ' - ' + ex.args[0])

        if is_list: type_out += ']'

        self.type_defs.clear()
        return type_out, py_type

    def get_used_typekinds(self, gql_typekind_list_param:list = None):
        try:
            if gql_typekind_list_param == None: gql_typekind_list_param = []
            gql_typekind_list = copy.deepcopy(gql_typekind_list_param)
            if hasattr(self, 'kind') and self.kind:
                gql_typekind_list.append(self.kind)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.get_used_typekinds(gql_typekind_list)
            if hasattr(self, 'type') and self.type:
                return self.type.get_used_typekinds(gql_typekind_list)
        except Exception as ex:
            raise Exception('Error during etraction of used object GraphQL names' + ' - ' + ex.args[0])

        return gql_typekind_list

    def get_used_typenames(self, gql_typename_list_param:list = None):
        try:
            if gql_typename_list_param == None: gql_typename_list_param = []
            gql_typename_list = copy.deepcopy(gql_typename_list_param)
            if hasattr(self, 'kind') and self.kind and self.kind in gqlTypeKinds:
                gql_typename_list.append(self.name)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.get_used_typenames(gql_typename_list)
            if hasattr(self, 'type') and self.type:
                return self.type.get_used_typenames(gql_typename_list)
        except Exception as ex:
            raise Exception('Error during etraction of used object GraphQL names' + ' - ' + ex.args[0])

        return gql_typename_list

    def get_objtype_defs(self, typeDefListParam = None):
        if typeDefListParam == None: typeDefListParam = []
        typeDefList = copy.deepcopy(typeDefListParam)

        try:
            if hasattr(self, 'kind') and self.kind:
                if self.kind in typesByName:
                    typeDefList.append(self.name)
                else:
                    typeDefList.append(self.kind)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.get_objtype_defs(typeDefList)
            if hasattr(self, 'type') and self.type:
                return self.type.get_objtype_defs(typeDefList)
        except Exception as ex:
            raise Exception('Error during etraction of object type definitions' + ' - ' + ex.args[0])

        return typeDefList

    def get_valid_fields_lst(self):
        try:
            if hasattr(self, 'args') and self.args: ##Schema Field
                    return self.args
            elif hasattr(self, 'fields') and self.fields: ##OBJECT, INTERFACE
                    return self.fields
            elif hasattr(self, 'inputFields') and self.inputFields: ##INPUT_OBJECT
                    return self.inputFields
            elif hasattr(self, 'possibleTypes') and self.possibleTypes: ##UNION
                    return self.possibleTypes.values()
            else: ##No list of fields
                return []
        except Exception as ex:
            raise Exception('Error getting fields list for type ' + self.name + ' - ' + ex.args[0])
