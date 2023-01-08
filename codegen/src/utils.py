from collections import deque
import os
import pathlib
from .enums import TypeKind

##, TypeKind.ENUM.name could be a big mess
gqlTypeKinds = (TypeKind.INPUT_OBJECT.name, TypeKind.INTERFACE.name, TypeKind.OBJECT.name, TypeKind.UNION.name)
typesByName = [TypeKind.INPUT_OBJECT.name, TypeKind.OBJECT.name, TypeKind.INTERFACE.name, TypeKind.SCALAR.name, TypeKind.ENUM.name, TypeKind.UNION.name]
    
def performanceProfilerLog():
    return  open('test/logs/performance analysis.log', 'w')
    
def splitTypes(dictionary: dict[str, any]):
    myDeque = deque()
    simpleTypes = []
    while dictionary:
        try:
            currentItem = dictionary.popitem()
            currUsedTypes = 0
            for field in currentItem[1].getValidFieldsList():
                currUsedTypes +=  len(field.getUsedGQLObjectNames())
            if currUsedTypes == 0:
                simpleTypes.append(currentItem)
            else:
                minUT = len(myDeque[0][1].getUsedGQLObjectNames()) if myDeque else 1
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
            # else:
            #     raise Exception('Invalid folder:' + str(input_path))
    except Exception as ex:
        raise ex
    
    return str(input_path)

def isDeprecated(obj):
    return hasattr(obj, 'isDeprecated') and obj.isDeprecated
                    