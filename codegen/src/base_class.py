import copy
import logging as logger
from pygqlmap.src.translator import Translate
from .enums import TypeKind
from .utils import gqlTypeKinds, typesByName

class TypeManager():

    def compose_py_type(self) -> str:
        is_non_null = False
        is_list = False
        is_custom_scalar = False
        typeOutput = ''

        if not self.type_defs:
            logger.error('Need to extract type definition first')
        for typeDef in self.type_defs:
            try:
                current_sctype = Translate.to_python_type(typeDef)
                if current_sctype == TypeKind.NON_NULL.name:
                    is_non_null = True
                    continue
                elif current_sctype == TypeKind.LIST.name:
                    is_list = True
                    continue

                typeOutput += current_sctype

            except Exception as ex:
                raise Exception('Error during composition of type ' + typeDef + ' for ' + self.name + ' - ' + ex.args[0])

        if is_non_null: typeOutput += ' ##NON NULL'
        if is_list: typeOutput += ' ##LIST'
        if is_custom_scalar: typeOutput += ' ##'+ typeDef + '##'

        self.type_defs.clear()
        return typeOutput, current_sctype

    def get_used_GQL_objnames(self, gqlTypeNameListParam:list = None):
        try:
            if gqlTypeNameListParam == None: gqlTypeNameListParam = []
            gqlTypeNameList = copy.deepcopy(gqlTypeNameListParam)
            if hasattr(self, 'kind') and self.kind and self.kind in gqlTypeKinds:
                gqlTypeNameList.append(self.name)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.get_used_GQL_objnames(gqlTypeNameList)
            if hasattr(self, 'type') and self.type:
                return self.type.get_used_GQL_objnames(gqlTypeNameList)
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
