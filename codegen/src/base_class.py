import copy
import logging as logger
from pygqlmap.src.consts import NON_NULL_PREFIX
from pygqlmap.src.translator import Translate
from .enums import TypeKind
from .utils import gqlTypeKinds, typesByName

class SchemaTypeManager():

    def compose_py_type(self, is_arg: bool = False) -> str:
        is_list = False
        type_out = ''

        if not self.type_defs:
            logger.error('Need to extract type definition first')
        for type_def in self.type_defs:
            try:
                py_type = Translate.to_python_type(type_def)
                if py_type == TypeKind.NON_NULL.name:
                    if is_arg: type_out += NON_NULL_PREFIX
                    continue
                elif py_type == TypeKind.LIST.name:
                    type_out += 'List['
                    is_list = True
                    continue

                type_out += py_type

            except Exception as ex:
                raise Exception('Error during composition of type ' + type_def + ' for ' + self.name + ' - ' + ex.args[0])

        if is_list: type_out += ']'

        self.type_defs.clear()
        return type_out, py_type

    def get_used_typenames(self, gqlTypeNameListParam:list = None):
        try:
            if gqlTypeNameListParam == None: gqlTypeNameListParam = []
            gqlTypeNameList = copy.deepcopy(gqlTypeNameListParam)
            if hasattr(self, 'kind') and self.kind and self.kind in gqlTypeKinds:
                gqlTypeNameList.append(self.name)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.get_used_typenames(gqlTypeNameList)
            if hasattr(self, 'type') and self.type:
                return self.type.get_used_typenames(gqlTypeNameList)
        except Exception as ex:
            raise Exception('Error during etraction of used object GraphQL names' + ' - ' + ex.args[0])

        return gqlTypeNameList

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
