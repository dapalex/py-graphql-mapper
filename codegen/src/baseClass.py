from pygqlmap.src.logger import Logger
from pygqlmap.src.translator import Translate
from .enums import TypeKind

class TypeManager():
    
    def composePythonType(self) -> str:
        isNonNull = False
        isList = False
        isCustomScalar = False
        typeOutput = ''
        
        if not self.typeDefs:
            Logger.logErrorMessage('Need to extract type definition first')
        for typeDef in self.typeDefs:
            try:
                currentType = Translate.toPythonTypeOrOriginal(typeDef)
                if currentType == TypeKind.NON_NULL.name: 
                    isNonNull = True
                    continue
                elif currentType == TypeKind.LIST.name: 
                    typeOutput += 'list['
                    isList = True
                    continue
                
                typeOutput += currentType
                
                if isList: 
                    typeOutput += ']'
                    isList = False
            except Exception as ex:
                raise Exception('Error during composition of type ' + typeDef + ' for ' + self.name + ' - ' + ex.args[0])
            
        if isNonNull: typeOutput += ' ##NON NULL' 
        if isCustomScalar: typeOutput += ' ##'+ typeDef + '##' 
        
        self.typeDefs.clear()
        return typeOutput, currentType
