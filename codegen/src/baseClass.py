import copy
import logging as logger
from pygqlmap.src.translator import Translate
from .enums import TypeKind
from .utils import gqlTypeKinds, typesByName

class TypeManager():
    
    def composePythonType(self) -> str:
        isNonNull = False
        isList = False
        isCustomScalar = False
        typeOutput = ''
        
        if not self.typeDefs:
            logger.error('Need to extract type definition first')
        for typeDef in self.typeDefs:
            try:
                currentType = Translate.toPythonTypeOrOriginal(typeDef)
                if currentType == TypeKind.NON_NULL.name: 
                    isNonNull = True
                    continue
                elif currentType == TypeKind.LIST.name: 
                    isList = True
                    continue
                
                typeOutput += currentType
                
            except Exception as ex:
                raise Exception('Error during composition of type ' + typeDef + ' for ' + self.name + ' - ' + ex.args[0])
            
        if isNonNull: typeOutput += ' ##NON NULL' 
        if isList: typeOutput += ' ##LIST' 
        if isCustomScalar: typeOutput += ' ##'+ typeDef + '##' 
        
        self.typeDefs.clear()
        return typeOutput, currentType

    def getUsedGQLObjectNames(self, gqlTypeNameListParam:list = None):
        try:
            if gqlTypeNameListParam == None: gqlTypeNameListParam = []
            gqlTypeNameList = copy.deepcopy(gqlTypeNameListParam)
            if hasattr(self, 'kind') and self.kind and self.kind in gqlTypeKinds:
                gqlTypeNameList.append(self.name)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.getUsedGQLObjectNames(gqlTypeNameList)
            if hasattr(self, 'type') and self.type:
                return self.type.getUsedGQLObjectNames(gqlTypeNameList)
        except Exception as ex:
            raise Exception('Error during etraction of used object GraphQL names' + ' - ' + ex.args[0])
        
        return gqlTypeNameList
            
    def getObjectTypeDefs(self, typeDefListParam = None):
        if typeDefListParam == None: typeDefListParam = []
        typeDefList = copy.deepcopy(typeDefListParam)
        
        try:
            if hasattr(self, 'kind') and self.kind:
                if self.kind in typesByName:
                    typeDefList.append(self.name)
                else:
                    typeDefList.append(self.kind)
            if hasattr(self, 'ofType') and self.ofType:
                return self.ofType.getObjectTypeDefs(typeDefList)
            if hasattr(self, 'type') and self.type:
                return self.type.getObjectTypeDefs(typeDefList)
        except Exception as ex:
            raise Exception('Error during etraction of object type definitions' + ' - ' + ex.args[0])
        
        return typeDefList

    def getValidFieldsList(self):
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
