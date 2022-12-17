from collections import deque
import copy
import os
import pathlib
from .enums import TypeKind

##, TypeKind.ENUM.name could be a big mess
gqlTypeKinds = (TypeKind.INPUT_OBJECT.name, TypeKind.INTERFACE.name, TypeKind.OBJECT.name, TypeKind.UNION.name)
typesByName = [TypeKind.INPUT_OBJECT.name, TypeKind.OBJECT.name, TypeKind.INTERFACE.name, TypeKind.SCALAR.name, TypeKind.ENUM.name, TypeKind.UNION.name]
    
def getUsedGQLObjectNames(scType, gqlTypeNameListParam:list = []):
    gqlTypeNameList = copy.deepcopy(gqlTypeNameListParam)
    if hasattr(scType, 'kind') and scType.kind and scType.kind in gqlTypeKinds:
        gqlTypeNameList.append(scType.name)
    if hasattr(scType, 'ofType') and scType.ofType:
        return getUsedGQLObjectNames(scType.ofType, gqlTypeNameList)
    if hasattr(scType, 'type') and scType.type:
        return getUsedGQLObjectNames(scType.type, gqlTypeNameList)
    
    return gqlTypeNameList
        
def getObjectTypeDefs(scType, typeDefListParam = []):
    try:
        typeDefList = copy.deepcopy(typeDefListParam)
        if hasattr(scType, 'kind') and scType.kind:
            if scType.kind in typesByName:
                typeDefList.append(scType.name)
            else:
                typeDefList.append(scType.kind)
        if hasattr(scType, 'ofType') and scType.ofType:
            return getObjectTypeDefs(scType.ofType, typeDefList)
        if hasattr(scType, 'type') and scType.type:
            return getObjectTypeDefs(scType.type, typeDefList)
    except Exception as ex:
        raise Exception('Error during etraction of object type definitions' + ' - ' + ex.args[0])
    return typeDefList

def getValidFieldsList(scType: any):
    try:
        if hasattr(scType, 'args') and scType.args: ##Schema Field
                return scType.args
        elif hasattr(scType, 'fields') and scType.fields: ##OBJECT, INTERFACE
                return scType.fields
        elif hasattr(scType, 'inputFields') and scType.inputFields: ##INPUT_OBJECT
                return scType.inputFields
        elif hasattr(scType, 'possibleTypes') and scType.possibleTypes: ##UNION
                return scType.possibleTypes.values()
        else: ##No list of fields
            return []
    except Exception as ex:
        raise Exception('Error getting fields list for type ' + scType.name + ' - ' + ex.args[0])

def performanceProfilerLog():
    ppFile = open('test/logs/performance analysis.log', 'w')
    return ppFile
    
def splitDictionary(dictionary: dict[str, any]):
    myDeque = deque()
    simpleTypes = []
    while dictionary:
        try:
            currentItem = dictionary.popitem()
            currUsedTypes = 0
            fields = getValidFieldsList(currentItem[1])
            for field in fields:
                currUsedTypes +=  len(getUsedGQLObjectNames(field))
            if currUsedTypes == 0:
                simpleTypes.append(currentItem)
            else:
                minUT = len(getUsedGQLObjectNames(myDeque[0][1])) if myDeque else 1
                if currUsedTypes <= minUT:
                    myDeque.appendleft(currentItem)
                else:
                    myDeque.append(currentItem)
        except Exception as ex:
            raise Exception('Error during split of types - ' + ex.args[0])
            
    return dict(simpleTypes), dict(myDeque)

def getValidFolder(folder):
    try:
        input_path = pathlib.Path(folder).absolute()
        
        if not input_path.exists():
            if input_path.parent.absolute().exists():
                os.mkdir(input_path)
            else:
                raise Exception('Invalid folder:' + folder)
    except Exception as ex:
        raise
    
    return str(input_path)


def isDeprecated(obj):
    return hasattr(obj, 'isDeprecated') and obj.isDeprecated
                    