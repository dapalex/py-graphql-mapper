from pygqlmap.src.consts import primitivesStringified
from pygqlmap.enums import OperationType
from pygqlmap.src.logger import Logger
from pygqlmap.src.translator import Translate, switchStrType
from .enums import TypeKind
from .spSchema import GQLSchema, SCField, SCType
from .utils import isDeprecated, splitTypes
from .priority import ExtractionResults, PriorElement
from .consts import scalarSignature, classSignature, enumSignature, arguedClassSignature, interfaceSignature

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
    addDescription: bool
    logProgress: bool
    
    def __init__(self, schema, customTypes = [], logProgress: bool = False, addDescription: bool = False):
        self.logProgress = logProgress
        self.addDescription = addDescription
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
        self.customTypes = customTypes
        
        if customTypes:
            switchStrType.update(customTypes)
        
        self.priorList = []
        
        super().__init__()
    
    def extractSchemaCode (self):
        try:
            self.extractTypesFromGQLSchema()
            
            self.extractionResults.scalarDefinitions = self.extractScalars()
            self.extractionResults.enumClasses = self.extractEnums()
            self.extractionResults.simpleTypeClasses = self.extractsimpleTypes()
            self.extractionResults.typeClasses = self.extractTypes()
            if hasattr(self, 'queries') and self.queries: 
                self.extractionResults.queryClasses, self.queriesEnumValues = self.extractOperations(OperationType.query, self.queries)
            
            if hasattr(self, 'mutations') and self.mutations: 
                self.extractionResults.mutationClasses, self.mutationsEnumValues = self.extractOperations(OperationType.mutation, self.mutations)
            
            #create Mutations Enum
            self.extractionResults.queriesEnumClass = self.extractOperationsEnum(OperationType.query, self.queriesEnumValues)
            self.extractionResults.mutationsEnumClass = self.extractOperationsEnum(OperationType.mutation, self.mutationsEnumValues)
        except Exception as ex:
            Logger.logErrorMessage('Error during Schema code extraction' + ' - ' + ex.args[0])
            
        return self.extractionResults

    def extractTypesFromGQLSchema(self):
        """For internal use
        
        Populates the CodeGenerator object lists
           - enums
           - mutations
           - types
        """
        try:
            if self.logProgress: Logger.logInfoMessage('Started extraction of types')
            tempTypes = {}
            while self.schema.types: 
                currentType = self.schema.types.popitem()
                if self.logProgress: Logger.logInfoMessage('Started extraction of type ' + currentType[0])
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
                    
            self.simpleTypes, self.types = splitTypes(tempTypes)
        except Exception as ex:
            Logger.logErrorMessage('Error during GQL schema types extraction - ' + ex.args[0]) 
    
    def extractScalars(self):
        scalarDefinitions = {}
        try:
            if self.logProgress: Logger.logInfoMessage('Started extraction of scalars')
            while self.scalars: 
                schemaScalar = self.scalars.popitem()[1]
                
                scalarCodeLine = self.generateScalar(schemaScalar)
                scalarDefinitions.update({ schemaScalar.name: scalarCodeLine })
        except Exception as ex:
            Logger.logErrorMessage('Error during transformation of CodeGenerator enums' + ' - ' + ex.args[0])
        
        return scalarDefinitions
    
    def generateScalar(self, schemaScalar: SCType):
        if self.logProgress: Logger.logInfoMessage('Started extraction of scalar ' + schemaScalar.name)
        schemaScalar.typeDefs = schemaScalar.getObjectTypeDefs() 

        if schemaScalar.name in switchStrType: 
            scalarType = switchStrType[schemaScalar.name]
        else:
            scalarType, actualType = schemaScalar.composePythonType()
            if scalarType not in primitivesStringified: 
                scalarType = 'str'
            
        scalarCodeLine = scalarSignature%(schemaScalar.name,scalarType)                
        
        if self.addDescription and schemaScalar.description: 
                scalarCodeLine +=  ' ##' + schemaScalar.description.replace('\n', ' - ')
            
        if self.logProgress: Logger.logInfoMessage(schemaScalar.name + 'scalar extracted')
        
        return scalarCodeLine
    
    def extractEnums(self):
        """For internal use"""
        enumClasses = {}
        
        try:
            if self.logProgress: Logger.logInfoMessage('Started extraction of enums')
            while self.enums: 
                schemaEnum = self.enums.popitem()[1]
                
                if not list(filter(lambda ev: not hasattr(ev, 'isDeprecated') or ev.isDeprecated == False, schemaEnum.enumValues)): continue
                
            # for schemaEnum in self.enums:
                if self.logProgress: Logger.logInfoMessage('Started extraction of enum ' + schemaEnum.name)
                enumCodeLst = []
                enumCodeLst.append(enumSignature%schemaEnum.name + ':')
                
                
                if self.addDescription:
                    if schemaEnum.description: 
                        enumCodeLst.append(self.indent + '"""')
                        enumCodeLst.append(self.indent + schemaEnum.name + ' - ' + schemaEnum.description + '\n')
                        enumCodeLst.append(self.indent + '"""')
                    
                for enumValue in schemaEnum.enumValues:
                    
                    if isDeprecated(enumValue): continue
                    
                    codeLine = self.indent + Translate.toPythonVariableName(enumValue.name) + ' = \'' + enumValue.name + '\''
                    if hasattr(enumValue, 'description') and enumValue.description:
                        codeLine += ' ##' + enumValue.description
                    enumCodeLst.append(codeLine)
                
                if self.logProgress: Logger.logInfoMessage(schemaEnum.name + 'enum extracted')
                enumClasses.update({ schemaEnum.name: enumCodeLst })
        except Exception as ex:
            Logger.logErrorMessage('Error during transformation of CodeGenerator enums' + ' - ' + ex.args[0])
        
        return enumClasses
    
    def extractsimpleTypes(self):
        """For internal use"""
        simpleTypeClasses = {}
        
        if self.logProgress: Logger.logInfoMessage('Started extraction of types')
        try:
            while self.simpleTypes:
                currentTypeKV = self.simpleTypes.popitem()
                
                if self.logProgress: Logger.logInfoMessage('Started extraction of type ' + currentTypeKV[0])
                self.extractSchemaType(currentTypeKV[1])
        
            for priorElement in self.priorList:
                
                if not priorElement.codeList: 
                    Logger.logErrorMessage('No body for simple type ' + priorElement.name)
                    
                ##force recheck?
                simpleTypeClasses.update({ priorElement.name: priorElement.codeList })
                self.priorList.remove(priorElement)
            if self.logProgress: Logger.logInfoMessage('Extraction of simpleTypes completed')
        except Exception as ex:
            Logger.logErrorMessage('Error during transformation of CodeGenerator simpleTypes' + ' - ' + ex.args[0])
            
        return simpleTypeClasses
    
    def extractTypes(self):
        """For internal use"""
        typeClasses = {}
        if self.logProgress: Logger.logInfoMessage('Started extraction of types')
        try:
            while self.types:
                currTypeKV = self.types.popitem()
                
                if self.logProgress: Logger.logInfoMessage('Started extraction of type ' + currTypeKV[0])
                self.extractSchemaType(currTypeKV[1])
        
            for priorElement in self.priorList:
                if not priorElement.codeList: 
                    Logger.logErrorMessage('No body for type ' + priorElement.name)
                    
                ##recheck for generated classes
                if priorElement.name.endswith('Field'):
                    realType = False
                    
                    priorElement.schemaType.typeDefs = priorElement.schemaType.getObjectTypeDefs() 
                    
                    if TypeKind.LIST.name in priorElement.schemaType.typeDefs: isList = True
                    
                    claimedType, actualType = priorElement.schemaType.composePythonType()

                    if actualType in primitivesStringified or actualType in self.extractionResults.scalarDefinitions.keys():
                        for objNameList in self.extractUsedTypes(priorElement.schemaType).values():
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
            if self.logProgress: Logger.logInfoMessage('Extraction of types completed')
        except Exception as ex:
            Logger.logErrorMessage('Error during transformation of CodeGenerator types' + ' - ' + ex.args[0])
            
        return typeClasses
    
    def extractOperations(self, opType: OperationType, operations: list):
        """For internal use"""
        operationClasses = {}
        operationEnumValues = []
        try:
            if self.logProgress: Logger.logInfoMessage('Started extraction of ' + opType.name)
            
            for operation in operations.fields:
                if self.logProgress: Logger.logInfoMessage('Started extraction of ' + opType.name + ' ' + operation.name)
                try:
                    operationCode = self.extractTypeCode(operation, objType=opType)
                    operationClasses.update({ operation.name : operationCode })
                    operationEnumValues.append(operation.name) 
                except Exception as ex:
                    Logger.logErrorMessage('Error during extraction of ' + opType.name + ' ' + operation.name + ' - ' + ex.args[0]) 
                     
                if self.logProgress: Logger.logInfoMessage(operation.name + ' extracted')
        except Exception as ex:
            Logger.logErrorMessage('Error during transformation of CodeGenerator operations' + ' - ' + ex.args[0])
        
        return operationClasses, operationEnumValues
    
    def extractOperationsEnum(self, opType: OperationType, operationsEnumValues):
        """For internal use"""
        operationKey = 'Queries' if opType == OperationType.query else 'Mutations'
        operationEnumClass = {}
        if self.logProgress: Logger.logInfoMessage('Started generation of ' + operationKey + ' enum')
        enumCodeLst = []
        
        enumCodeLst.append(enumSignature%operationKey + ':')
        
        for enumValue in operationsEnumValues:
            enumCodeLst.append(self.indent + enumValue + ' = ' + enumValue)
        
        operationEnumClass.update({ operationKey: enumCodeLst })
        if self.logProgress: Logger.logInfoMessage(operationKey + ' enum generated')
        
        return operationEnumClass
    
    def extractSchemaType(self, currentType, circularRefTypes: dict[str, list[str]] = {}, arguedName: str = None):
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
        if self.logProgress: Logger.logInfoMessage('Started extraction of type ' + currentTypeName)
        
        if self.isAlreadyExtracted(currentTypeName):
            Logger.logWarningMessage(currentTypeName + " already extracted!")
            return
        
        usedTypes = []
        try:
            usedTypes = self.extractUsedTypes(currentType)
            usedTypesDict = {}
            for objNameList in usedTypes.values():
                for objName in objNameList:
                    if objName not in usedTypesDict.keys():
                        usedTypesDict.update({ objName: 1 })
                    else:
                        usedTypesDict[objName] += 1 
                    
            if arguedName: 
                usedTypesDict.update({ arguedName.removesuffix('Field'): 1 })
            
            for usedTypeNameKey, occurrences in usedTypesDict.items():
                try:
                    if self.logProgress: Logger.logInfoMessage(currentTypeName + ' uses ' + usedTypeNameKey)
                    if self.isAlreadyExtracted(usedTypeNameKey):
                        Logger.logWarningMessage(currentTypeName + " already extracted!") 
                        continue
                    elif self.types.get(usedTypeNameKey): 
                        poppedUsedType = self.types.pop(usedTypeNameKey)
                        
                        if self.logProgress: Logger.logInfoMessage('Call extraction for ' + usedTypeNameKey)
                        
                        self.extractSchemaType(poppedUsedType, circularRefTypes)
                    else:
                        # It can be a circular reference
                        if self.logProgress: Logger.logInfoMessage('Used type ' + usedTypeNameKey + ' for ' + currentTypeName + ' not found in already managed types, it can be a circular reference')
                        
                        utilizers = []
                        
                        for fieldName, usedTypeList in usedTypes.items():
                            if usedTypeNameKey in usedTypeList:
                                utilizers.append(currentType.name + '.' + fieldName)
                                
                        if arguedName:
                                utilizers.append(arguedName)
                                    
                        if usedTypeNameKey == currentType.name and occurrences == 0:
                            Logger.logErrorMessage('inconsistence')
                            
                        if not usedTypeNameKey in circularRefTypes.keys(): 
                            circularRefTypes.update({ usedTypeNameKey: utilizers }) 
                        else:
                            if not currentType.name in circularRefTypes[usedTypeNameKey]: 
                                circularRefTypes[usedTypeNameKey].extend(utilizers)
                                
                except Exception as ex:
                    Logger.logErrorMessage('Error during management of used type ' + usedTypeNameKey + ' - ' + ex.args[0])   
            
            typeCode = self.extractTypeCode(currentType, circularRefTypes, arguedName=arguedName)

            if typeCode:
                pqElement = PriorElement(currentTypeName, currentType, typeCode)
            
                if self.logProgress: Logger.logInfoMessage(currentTypeName + ' type extracted')
                if self.logProgress: Logger.logInfoMessage('Appending extracted ' + currentTypeName)
                self.priorList.append(pqElement)
            else:
                Logger.logWarningMessage('Type ' + currentTypeName + ' not extracted') 
                
        except Exception as ex:
            Logger.logErrorMessage('Error during extraction of type ' + currentTypeName + ' - ' + ex.args[0])   
          
          
    def isAlreadyExtracted(self, checkTypeName):
        if checkTypeName in self.extractionResults.scalarDefinitions.keys(): 
            return True
        if checkTypeName in self.extractionResults.enumClasses.keys(): 
            return True
        elif checkTypeName in self.extractionResults.simpleTypeClasses.keys():
            return True
        elif checkTypeName in self.extractionResults.circularRefs.keys():
            return True
        else:
            for x in self.priorList:
                if checkTypeName == x.name:
                    return True #break from for
                
        return False
                        
    
    
    
    def extractTypeCode(self, schemaType, circularRefTypes = [], objType: OperationType = OperationType.genericType, arguedName:str = None):
        """For internal use"""
        schemaTypeName = schemaType.name if not arguedName else arguedName
        if self.logProgress: Logger.logInfoMessage('Started extraction of code for ' + schemaTypeName)
        codeLines = []
        try:
            if hasattr(schemaType, 'kind') and schemaType.kind == TypeKind.UNION.name: 
                codeLines = self.generateUnionCode(schemaType, circularRefTypes)
            else:                
                codeLines = self.generateClassCode(schemaType, circularRefTypes, objType, arguedName)
                                    
            if self.logProgress: Logger.logInfoMessage(schemaTypeName + ' code extraction  completed')
            return codeLines
        except Exception as ex:
            Logger.logErrorMessage('Error during extraction of type ' + schemaTypeName + ' - ' + ex.args[0]) 
            return []
    
    def generateUnionCode(self, scType: SCType, circularRefTypes: dict[str,list[str]]):
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
            #             singleLineCode += "'" + Translate.toPythonVariableName(argument[0]) + "'" + ','
            #             self.removeFromCheckCircularTypes(argument[0], scType.name + '.' + argument[0], circularRefTypes)
            #             # circularRefTypes[argument[0]].remove(scType.name + '.' + argument[0])
            #             # if not circularRefTypes[argument[0]]:
            #             #     circularRefTypes.pop(argument[0])
            #         else:
            #             singleLineCode += Translate.toPythonVariableName(argument[0]) + ', ' 
                
            #     except Exception as ex:
            #         Logger.logErrorMessage('Error during extraction of element ' + argument[0] + ' - ' + ex.args[0])
            
            # singleLineCode = singleLineCode.removesuffix(',')
            
            # if multipleTypes:
            #     singleLineCode += ']'
            
            # if self.addDescription and scType.description:
            #         codeLst.append('"""\n' + scType.description + '\n"""\n')
            codeLst.append(singleLineCode)
        
        except Exception as ex:
            Logger.logErrorMessage('Error during extraction of content for type ' + scType.name + ' - ' + ex.args[0])

        return codeLst
    
    def generateClassCode(self, scType: SCType, circularRefTypes: dict[str,list[str]], objType: OperationType = OperationType.genericType, arguedName: str = None):
        """For internal use"""
        scTypeName = scType.name if not arguedName else arguedName
        if self.logProgress: Logger.logInfoMessage('Started generation of class for ' + scTypeName)
        classCodeLst = []
        docsLst = []
        returnCodeList = []
        isList = False
        possibleTypes = None
        
        try:
            if self.addDescription:
                if hasattr(scType, 'description') and scType.description: 
                    docsLst.append(self.indent + scTypeName + ' - ' + scType.description + '\n')
                    
            scType.typeDefs = scType.getObjectTypeDefs() 
            
            if TypeKind.LIST.name in scType.typeDefs: isList = True
            
            claimedType, actualType = scType.composePythonType()
            arguedPrimitive = actualType in primitivesStringified
            
            if not arguedName:
                if isList:
                    return [scTypeName + ' = list[' + actualType + ']']
            
                if arguedPrimitive: #TEMP - with NOT NULL managed should disappear
                    return [scTypeName + ' = ' + actualType]
            
            fieldsCodeList = []
            fieldsDocCodeList = []
            
            if type(scType) == SCField:
                fieldsCodeList = self.extractSchemaFieldCode(scType, objType, circularRefTypes)
            elif hasattr(scType, 'kind') and scType.kind == 'OBJECT': #fields
                    fieldsDocCodeList, fieldsCodeList =  self.extractSchemaTypeContent(scType, circularRefTypes, actualType, 'fields')
            elif hasattr(scType, 'kind') and scType.kind == 'INTERFACE':
                    fieldsDocCodeList, fieldsCodeList =  self.extractSchemaTypeContent(scType, circularRefTypes, actualType, 'fields')
                    # if scType.possibleTypes:
                    #     possibleTypes =  self.extractSchemaPossibleTypes(scType)
            elif hasattr(scType, 'kind') and  scType.kind == 'INPUT_OBJECT': #inputFields
                    fieldsDocCodeList, fieldsCodeList =  self.extractSchemaTypeContent(scType, circularRefTypes, actualType, 'inputFields')
            
            if self.addDescription and fieldsDocCodeList: docsLst.extend(fieldsDocCodeList)
            classCodeLst.extend(fieldsCodeList)
            
            if not arguedName:
                    if hasattr(scType, 'type') and scType.type:
                        # if objType == OperationType.genericType:
                            classCodeLst.append(self.indent + "type: " + claimedType) 
                        # elif objType == OperationType.query or objType == OperationType.mutation: ##field type consists in the content of the query/mutation
                        #     typeContent = self.getExtractedContent(claimedType)
                        #     for typeContentLine in typeContent[1,]:
                        #         codeLst.append(typeContentLine) 
                        #     pass
            else:
                if actualType in primitivesStringified:
                    scalarCodeLine = self.generateScalar(scType)
                    self.extractionResults.scalarDefinitions.update({ scType.name: scalarCodeLine })
            
            try:
                scTypeName = actualType if actualType not in primitivesStringified and objType == OperationType.genericType else scType.name
                signature = self.generateTypeSignature(scTypeName, arguedName, possibleTypes, circularRefTypes, arguedPrimitive)
            except Exception as ex:
                Logger.logErrorMessage('Error during creation of signature for type ' + scTypeName + ' - ' + ex.args[0])
                    
            if classCodeLst:
                returnCodeList.append(signature)
                if self.addDescription and docsLst:
                    returnCodeList.append(self.indent + '"""')
                    returnCodeList.extend(docsLst)
                    returnCodeList.append(self.indent + '"""')
                returnCodeList.extend(classCodeLst)
            else:
                Logger.logErrorMessage('Missing code for type ' + scTypeName)
        
            if self.logProgress: Logger.logInfoMessage(scTypeName + ' code generation completed')
            
        except Exception as ex:
            Logger.logErrorMessage('Error during extraction of content for type ' + scTypeName + ' - ' + ex.args[0])

        return returnCodeList
    
    def extractSchemaFieldCode(self, scType, objType: OperationType, circularRefTypes):
        codeLst = []
        
        if hasattr(scType, 'args') and scType.args:
            parentClass = "GQLArgsSet" if objType == OperationType.genericType else "GQLOperationArgs"
            codeLst.append(self.indent + "class Args(" + parentClass + "): ")
            
            queryArgDocLst = []
            queryArgCodeLst = []
            for argument in scType.args:
                                        
                try:
                    docLine, codeLine = self.extractElementContent(argument, scType, circularRefTypes)
                    if self.addDescription and docLine: queryArgDocLst.append(docLine)
                    queryArgCodeLst.append(codeLine)
                    
                except Exception as ex:
                    Logger.logErrorMessage('Error during extraction of schema field element ' + argument.name + ' - ' + ex.args[0])
            
            if self.addDescription and queryArgDocLst:
                codeLst.append(self.indent + self.indent + '"""')
                codeLst.extend(list(map(lambda el: self.indent + el, queryArgDocLst)))
                codeLst.append(self.indent + self.indent + '"""')
            codeLst.extend(list(map(lambda el: self.indent + el, queryArgCodeLst)))
            codeLst.append('\n' + self.indent + '_args: Args')
            codeLst.append('\n')
        
        return codeLst
    
    def extractSchemaPossibleTypes(self, scType):
        possibleTypes = ''
        for possibleTypeName, possibleType in scType.possibleTypes.items():
                
                ##check if the element is deprecated --> skip it
                if isDeprecated(possibleType): 
                    continue
                
                possibleTypes += "'" + possibleTypeName + "'" if not possibleTypes else (" or '" + possibleTypeName + "'")
        return possibleTypes
    
    def extractSchemaTypeContent(self, scType, circularRefTypes, actualType, contentName):
        codeLst = []
        docsLst = []
        
        if hasattr(scType, contentName):
            content = getattr(scType, contentName)
            if not content: return [scType.name + ' = ' + actualType]
            
            ##check if all elements are deprecated --> get out empty handed
            if not list(filter(lambda ev: not hasattr(ev, 'isDeprecated') or ev.isDeprecated == False, content)): 
                Logger.logWarningMessage('Type ' + scType.name + ' deprecated!')
                return [], []
            
            for element in content:
                
                ##check if the element is deprecated --> skip it
                if isDeprecated(element): 
                    continue
                
                try:
                    docLine, codeLine = self.extractElementContent(element, scType, circularRefTypes)
                    if self.addDescription and docLine: docsLst.append(docLine)
                    codeLst.append(codeLine)
                    
                except Exception as ex:
                    Logger.logErrorMessage('Error during extraction of schema Type content ' + element.name + ' - ' + ex.args[0])    
        
        return docsLst, codeLst  
    
    def extractElementContent(self, element, parentType, circularRefTypes):  
        docLine = ''  
        codeLine = ''
        found = False
        
        try:
            if self.addDescription:
                if hasattr(element, 'description') and element.description: 
                    docLine = self.indent + element.name + ' - ' + element.description + '\n'
                    
            element.typeDefs = element.getObjectTypeDefs() 
            claimedElType, actualElType = element.composePythonType()
            
            arguedNameRef = None
            
            if hasattr(element, 'args') and element.args: 
                ## Goes back up to construct an object
                arguedName = (actualElType if not actualElType in primitivesStringified else element.name) + 'Field'
                ##CAREFUL HERE - Pass element.name as usedTypes in extractSchemaType
                self.extractSchemaType(element, circularRefTypes, arguedName)
                arguedNameRef = claimedElType.replace(actualElType, (actualElType if not actualElType in primitivesStringified else element.name) + 'Field') 
            
            if element.getUsedGQLObjectNames() and circularRefTypes:
                circTypeUtilizer = self.startCheckCircularRefTypes(element, parentType, actualElType, circularRefTypes)
                    
                if circTypeUtilizer:
                    claimedElType = claimedElType.replace(actualElType, "NewType('" + actualElType + "', GQLObject)")
                    
                    codeLine = self.indent + Translate.toPythonVariableName(element.name) + ": " + (claimedElType if not arguedNameRef else arguedNameRef)
                    codeLine += ' ## Circular Reference for ' + actualElType
                    
                    self.removeFromCheckCircularTypes(actualElType, circTypeUtilizer, circularRefTypes)
                else:
                    codeLine = self.indent + Translate.toPythonVariableName(element.name) + ': ' + (claimedElType if not arguedNameRef else arguedNameRef)
            else:
                codeLine = self.indent + Translate.toPythonVariableName(element.name) + ': ' + (claimedElType if not arguedNameRef else arguedNameRef)
        
        except Exception as ex:
            Logger.logErrorMessage('Error during extraction of element ' + element.name + ' - ' + ex.args[0]) 
            
        return docLine, codeLine
                
    def generateTypeSignature(self, scTypeName, arguedName, possibleTypes, circularRefTypes, arguedPrimitive = False):
        if not arguedName:
            if not possibleTypes:
                return classSignature%scTypeName + ':' 
            else:
                return interfaceSignature%(scTypeName, possibleTypes) + ':'
        else:
            if scTypeName not in primitivesStringified and scTypeName not in self.extractionResults.scalarDefinitions.keys():
                if scTypeName in circularRefTypes.keys() and arguedName in circularRefTypes[scTypeName]:
                    ##creates circular ref type
                    circularRefCodeLine = scTypeName + ' = TypeVar(\'' + scTypeName + '\', bound=GQLObject)'
                    self.extractionResults.circularRefs.update({ scTypeName: circularRefCodeLine })
                    #update signature with circular ref management
                    signature = arguedClassSignature%(arguedName, "Generic[" + scTypeName + "]") + ':' 
                    self.removeFromCheckCircularTypes(scTypeName, arguedName, circularRefTypes )
                    return signature
            else:
                try:
                    scalar = self.extractionResults.scalarDefinitions[scTypeName]
                    scalar = scalar.split('##')[0].split('=')[1].strip()
                except Exception as ex:
                    raise Exception('Error during scalar code string extrapolation - ' + ex.args[0])
                
                gqlArguedScalar = 'Argued' + scalar.capitalize()
                return arguedClassSignature%(arguedName, gqlArguedScalar) + ':' 
                pass
        
            return arguedClassSignature%(arguedName, scTypeName) + ':' 
    
    def extractUsedTypes(self, scType: SCType):
        """For internal use

        Args:
            scType (SCType): schema type to check

        Returns: dictionary containing used type names and number of occurrences
        """
        if self.logProgress: Logger.logInfoMessage('Started extraction of used types for ' + scType.name)
        objNames = {}
                
        fieldsList = scType.getValidFieldsList()
        
        try:
            for field in fieldsList:
                objNames.update({ field.name: field.getUsedGQLObjectNames() })
                if self.logProgress and objNames: Logger.logInfoMessage('Found used Types: ' + str(objNames) + 'for field ' + field.name)
                
        except Exception as ex:
            Logger.logErrorMessage('Error during extraction of used Types for ' + field.name + ' - ' + ex.args[0])
        
        if self.logProgress: Logger.logInfoMessage('Used types for ' + scType.name + ' extracted')
        return objNames
    
    def startCheckCircularRefTypes(self, element, parentType, actualElType, circularRefTypes):
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
            