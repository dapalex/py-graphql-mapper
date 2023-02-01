import random
import string
import logging as logger
from codegen.src.base_class import SchemaTypeManager
from pygqlmap.components import GQLArgsSet
from pygqlmap.enums import OperationType
from pygqlmap.src.translator import Translate, switch_gql_py_type
from pygqlmap.src.consts import *
from .consts import *
from .enums import TypeKind
from .sp_schema import GQLSchema, SCField, SCType
from .utils import add_val_update_dict, is_deprecated, pop_val_clean_dict, split_types
from .priority import ExtractionResults, PriorElement

class Extractor():

    indent: str
    schema: GQLSchema
    enums: dict
    queries: dict
    mutations: dict
    mutationsEnumValues: list
    simpleTypes: dict[str, SCType]
    types: dict[str, SCType]
    priorList: list[PriorElement]
    extraction_results: ExtractionResults
    add_desc: bool
    log_progress: bool
    circular_ref_types: dict[str, list[str]]

    def __init__(self, schema, log_progress: bool = False, add_desc: bool = False):
        self.log_progress = log_progress
        self.add_desc = add_desc
        self.indent = '   '
        self.scalars = {}
        self.enums = {}
        self.simpleTypes = {}
        self.types = {}
        self.queries = None
        self.queriesEnumValues = []
        self.mutations = None
        self.mutationsEnumValues = []
        self.circular_ref_types = {}

        self.extraction_results = ExtractionResults()

        self.schema = schema

        self.priorList = []

        super().__init__()

    def extract_schema_code(self):
        try:
            self.extract_types_from_gqlschema()

            self.extraction_results.enum_classes = self.extract_enums()
            self.extraction_results.scalar_defs = self.extract_scalars()
            self.extraction_results.simple_type_classes = self.extract_simple_types()
            self.extraction_results.type_classes = self.extract_types()
            if hasattr(self, 'queries') and self.queries:
                self.query_classes, self.queriesEnumValues = self.extract_operations(OperationType.QUERY, self.queries)
                if self.query_classes: self.extraction_results.query_classes.update(self.query_classes)

            if hasattr(self, 'mutations') and self.mutations:
                self.mutation_classes, self.mutationsEnumValues = self.extract_operations(OperationType.MUTATION, self.mutations)
                if self.mutation_classes: self.extraction_results.mutation_classes.update(self.mutation_classes)

            #create Mutations Enum
            self.extraction_results.queries_enum_class = self.extract_operations_enum(OperationType.QUERY, self.queriesEnumValues)
            self.extraction_results.mutations_enum_class = self.extract_operations_enum(OperationType.MUTATION, self.mutationsEnumValues)
        except Exception as ex:
            logger.error('Error during Schema code extraction' + ' - ' + ex.args[0])

        return self.extraction_results

    def extract_types_from_gqlschema(self):
        """For internal use

        Populates the CodeGenerator object lists
           - enums
           - mutations
           - types
        """
        try:
            if self.log_progress: logger.info('Started extraction of types')
            tempTypes = {}
            while self.schema.types:
                currentType = self.schema.types.popitem()
                if self.log_progress: logger.info('Started extraction of type ' + currentType[0])
                if currentType[0].startswith('__'):
                    continue
                if currentType[1].kind == TypeKind.SCALAR.name:
                    self.scalars.update({ currentType[0]: currentType[1] })
                    continue
                if currentType[0] == 'Query':
                    self.queries = currentType[1]
                    continue
                if currentType[0] == 'Mutation':
                    self.mutations = currentType[1]
                    continue
                if currentType[1].kind == TypeKind.ENUM.name:
                    self.enums.update({ currentType[0]: currentType[1] })
                    continue
                else:
                    tempTypes.update({ currentType[0]: currentType[1] })

            self.simpleTypes, self.types = split_types(tempTypes)
        except Exception as ex:
            logger.error('Error during GQL schema types extraction - ' + ex.args[0])

    def extract_scalars(self):
        scalarDefinitions = {}
        try:
            if self.log_progress: logger.info('Started extraction of scalars')
            while self.scalars:
                schemaScalar = self.scalars.popitem()[1]

                scalarCodeLine = self.generate_scalar(schemaScalar)
                scalarDefinitions.update({ schemaScalar.name: [scalarCodeLine] })
        except Exception as ex:
            logger.error('Error during transformation of CodeGenerator enums' + ' - ' + ex.args[0])

        return scalarDefinitions

    def generate_scalar(self, schemaScalar: SCType):
        if self.log_progress: logger.info('Started extraction of scalar ' + schemaScalar.name)
        schemaScalar.type_defs = schemaScalar.get_objtype_defs()

        if schemaScalar.name in switch_gql_py_type:
            scalarType = switch_gql_py_type[schemaScalar.name]
        else:
            scalarType = schemaScalar.compose_py_type()[0]
            if scalarType not in STRING_PRIMITIVES:
                scalarType = 'str'

        scalarCodeLine = SCALAR_SIGNATURE%(schemaScalar.name,scalarType)

        if self.add_desc and schemaScalar.description:
                scalarCodeLine +=  ' ##' + schemaScalar.description.replace('\n', ' - ')

        if self.log_progress: logger.info(schemaScalar.name + 'scalar extracted')

        return scalarCodeLine

    def extract_enums(self):
        """For internal use"""
        enumClasses = {}

        try:
            if self.log_progress: logger.info('Started extraction of enums')
            while self.enums:
                schemaEnum = self.enums.popitem()[1]

                if not list(filter(lambda ev: not hasattr(ev, 'isDeprecated') or ev.isDeprecated == False, schemaEnum.enumValues)): continue

                if self.log_progress: logger.info('Started extraction of enum ' + schemaEnum.name)
                enumCodeLst = []
                enumCodeLst.append(ENUM_SIGNATURE%schemaEnum.name + ':')


                if self.add_desc:
                    if schemaEnum.description:
                        enumCodeLst.append(self.indent + '"""')
                        enumCodeLst.append(self.indent + schemaEnum.name + ' - ' + schemaEnum.description + '\n')
                        enumCodeLst.append(self.indent + '"""')

                ##SET DEFAULT
                enumCodeLst.append(self.indent + "DEFAULT = None")

                for enumValue in schemaEnum.enumValues:

                    if is_deprecated(enumValue):
                        logger.warning(enumValue.name + ' deprecated!')
                        continue

                    codeLine = self.indent + Translate.to_python_var_name(enumValue.name) + ' = \'' + enumValue.name + '\''
                    if hasattr(enumValue, 'description') and enumValue.description:
                        codeLine += ' ##' + enumValue.description
                    enumCodeLst.append(codeLine)

                if self.log_progress: logger.info(schemaEnum.name + 'enum extracted')
                enumClasses.update({ schemaEnum.name: enumCodeLst })
        except Exception as ex:
            logger.error('Error during transformation of CodeGenerator enums' + ' - ' + ex.args[0])

        return enumClasses

    def extract_simple_types(self):
        """For internal use"""
        simpleTypeClasses = {}

        if self.log_progress: logger.info('Started extraction of types')
        try:
            while self.simpleTypes:
                currentTypeKV = self.simpleTypes.popitem()

                if self.log_progress: logger.info('Started extraction of type ' + currentTypeKV[0])
                self.extract_schema_type(currentTypeKV[1])

            for priorElement in self.priorList:

                if not priorElement.codeList:
                    logger.error('No body for simple type ' + priorElement.name)

                simpleTypeClasses.update({ priorElement.name: priorElement.codeList })
                self.priorList.remove(priorElement)
            if self.log_progress: logger.info('Extraction of simpleTypes completed')
        except Exception as ex:
            logger.error('Error during transformation of CodeGenerator simpleTypes' + ' - ' + ex.args[0])

        return simpleTypeClasses

    def extract_types(self):
        """For internal use"""
        typeClasses = {}
        if self.log_progress: logger.info('Started extraction of types')
        try:
            while self.types:
                currTypeKV = self.types.popitem()

                if self.log_progress: logger.info('Started extraction of type ' + currTypeKV[0])
                self.extract_schema_type(currTypeKV[1], {})

            for priorElement in self.priorList:
                if not priorElement.codeList:
                    logger.error('No body for type ' + priorElement.name)

                ##recheck for generated classes
                if priorElement.name.endswith(ARGUED_SIGNATURE_SUFFIX):
                    realType = False

                    priorElement.schemaType.type_defs = priorElement.schemaType.get_objtype_defs()

                    actualType = priorElement.schemaType.compose_py_type()[1]

                    if actualType in STRING_PRIMITIVES or actualType in self.extraction_results.scalar_defs.keys():
                        for objNameList in self.extract_fields_types(priorElement.schemaType).values():
                            if objNameList:
                                realType = True
                                break

                        if not realType:
                            simpleTypeClasses = { priorElement.name: priorElement.codeList }
                            simpleTypeClasses.update(self.extraction_results.simple_type_classes)
                            self.extraction_results.simple_type_classes = simpleTypeClasses
                            continue
                ##recheck for generated classes

                typeClasses.update({ priorElement.name: priorElement.codeList })
            if self.log_progress: logger.info('Extraction of types completed')
        except Exception as ex:
            logger.error('Error during transformation of CodeGenerator types' + ' - ' + ex.args[0])

        return typeClasses

    def extract_operations(self, opType: OperationType, operations: list):
        """For internal use"""
        operationClasses = {}
        operationEnumValues = []
        self.circular_ref_types = {}
        try:
            if self.log_progress: logger.info('Started extraction of ' + opType.name)

            for operation in operations.fields:
                if self.log_progress: logger.info('Started extraction of ' + opType.name + ' ' + operation.name)
                try:
                    operation_code_list = self.extract_type_code(operation, objType=opType)
                    operationClasses.update({ operation.name : operation_code_list })
                    operationEnumValues.append(operation.name)
                except Exception as ex:
                    logger.error('Error during extraction of ' + opType.name + ' ' + operation.name + ' - ' + ex.args[0])

                if self.log_progress: logger.info(operation.name + ' extracted')
        except Exception as ex:
            logger.error('Error during transformation of CodeGenerator operations' + ' - ' + ex.args[0])

        return operationClasses, operationEnumValues

    def extract_operations_enum(self, opType: OperationType, operationsEnumValues):
        """For internal use"""
        operationKey = 'Queries' if opType == OperationType.QUERY else 'Mutations'
        operationEnumClass = {}
        if self.log_progress: logger.info('Started generation of ' + operationKey + ' enum')
        enumCodeLst = []

        enumCodeLst.append(ENUM_SIGNATURE%operationKey + ':')

        for enumValue in operationsEnumValues:
            enumCodeLst.append(self.indent + enumValue + ' = ' + enumValue)

        operationEnumClass.update({ operationKey: enumCodeLst })
        if self.log_progress: logger.info(operationKey + ' enum generated')

        return operationEnumClass

    def extract_schema_type(self, curr_schematype, argued_field_cls_name: str = None):
        """For internal use

        Args:
            currentType (tuple): tuple containing (schema name, schema type) to extract
           self.circular_ref_types (dict[str, list[str]], optional):

            Dictionary containing

            key: schema Type???

            value: list of paths where the schema type is used???

            Defaults to {}.
        """
        currentTypeName = curr_schematype.name if not argued_field_cls_name else argued_field_cls_name
        if self.log_progress: logger.info('Started extraction of type ' + currentTypeName)

        if self.is_already_extracted(currentTypeName)[0]:
            logger.debug(currentTypeName + " already extracted!")
            return

        try:
            ###### Create dictionary for current schema type containing
            # key:field name
            # value: type used by field
            fields_name_usedtype = self.extract_fields_types(curr_schematype)

            if argued_field_cls_name: #set parent class as used type
                splitArgName = argued_field_cls_name.split('_')
                fields_name_usedtype.update({ argued_field_cls_name: [splitArgName[1]] })

            for used_types in fields_name_usedtype.values():
              for usedtype_name in used_types:
                try:
                    if self.log_progress: logger.info(currentTypeName + ' uses ' + usedtype_name)

                    if self.is_already_extracted(usedtype_name)[0]:
                        logger.debug(usedtype_name + ' for ' + currentTypeName + " already extracted!")
                        pop_val_clean_dict(usedtype_name, fields_name_usedtype)
                        continue
                    elif self.types.get(usedtype_name):
                        poppedUsedType = self.types.pop(usedtype_name)

                        if self.log_progress: logger.info('Calling extraction for ' + usedtype_name)

                        self.extract_schema_type(poppedUsedType)
                    else:
                        # It is a circular reference
                        if self.log_progress: logger.info('Used type ' + usedtype_name + ' for ' + currentTypeName + ' not found in already managed types, it can be a circular reference')

                        ###### Generate list containing dotted path to the used type for circular references registration
                        utilizers = []

                        for fieldName, usedTypeList in fields_name_usedtype.items():
                            if fieldName == argued_field_cls_name:
                                utilizers.append(argued_field_cls_name)
                            elif usedtype_name in usedTypeList:
                                utilizers.append(curr_schematype.name + '.' + fieldName)

                        #Register the used type in the circular references
                        add_val_update_dict(self.circular_ref_types, usedtype_name, utilizers)

                except Exception as ex:
                    logger.error('Error during management of used type ' + usedtype_name + ' - ' + ex.args[0])

            typeCode = self.extract_type_code(curr_schematype, arguedName=argued_field_cls_name)

            if typeCode:
                pqElement = PriorElement(currentTypeName, curr_schematype, typeCode)

                if self.log_progress: logger.info(currentTypeName + ' type extracted, appending...')
                self.priorList.append(pqElement)
            else:
                logger.warning('Type ' + currentTypeName + ' not extracted')

        except Exception as ex:
            logger.error('Error during extraction of type ' + currentTypeName + ' - ' + ex.args[0])

    def extract_type_code(self, schemaType, objType: OperationType = OperationType.GENERIC_TYPE, arguedName:str = None):
        """For internal use"""
        schemaTypeName = schemaType.name if not arguedName else arguedName
        if self.log_progress: logger.info('Started extraction of code for ' + schemaTypeName)
        codeLines = []
        try:
            if hasattr(schemaType, 'kind') and schemaType.kind == TypeKind.UNION.name:
                codeLines = self.generate_union_code(schemaType)
            else:
                codeLines = self.generate_class_code(schemaType, objType, arguedName)

            if self.log_progress: logger.info(schemaTypeName + ' code extraction  completed')
            return codeLines
        except Exception as ex:
            logger.error('Error during extraction of type ' + schemaTypeName + ' - ' + ex.args[0])
            return []

    def generate_union_code(self, scType: SCType):
        """For internal use"""
        try:
            codeLst = []

            singleLineCode = "class " + scType.name + '(GQLObject): \n' + self.indent + 'pass'

            # singleLineCode = scType.name + ' = '

            # if multipleTypes := len(scType.possibleTypes) > 1:
            #     singleLineCode += 'Union['

            # while scType.possibleTypes:
            #     argument = scType.possibleTypes.popitem()
            #     try:
            #         if argument[0] inself.circular_ref_types.keys() and scType.name + '.' + argument[0] inself.circular_ref_types[argument[0]]:
            #             singleLineCode += "'" + Translate.to_python_var_name(argument[0]) + "'" + ','
            #             self.removeFromCheckCircularTypes(argument[0], scType.name + '.' + argument[0])
            #             #self.circular_ref_types[argument[0]].remove(scType.name + '.' + argument[0])
            #             # if notself.circular_ref_types[argument[0]]:
            #             #    self.circular_ref_types.pop(argument[0])
            #         else:
            #             singleLineCode += Translate.to_python_var_name(argument[0]) + ', '

            #     except Exception as ex:
            #         logger.error('Error during extraction of element ' + argument[0] + ' - ' + ex.args[0])

            # singleLineCode = singleLineCode.removesuffix(',')

            # if multipleTypes:
            #     singleLineCode += ']'

            # if self.add_desc and scType.description:
            #         codeLst.append('"""\n' + scType.description + '\n"""\n')
            codeLst.append(singleLineCode)

        except Exception as ex:
            logger.error('Error during extraction of content for type ' + scType.name + ' - ' + ex.args[0])

        return codeLst

    def generate_class_code(self, scType: SCType, obj_type: OperationType = OperationType.GENERIC_TYPE, argued_class_name: str = None):
        """For internal use"""
        scTypeName = scType.name if not argued_class_name else argued_class_name
        if self.log_progress: logger.info('Started generation of class for ' + scTypeName)
        classCodeLst = []
        docsLst = []
        returnCodeList = []
        possibleTypes = None

        try:
            if self.add_desc:
                if hasattr(scType, 'description') and scType.description:
                    docsLst.append(self.indent + scTypeName + ' - ' + scType.description + '\n')

            scType.type_defs = scType.get_objtype_defs()
            py_type = scType.compose_py_type(argued_class_name)[1]

            fieldsCodeList = []
            fieldsDocCodeList = []

            if isinstance(scType, SCField):
                fieldsCodeList = self.extract_schema_field_code(scType, obj_type)
            elif hasattr(scType, 'kind') and scType.kind == 'OBJECT': #fields
                    fieldsDocCodeList, fieldsCodeList =  self.extract_schema_type_content(scType, py_type, obj_type, 'fields')
            elif hasattr(scType, 'kind') and scType.kind == 'INTERFACE':
                    fieldsDocCodeList, fieldsCodeList =  self.extract_schema_type_content(scType, py_type, obj_type, 'fields')
                    # if scType.possibleTypes:
                    #     possibleTypes =  self.extract_schema_possible_types(scType)
            elif hasattr(scType, 'kind') and  scType.kind == 'INPUT_OBJECT': #inputFields
                    fieldsDocCodeList, fieldsCodeList =  self.extract_schema_type_content(scType, py_type, obj_type, 'inputFields')

            if self.add_desc and fieldsDocCodeList: docsLst.extend(fieldsDocCodeList)
            classCodeLst.extend(fieldsCodeList)

            if not argued_class_name:
                    if hasattr(scType, 'type') and scType.type:
                        classCodeLst.append(self.generate_code_line(scType, None, obj_type)[1])
            else:
                if py_type in STRING_PRIMITIVES:
                    scalarCodeLine = self.generate_scalar(scType)
                    self.extraction_results.scalar_defs.update({ scType.name: [scalarCodeLine] })

            try:
                scTypeName = py_type if py_type not in STRING_PRIMITIVES and obj_type == OperationType.GENERIC_TYPE else scType.name
                signature = self.generate_type_signature(obj_type, scTypeName, argued_class_name, possibleTypes)
            except Exception as ex:
                logger.error('Error during creation of signature for type ' + scTypeName + ' - ' + ex.args[0])

            if classCodeLst:
                returnCodeList.append(signature)
                if self.add_desc and docsLst:
                    returnCodeList.append(self.indent + '"""')
                    returnCodeList.extend(docsLst)
                    returnCodeList.append(self.indent + '"""')
                returnCodeList.extend(classCodeLst)
            else:
                logger.warning('Missing code for type ' + scTypeName)

            if self.log_progress: logger.info(scTypeName + ' code generation completed')

        except Exception as ex:
            logger.error('Error during extraction of content for type ' + scTypeName + ' - ' + ex.args[0])

        return returnCodeList

    def extract_schema_field_code(self, scType: SchemaTypeManager, obj_type: OperationType):
        """For internal use
           Generates the class content corresponding to the schema type
           plus a nested custom class with signature suffix 'Args' corresponding to a field

        Args:
            scType (SchemaTypeManager)
            obj_type (OperationType)

        Returns:
            _type_: class code
        """
        codeLst = []

        if hasattr(scType, 'args') and scType.args:
            scType.type_defs = scType.get_objtype_defs()
            py_el_type = scType.compose_py_type()[1]
            arguedClassName = py_el_type + "Args"
            codeLst.append(self.indent + "class " + arguedClassName + "(" + GQLArgsSet.__name__ + ", GQLObject):")

            queryArgDocLst = []
            queryArgCodeLst = []
            for argument in scType.args:

                try:
                    docLine, codeLine = self.generate_code_line(argument, scType, obj_type, is_argument=True)
                    if self.add_desc and docLine: queryArgDocLst.append(docLine)
                    queryArgCodeLst.append(codeLine)

                except Exception as ex:
                    logger.error('Error during extraction of schema field element ' + argument.name + ' - ' + ex.args[0])

            if self.add_desc and queryArgDocLst:
                codeLst.append(self.indent + self.indent + '"""')
                codeLst.extend(list(map(lambda el: self.indent + el, queryArgDocLst)))
                codeLst.append(self.indent + self.indent + '"""')
            codeLst.extend(list(map(lambda el: self.indent + el, queryArgCodeLst)))
            codeLst.append('\n' + self.indent + ARGS_DECLARE + ': ' + arguedClassName)
            codeLst.append('\n')

        return codeLst

    def extract_schema_possible_types(self, scType):
        possibleTypes = ''
        for possibleTypeName, possibleType in scType.possibleTypes.items():

                ##check if the element is deprecated --> skip it
                if is_deprecated(possibleType):
                    logger.warning(possibleTypeName + ' deprecated!')
                    continue

                possibleTypes += "'" + possibleTypeName + "'" if not possibleTypes else (" or '" + possibleTypeName + "'")
        return possibleTypes

    def extract_schema_type_content(self, scType, py_sctype, obj_type, contentName):
        """For internal use
           Generate the class content corresponding to the schema type

        Args:
            scType (_type_)
            py_el_type (_type_)
            contentName (_type_)

        Returns:
            _type_: _description_
        """
        codeLst = []
        docsLst = []
        try:
            if hasattr(scType, contentName):
                content = getattr(scType, contentName)
                if not content: return [scType.name + ' = ' + py_sctype]

                ##check if all elements are deprecated --> get out empty handed
                if not list(filter(lambda ev: not hasattr(ev, 'isDeprecated') or ev.isDeprecated == False, content)):
                    logger.warning('Type ' + scType.name + ' deprecated!')
                    return [], []

                for element in content:

                    ##check if the element is deprecated --> skip it
                    if is_deprecated(element):
                        logger.warning(element.name + ' is deprecated')
                        continue

                    try:
                        docLine, codeLine = self.generate_code_line(element, scType)
                        if self.add_desc and docLine: docsLst.append(docLine)
                        codeLst.append(codeLine)

                    except Exception as ex:
                        logger.error('Error during extraction of content of element ' + element.name + ' for schema Type ' + scType.name + ' - ' + ex.args[0])

        except Exception as ex:
            logger.error('Error during extraction of schema Type content ' + element.name + ' - ' + ex.args[0])
        return docsLst, codeLst

    def generate_code_line(self, element: SchemaTypeManager, parentType, obj_type: OperationType = OperationType.GENERIC_TYPE, is_argument: bool = False):
        docLine = ''
        codeLine = ''

        try:
            if self.add_desc:
                if hasattr(element, 'description') and element.description:
                    docLine = self.indent + element.name + ' - ' + element.description + '\n'

            element.type_defs = element.get_objtype_defs()
            py_inline_type, py_el_tp = element.compose_py_type(is_arg=is_argument)
            #################################################################
            #If the current schema field will be used as argument
            #If it has a nonnull constraint it will create a custom empty class
            #keeping note of that in the class name
            #################################################################
            try:
                if is_argument:
                    ##Check if nonnull type
                    if py_inline_type.__contains__((non_null_type := NON_NULL_PREFIX + py_el_tp))and not py_el_tp in STRING_GQL_BUILTIN:
                        if not self.is_already_extracted(non_null_type, include_type_refs=True)[0]:
                            ##Create Type alias with TypeVar
                            nonnull_ref_code_lines = []

                            is_extracted = self.is_already_extracted(py_el_tp, include_type_refs=True)[0]
                            if is_extracted and not 'ENUM' in element.get_used_typekinds():
                                nonnull_ref_code_lines.append(EMPTY_CLASS_SIGNATURE%(non_null_type, py_el_tp))
                            else:
                                nonnull_ref_code_lines.append(EMPTY_CLASS_SIGNATURE%(non_null_type, 'GQLObject'))

                            self.add_custom_class(obj_type, non_null_type, element, nonnull_ref_code_lines)
            except Exception as ex:
                logger.error('Error during code line generation - nonnull check - for ' + element.name + ' - ' + ex.args[0])

            #################################################################
            #Check if the current type contains arguments with schema type to extract
            #If so, extract the type as argued class first.
            #It has to be done here in order to keep the arg class name generated
            #################################################################
            argued_class_name = None

            if hasattr(element, 'args') and element.args and obj_type == OperationType.GENERIC_TYPE: ##MOVE OUT!
                ## Argued class name -> 5 chars random & field name & "_" parent class Name & "_Field"
                argued_class_name = ''.join(random.choices(string.ascii_uppercase, k=5)) + '_' + (py_el_tp if not py_el_tp in STRING_PRIMITIVES else element.name) + ARGUED_SIGNATURE_SUFFIX
                self.extract_schema_type(element, argued_class_name)

            #################################################################
            #Check if the current type has been registered as circular reference
            #If so, it will create a type alias (and deregister the type)
            #################################################################
            circ_ref_utilizer = False

            try:
                if element.get_used_typenames() and self.circular_ref_types:
                    circ_ref_utilizer = self.start_check_circular_ref_types(element, parentType, py_el_tp)

                    if circ_ref_utilizer:
                        new_type = NEWTYPE_DECLARATION%py_el_tp
                        py_inline_type = py_inline_type.replace(py_el_tp, new_type)
                        #Deregister the type from circular references
                        pop_val_clean_dict(circ_ref_utilizer, self.circular_ref_types, py_el_tp)
            except Exception as ex:
                logger.error('Error during code line generation - type alias creation - for element ' + element.name + ' - ' + ex.args[0])

            #################################################################
            #Last alteration of type declaration in the code
            #If it is a list of schema types it will create a new class merging list and class
            #so it can be directly used when its arguments need to be set
            #################################################################
            ##Check if gqllist type
            try:
                if (
                    py_inline_type.__contains__((gqllist_type := (NON_NULL_PREFIX + GQLLIST_PREFIX + py_el_tp))) or \
                    py_inline_type.__contains__((gqllist_type := (GQLLIST_PREFIX + py_el_tp)))
                    or \
                    (
                    circ_ref_utilizer and \
                    (
                    py_inline_type.__contains__((gqllist_type := (GQLLIST_PREFIX + new_type))) or \
                    py_inline_type.__contains__((gqllist_type := (NON_NULL_PREFIX + GQLLIST_PREFIX + new_type)))
                    )
                    )
                ) \
                and \
                not py_el_tp in STRING_GQLLIST_BUILTIN:
                    if circ_ref_utilizer:
                        py_inline_split = py_inline_type.split(gqllist_type)
                        gqllist_type = gqllist_type.replace(new_type, 'GQLObject')
                        py_inline_type = py_inline_split[0] + gqllist_type + py_inline_split[1].replace(new_type, 'GQLObject')
                    if not self.is_already_extracted(gqllist_type, include_type_refs=True)[0]:
                        gqllist_ref_code_lines = []
                        gqllist_ref_code_lines.append(GQLLIST_SIGNATURE%(gqllist_type, py_el_tp if not circ_ref_utilizer else 'GQLObject'))
                        self.add_custom_class(obj_type, gqllist_type, element, gqllist_ref_code_lines)
            except Exception as ex:
                logger.error('Error during code line generation - gqllist check - for element ' + element.name + ' - ' + ex.args[0])


            #################################################################
            #Actual generation of line of code
            #################################################################
            try:
                var_name = Translate.to_python_var_name(element.name) if (obj_type == OperationType.GENERIC_TYPE or is_argument) else 'type'
                codeLine = self.indent + var_name + ': ' + (py_inline_type if not argued_class_name else argued_class_name)
                if circ_ref_utilizer: codeLine += ' ## Circular Reference for ' + py_el_tp
            except Exception as ex:
                logger.error('Error during generation of line code for element ' + element.name + ' - ' + ex.args[0])

        except Exception as ex:
            logger.error('Error during extraction of element ' + element.name + ' - ' + ex.args[0])

        return docLine, codeLine

    def generate_type_signature(self, objType: OperationType, sctype_name, argued_class_name, possibleTypes):
        if not argued_class_name:
            if not possibleTypes:
                if objType == OperationType.QUERY:
                    return QUERY_SIGNATURE%sctype_name + ':'
                elif objType == OperationType.MUTATION:
                    return MUTATION_SIGNATURE%sctype_name + ':'
                else:
                    return CLASS_SIGNATURE%sctype_name + ':'
            else:
                return INTERFACE_SIGNATURE%(sctype_name, possibleTypes) + ':'
        else:
            if sctype_name not in STRING_PRIMITIVES and sctype_name not in self.extraction_results.scalar_defs.keys():
                if sctype_name in self.circular_ref_types.keys() and argued_class_name in self.circular_ref_types[sctype_name]:
                    ##creates circular ref type
                    circular_ref_code_line = TYPEVAR_SIGNATURE%(sctype_name, sctype_name, 'GQLObject')
                    self.extraction_results.type_refs.update({ sctype_name: [circular_ref_code_line] })
                    #update signature with circular ref management
                    signature = ARGUED_CLASS_SIGNATURE%(argued_class_name, "Generic[" + sctype_name + "]") + ':'

                    #Deregister the type from circular references
                    pop_val_clean_dict(argued_class_name, self.circular_ref_types, sctype_name)
                    return signature
            else:
                try:
                    scalar = self.extraction_results.scalar_defs[sctype_name]
                    scalar = scalar[0].split('##')[0].split('=')[1].strip()
                except Exception as ex:
                    raise Exception('Error during scalar code string extrapolation - ' + ex.args[0])

                gqlArguedScalar = 'Argued' + scalar.capitalize()
                return ARGUED_CLASS_SIGNATURE%(argued_class_name, gqlArguedScalar) + ':'

            if sctype_name in self.extraction_results.type_refs.keys() and \
               not self.is_already_extracted(sctype_name, include_type_refs=False):
                return ARGUED_CLASS_SIGNATURE%(argued_class_name, "Generic[" + sctype_name + "]") + ':'
            else:
                return ARGUED_CLASS_SIGNATURE%(argued_class_name, sctype_name) + ':'

    def add_custom_class(self, obj_type, custom_typename, schema_type, code_lines):
        if obj_type == OperationType.GENERIC_TYPE:
            self.priorList.append(PriorElement(custom_typename, schema_type, code_lines))
        elif obj_type == OperationType.QUERY:
            self.extraction_results.query_classes.update({custom_typename: code_lines})
        elif obj_type == OperationType.MUTATION:
            self.extraction_results.mutation_classes.update({custom_typename: code_lines})

    def extract_fields_types(self, scType: SCType):
        """For internal use

        Args:
            scType (SCType): schema type to check

        Returns: dictionary containing used type names and number of occurrences
        """
        if self.log_progress: logger.info('Started extraction of used types for ' + scType.name)
        field_usedtypes = {}

        fieldsList = scType.get_valid_fields_lst()

        try:
            for field in fieldsList:
                usedtypes_lst = field.get_used_typenames()
                if usedtypes_lst:
                    field_usedtypes.update({ field.name: usedtypes_lst })
                    if self.log_progress and field_usedtypes: logger.info('Found used Types: ' + str(field_usedtypes) + 'for field ' + field.name)

        except Exception as ex:
            logger.error('Error during extraction of used Types for ' + field.name + ' - ' + ex.args[0])

        if self.log_progress: logger.info('Used types for ' + scType.name + ' extracted')
        return field_usedtypes

    def is_already_extracted(self, typeNameCheck, include_type_refs: bool = False):
        if typeNameCheck in self.extraction_results.scalar_defs.keys():
            return True, SCALARS_NAME
        if typeNameCheck in self.extraction_results.enum_classes.keys():
            return True, ENUMS_NAME
        elif typeNameCheck in self.extraction_results.simple_type_classes.keys():
            return True, SIMPLE_TYPES_NAME
        elif typeNameCheck in self.extraction_results.type_classes.keys():
            return True, TYPES_NAME
        elif include_type_refs and typeNameCheck in self.extraction_results.type_refs.keys():
            return True, TYPE_REFS_NAME
        else:
            for x in self.priorList:
                if typeNameCheck == x.name:
                    return True, ''

        return False, ''

    def start_check_circular_ref_types(self, element, parentType, actualElType):
        try:
            if self.circular_ref_types and (circTypeUtilizers := self.circular_ref_types.get(actualElType)):

                    for circTypeUtilizer in circTypeUtilizers:
                        circType, circTypeField = circTypeUtilizer.split('.')

                        if parentType.name == circType and element.name == circTypeField:
                            return circTypeUtilizer
        except Exception as ex:
            logger.error('Error during check of circular refs for element ' + element.name + ' - ' + ex.args[0])
        return None
