import random
import string
from pygqlmap.components import GQLArgsSet
from pygqlmap.src.consts import STRING_PRIMITIVES, ARGUED_SIGNATURE_SUFFIX
from pygqlmap.enums import OperationType
import logging as logger
from pygqlmap.src.translator import Translate, switchStrType
from .enums import TypeKind
from .sp_schema import GQLSchema, SCField, SCType
from .utils import is_deprecated, split_types
from .priority import ExtractionResults, PriorElement
from .consts import SCALAR_SIGNATURE, CLASS_SIGNATURE, ENUM_SIGNATURE, ARGUED_CLASS_SIGNATURE, INTERFACE_SIGNATURE, QUERY_SIGNATURE, MUTATION_SIGNATURE

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
    extractionResults: ExtractionResults
    add_desc: bool
    log_progress: bool

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

        self.extractionResults = ExtractionResults()

        self.schema = schema

        self.priorList = []

        super().__init__()

    def extract_schema_code (self):
        try:
            self.extract_types_from_gqlschema()

            self.extractionResults.scalarDefinitions = self.extract_scalars()
            self.extractionResults.enumClasses = self.extract_enums()
            self.extractionResults.simpleTypeClasses = self.extract_simple_types()
            self.extractionResults.typeClasses = self.extract_types()
            if hasattr(self, 'queries') and self.queries:
                self.extractionResults.queryClasses, self.queriesEnumValues = self.extract_operations(OperationType.QUERY, self.queries)

            if hasattr(self, 'mutations') and self.mutations:
                self.extractionResults.mutationClasses, self.mutationsEnumValues = self.extract_operations(OperationType.MUTATION, self.mutations)

            #create Mutations Enum
            self.extractionResults.queriesEnumClass = self.extract_operations_enum(OperationType.QUERY, self.queriesEnumValues)
            self.extractionResults.mutationsEnumClass = self.extract_operations_enum(OperationType.MUTATION, self.mutationsEnumValues)
        except Exception as ex:
            logger.error('Error during Schema code extraction' + ' - ' + ex.args[0])

        return self.extractionResults

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
                scalarDefinitions.update({ schemaScalar.name: scalarCodeLine })
        except Exception as ex:
            logger.error('Error during transformation of CodeGenerator enums' + ' - ' + ex.args[0])

        return scalarDefinitions

    def generate_scalar(self, schemaScalar: SCType):
        if self.log_progress: logger.info('Started extraction of scalar ' + schemaScalar.name)
        schemaScalar.type_defs = schemaScalar.get_objtype_defs()

        if schemaScalar.name in switchStrType:
            scalarType = switchStrType[schemaScalar.name]
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
                self.extract_schema_type(currentTypeKV[1], {})

            for priorElement in self.priorList:

                if not priorElement.codeList:
                    logger.error('No body for simple type ' + priorElement.name)

                ##force recheck?
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

                    if actualType in STRING_PRIMITIVES or actualType in self.extractionResults.scalarDefinitions.keys():
                        for objNameList in self.extract_used_types(priorElement.schemaType).values():
                            if objNameList:
                                realType = True
                                break

                        if not realType:
                            simpleTypeClasses = { priorElement.name: priorElement.codeList }
                            simpleTypeClasses.update(self.extractionResults.simpleTypeClasses)
                            self.extractionResults.simpleTypeClasses = simpleTypeClasses
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
        try:
            if self.log_progress: logger.info('Started extraction of ' + opType.name)

            for operation in operations.fields:
                if self.log_progress: logger.info('Started extraction of ' + opType.name + ' ' + operation.name)
                try:
                    operationCode = self.extract_type_code(operation, circularRefTypes=[], objType=opType)
                    operationClasses.update({ operation.name : operationCode })
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

    def extract_schema_type(self, currentType, circularRefTypes: dict[str, list[str]], arguedName: str = None):
        """For internal use

        Args:
            currentType (tuple): tuple containing (schema name, schema type) to extract
            circularRefTypes (dict[str, list[str]], optional):

            Dictionary containing

            key: schema Type???

            value: list of paths where the schema type is used???

            Defaults to {}.
        """
        currentTypeName = currentType.name if not arguedName else arguedName
        if self.log_progress: logger.info('Started extraction of type ' + currentTypeName)

        if self.is_already_extracted(currentTypeName):
            logger.warning(currentTypeName + " already extracted!")
            return

        usedTypes = []
        try:
            usedTypes = self.extract_used_types(currentType)
            usedTypesDict = {}
            for objNameList in usedTypes.values():
                for objName in objNameList:
                    if objName not in usedTypesDict.keys():
                        usedTypesDict.update({ objName: 1 })
                    else:
                        usedTypesDict[objName] += 1

            if arguedName:
                splitArgName = arguedName.split('_')
                usedTypesDict.update({ splitArgName[1]: 1 })
                # usedTypesDict.update({ arguedName.removesuffix(ARGUED_SIGNATURE_SUFFIX): 1 })

            for usedTypeNameKey, occurrences in usedTypesDict.items():
                try:
                    if self.log_progress: logger.info(currentTypeName + ' uses ' + usedTypeNameKey)
                    if self.is_already_extracted(usedTypeNameKey):
                        logger.warning(currentTypeName + " already extracted!")
                        continue
                    elif self.types.get(usedTypeNameKey):
                        poppedUsedType = self.types.pop(usedTypeNameKey)

                        if self.log_progress: logger.info('Call extraction for ' + usedTypeNameKey)

                        self.extract_schema_type(poppedUsedType, circularRefTypes)
                    else:
                        # It can be a circular reference
                        if self.log_progress: logger.info('Used type ' + usedTypeNameKey + ' for ' + currentTypeName + ' not found in already managed types, it can be a circular reference')

                        utilizers = []

                        for fieldName, usedTypeList in usedTypes.items():
                            if usedTypeNameKey in usedTypeList:
                                utilizers.append(currentType.name + '.' + fieldName)

                        if arguedName:
                                utilizers.append(arguedName)

                        if usedTypeNameKey == currentType.name and occurrences == 0:
                            logger.error('inconsistence')

                        if not usedTypeNameKey in circularRefTypes.keys():
                            circularRefTypes.update({ usedTypeNameKey: utilizers })
                        else:
                            if not currentType.name in circularRefTypes[usedTypeNameKey]:
                                circularRefTypes[usedTypeNameKey].extend(utilizers)

                except Exception as ex:
                    logger.error('Error during management of used type ' + usedTypeNameKey + ' - ' + ex.args[0])

            typeCode = self.extract_type_code(currentType, circularRefTypes, arguedName=arguedName)

            if typeCode:
                pqElement = PriorElement(currentTypeName, currentType, typeCode)

                if self.log_progress: logger.info(currentTypeName + ' type extracted')
                if self.log_progress: logger.info('Appending extracted ' + currentTypeName)
                self.priorList.append(pqElement)
            else:
                logger.warning('Type ' + currentTypeName + ' not extracted')

        except Exception as ex:
            logger.error('Error during extraction of type ' + currentTypeName + ' - ' + ex.args[0])


    def is_already_extracted(self, typeNameCheck, includeCircularRefs: bool = True):
        if typeNameCheck in self.extractionResults.scalarDefinitions.keys():
            return True
        if typeNameCheck in self.extractionResults.enumClasses.keys():
            return True
        elif typeNameCheck in self.extractionResults.simpleTypeClasses.keys():
            return True
        elif includeCircularRefs and typeNameCheck in self.extractionResults.circularRefs.keys():
            return True
        else:
            for x in self.priorList:
                if typeNameCheck == x.name:
                    return True

        return False




    def extract_type_code(self, schemaType, circularRefTypes, objType: OperationType = OperationType.GENERIC_TYPE, arguedName:str = None):
        """For internal use"""
        schemaTypeName = schemaType.name if not arguedName else arguedName
        if self.log_progress: logger.info('Started extraction of code for ' + schemaTypeName)
        codeLines = []
        try:
            if hasattr(schemaType, 'kind') and schemaType.kind == TypeKind.UNION.name:
                codeLines = self.generate_union_code(schemaType, circularRefTypes)
            else:
                codeLines = self.generate_class_code(schemaType, circularRefTypes, objType, arguedName)

            if self.log_progress: logger.info(schemaTypeName + ' code extraction  completed')
            return codeLines
        except Exception as ex:
            logger.error('Error during extraction of type ' + schemaTypeName + ' - ' + ex.args[0])
            return []

    def generate_union_code(self, scType: SCType, circularRefTypes: dict[str,list[str]]):
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
            #         if argument[0] in circularRefTypes.keys() and scType.name + '.' + argument[0] in circularRefTypes[argument[0]]:
            #             singleLineCode += "'" + Translate.to_python_var_name(argument[0]) + "'" + ','
            #             self.removeFromCheckCircularTypes(argument[0], scType.name + '.' + argument[0], circularRefTypes)
            #             # circularRefTypes[argument[0]].remove(scType.name + '.' + argument[0])
            #             # if not circularRefTypes[argument[0]]:
            #             #     circularRefTypes.pop(argument[0])
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

    def generate_class_code(self, scType: SCType, circularRefTypes: dict[str,list[str]], objType: OperationType = OperationType.GENERIC_TYPE, arguedName: str = None):
        """For internal use"""
        scTypeName = scType.name if not arguedName else arguedName
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

            inlineCodeType, actualType = scType.compose_py_type()

            fieldsCodeList = []
            fieldsDocCodeList = []

            if isinstance(scType, SCField):
                fieldsCodeList = self.extract_schema_field_code(scType, objType, circularRefTypes)
            elif hasattr(scType, 'kind') and scType.kind == 'OBJECT': #fields
                    fieldsDocCodeList, fieldsCodeList =  self.extract_schema_type_content(scType, circularRefTypes, actualType, 'fields')
            elif hasattr(scType, 'kind') and scType.kind == 'INTERFACE':
                    fieldsDocCodeList, fieldsCodeList =  self.extract_schema_type_content(scType, circularRefTypes, actualType, 'fields')
                    # if scType.possibleTypes:
                    #     possibleTypes =  self.extract_schema_possible_types(scType)
            elif hasattr(scType, 'kind') and  scType.kind == 'INPUT_OBJECT': #inputFields
                    fieldsDocCodeList, fieldsCodeList =  self.extract_schema_type_content(scType, circularRefTypes, actualType, 'inputFields')

            if self.add_desc and fieldsDocCodeList: docsLst.extend(fieldsDocCodeList)
            classCodeLst.extend(fieldsCodeList)

            if not arguedName:
                    if hasattr(scType, 'type') and scType.type:
                        # if objType == OperationType.GENERIC_TYPE:
                            classCodeLst.append(self.indent + "type: " + inlineCodeType)
                        # elif objType == OperationType.QUERY or objType == OperationType.MUTATION: ##field type consists in the content of the query/mutation
                        #     typeContent = self.getExtractedContent(inlineCodeType)
                        #     for typeContentLine in typeContent[1,]:
                        #         codeLst.append(typeContentLine)
                        #     pass
            else:
                if actualType in STRING_PRIMITIVES:
                    scalarCodeLine = self.generate_scalar(scType)
                    self.extractionResults.scalarDefinitions.update({ scType.name: scalarCodeLine })

            try:
                scTypeName = actualType if actualType not in STRING_PRIMITIVES and objType == OperationType.GENERIC_TYPE else scType.name
                signature = self.generate_type_signature(objType, scTypeName, arguedName, possibleTypes, circularRefTypes)
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

    def extract_schema_field_code(self, scType, objType: OperationType, circularRefTypes):
        codeLst = []

        if hasattr(scType, 'args') and scType.args:
            scType.type_defs = scType.get_objtype_defs()
            actualType = scType.compose_py_type()[1]
            arguedClassName = actualType + "Args"
            parentClass = GQLArgsSet.__name__
            codeLst.append(self.indent + "class " + arguedClassName + "(" + parentClass + ", GQLObject): ")

            queryArgDocLst = []
            queryArgCodeLst = []
            for argument in scType.args:

                try:
                    docLine, codeLine = self.extract_element_content(argument, scType, circularRefTypes)
                    if self.add_desc and docLine: queryArgDocLst.append(docLine)
                    queryArgCodeLst.append(codeLine)

                except Exception as ex:
                    logger.error('Error during extraction of schema field element ' + argument.name + ' - ' + ex.args[0])

            if self.add_desc and queryArgDocLst:
                codeLst.append(self.indent + self.indent + '"""')
                codeLst.extend(list(map(lambda el: self.indent + el, queryArgDocLst)))
                codeLst.append(self.indent + self.indent + '"""')
            codeLst.extend(list(map(lambda el: self.indent + el, queryArgCodeLst)))
            codeLst.append('\n' + self.indent + '_args: ' + arguedClassName)
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

    def extract_schema_type_content(self, scType, circularRefTypes, actualType, contentName):
        codeLst = []
        docsLst = []
        try:
            if hasattr(scType, contentName):
                content = getattr(scType, contentName)
                if not content: return [scType.name + ' = ' + actualType]

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
                        docLine, codeLine = self.extract_element_content(element, scType, circularRefTypes)
                        if self.add_desc and docLine: docsLst.append(docLine)
                        codeLst.append(codeLine)

                    except Exception as ex:
                        logger.error('Error during extraction of content of element ' + element.name + ' for schema Type ' + scType.name + ' - ' + ex.args[0])

        except Exception as ex:
            logger.error('Error during extraction of schema Type content ' + element.name + ' - ' + ex.args[0])
        return docsLst, codeLst

    def extract_element_content(self, element, parentType, circularRefTypes):
        docLine = ''
        codeLine = ''

        try:
            if self.add_desc:
                if hasattr(element, 'description') and element.description:
                    docLine = self.indent + element.name + ' - ' + element.description + '\n'

            element.type_defs = element.get_objtype_defs()
            claimedElType, actualElType = element.compose_py_type()

            arguedName = None

            if hasattr(element, 'args') and element.args:
                ## Goes back up to construct an object
                ## Argued class name -> 5 chars random & field name & "_" parent class Name & "_Field"
                arguedName = ''.join(random.choices(string.ascii_uppercase, k=5)) + element.name + '_' + (actualElType if not actualElType in STRING_PRIMITIVES else element.name) + ARGUED_SIGNATURE_SUFFIX
                ##CAREFUL HERE - Pass element.name as usedTypes in extract_schema_type
                self.extract_schema_type(element, circularRefTypes, arguedName)

            if element.get_used_GQL_objnames() and circularRefTypes:
                circTypeUtilizer = self.start_check_circular_ref_types(element, parentType, actualElType, circularRefTypes)

                if circTypeUtilizer:
                    claimedElType = claimedElType.replace(actualElType, "NewType('" + actualElType + "', GQLObject)")

                    codeLine = self.indent + Translate.to_python_var_name(element.name) + ": " + (claimedElType if not arguedName else arguedName)
                    codeLine += ' ## Circular Reference for ' + actualElType

                    self.removeFromCheckCircularTypes(actualElType, circTypeUtilizer, circularRefTypes)
                else:
                    codeLine = self.indent + Translate.to_python_var_name(element.name) + ': ' + (claimedElType if not arguedName else arguedName)
            else:
                codeLine = self.indent + Translate.to_python_var_name(element.name) + ': ' + (claimedElType if not arguedName else arguedName)

        except Exception as ex:
            logger.error('Error during extraction of element ' + element.name + ' - ' + ex.args[0])

        return docLine, codeLine

    def generate_type_signature(self, objType: OperationType, scTypeName, arguedName, possibleTypes, circularRefTypes):
        if not arguedName:
            if not possibleTypes:
                if objType == OperationType.QUERY:
                    return QUERY_SIGNATURE%scTypeName + ':'
                if objType == OperationType.MUTATION:
                    return MUTATION_SIGNATURE%scTypeName + ':'
                else:
                    return CLASS_SIGNATURE%scTypeName + ':'
            else:
                return INTERFACE_SIGNATURE%(scTypeName, possibleTypes) + ':'
        else:
            if scTypeName not in STRING_PRIMITIVES and scTypeName not in self.extractionResults.scalarDefinitions.keys():
                if scTypeName in circularRefTypes.keys() and arguedName in circularRefTypes[scTypeName]:
                    ##creates circular ref type
                    circularRefCodeLine = scTypeName + ' = TypeVar(\'' + scTypeName + '\', bound=GQLObject)'
                    self.extractionResults.circularRefs.update({ scTypeName: circularRefCodeLine })
                    #update signature with circular ref management
                    signature = ARGUED_CLASS_SIGNATURE%(arguedName, "Generic[" + scTypeName + "]") + ':'
                    self.removeFromCheckCircularTypes(scTypeName, arguedName, circularRefTypes )
                    return signature
            else:
                try:
                    scalar = self.extractionResults.scalarDefinitions[scTypeName]
                    scalar = scalar.split('##')[0].split('=')[1].strip()
                except Exception as ex:
                    raise Exception('Error during scalar code string extrapolation - ' + ex.args[0])

                gqlArguedScalar = 'Argued' + scalar.capitalize()
                return ARGUED_CLASS_SIGNATURE%(arguedName, gqlArguedScalar) + ':'

            if scTypeName in self.extractionResults.circularRefs.keys() and \
               not self.is_already_extracted(scTypeName, includeCircularRefs=False):
                return ARGUED_CLASS_SIGNATURE%(arguedName, "Generic[" + scTypeName + "]") + ':'
            else:
                return ARGUED_CLASS_SIGNATURE%(arguedName, scTypeName) + ':'

    def extract_used_types(self, scType: SCType):
        """For internal use

        Args:
            scType (SCType): schema type to check

        Returns: dictionary containing used type names and number of occurrences
        """
        if self.log_progress: logger.info('Started extraction of used types for ' + scType.name)
        objNames = {}

        fieldsList = scType.get_valid_fields_lst()

        try:
            for field in fieldsList:
                objNames.update({ field.name: field.get_used_GQL_objnames() })
                if self.log_progress and objNames: logger.info('Found used Types: ' + str(objNames) + 'for field ' + field.name)

        except Exception as ex:
            logger.error('Error during extraction of used Types for ' + field.name + ' - ' + ex.args[0])

        if self.log_progress: logger.info('Used types for ' + scType.name + ' extracted')
        return objNames

    def start_check_circular_ref_types(self, element, parentType, actualElType, circularRefTypes):
        if circTypeUtilizers:= circularRefTypes.get(actualElType):

                for circTypeUtilizer in circTypeUtilizers:
                    circType, circTypeField = circTypeUtilizer.split('.')

                    if parentType.name == circType and element.name == circTypeField:
                        return circTypeUtilizer

        return None

    def removeFromCheckCircularTypes(self, actualElType, circTypeUtilizer, circularRefTypes):
        circularRefTypes[actualElType].remove(circTypeUtilizer)
        if not circularRefTypes[actualElType]:
            circularRefTypes.pop(actualElType)
