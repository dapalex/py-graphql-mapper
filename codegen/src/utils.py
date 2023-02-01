from collections import deque
import os
import pathlib
from .enums import TypeKind

##, TypeKind.ENUM.name could be a big mess
gqlTypeKinds = (TypeKind.INPUT_OBJECT.name, TypeKind.INTERFACE.name, TypeKind.OBJECT.name, TypeKind.UNION.name)
typesByName = [TypeKind.INPUT_OBJECT.name, TypeKind.OBJECT.name, TypeKind.INTERFACE.name, TypeKind.SCALAR.name, TypeKind.ENUM.name, TypeKind.UNION.name]

def perf_profile_log():
    return  open('test/logs/performance analysis.log', 'w')

def split_types(dictionary: dict[str, any]):
    myDeque = deque()
    simpleTypes = []
    while dictionary:
        try:
            currentItem = dictionary.popitem()
            currUsedTypes = 0
            for field in currentItem[1].get_valid_fields_lst():
                currUsedTypes +=  len(field.get_used_typenames())
            if currUsedTypes == 0:
                simpleTypes.append(currentItem)
            else:
                minUT = len(myDeque[0][1].get_used_typenames()) if myDeque else 1
                if currUsedTypes <= minUT:
                    myDeque.appendleft(currentItem)
                else:
                    myDeque.append(currentItem)
        except Exception as ex:
            raise Exception('Error during split of types - ' + ex.args[0])

    return dict(simpleTypes), dict(myDeque)

def get_valid_folder(folder):
    try:
        input_path = pathlib.Path(folder).absolute()

        if not input_path.exists():
            if input_path.parent.absolute().exists():
                os.mkdir(input_path)
    except Exception as ex:
        raise ex

    return str(input_path)

def is_deprecated(obj):
    return hasattr(obj, 'isDeprecated') and obj.isDeprecated

def pop_val_clean_dict(value, dictionary: dict[str, list], key = None):
    k_to_check = []
    try:
        if not key:
            for k, v in dictionary.items():
                if value in v:
                    v.remove(value)
                    k_to_check.append(k)
        else:
            dictionary[key].remove(value)
            k_to_check.append(key)

        map(lambda key: dictionary.pop(key) if not dictionary[key] else None, k_to_check)
    except Exception as ex:
        raise ex

def add_val_update_dict(dictionary: dict, key, value):
    try:
        if not key in dictionary.keys():
            dictionary.update({ key: value })
        else:
            if isinstance(value, list):
                dictionary[key].extend(value)
            elif isinstance(value, int):
                dictionary[key] += value
    except Exception as ex:
        raise ex