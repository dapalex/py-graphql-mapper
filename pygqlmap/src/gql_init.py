import sys
from ctypes import Union
from enum import Enum
import inspect
import types
from typing import Generic, NewType, TypeVar
from pygqlmap.enums import OperationType
from pygqlmap.gql_types import ID
from .base import FieldsShow
from .consts import ARGS_DECLARE, ARGUED_SIGNATURE_SUFFIX, GQL_BUILTIN
from .utils import get_class_name
from pygqlmap.helper import handle_recursive_ex, mapConfig
import logging as logger
from dataclasses import dataclass

## dictionary of
## key: tuple (type, startingPath)
## value: int occurrences
circularRefs: dict[str, list] = dict()
currentPath: str = None
mergedClasses: dict = {}

depthReached: str = 'Recursion depth %s reached for %s of type %s'

def _sub_class_init(obj, **kwargs):
    """For internal use only"""
    global currentPath

    try:
        if not currentPath: currentPath = obj.__class__.__name__
        for fieldName in obj.__dataclass_fields__: #if not fields else fields:
            try:
                fieldType = obj.__dataclass_fields__[fieldName].type # if not fields else fields[fieldName]

                _update_current_path(obj, fieldName, fieldType)
                _init_type(obj, fieldType, fieldName)
            except Exception as ex:
                raise handle_recursive_ex(ex, 'Exception during init of ' + fieldName + ' in ' + str(obj))

        if kwargs: _init_args(obj, kwargs)

        if FieldsShow in inspect.getmro(type(obj)):
            obj.init_fieldshow()

        #gotta clean
        _rm_initialized_from_path(obj)

    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during _sub_class_init of ' + obj.__class__.__name__)

def _init_type(obj, fieldType, fieldName):
    try:
        if fieldType == int or fieldType == float:
            setattr(obj, fieldName, -1)
        elif fieldType == list or (hasattr(fieldType, '__origin__') and fieldType.__origin__ == list):
            _init_typed_lst_as_type(obj, fieldName, fieldType)
        elif fieldType == bool:
            setattr(obj, fieldName, False)
        elif fieldType == ID:
            setattr(obj, fieldName, ID())
        elif fieldType == str:
            setattr(obj, fieldName, '')
        elif inspect.isclass(fieldType):
            if issubclass(fieldType, Enum):
                setattr(obj, fieldName, list(map(lambda c: c, fieldType))[0]) ##set first value from enum
            elif Generic in inspect.getmro(fieldType): ##recursive type
                _add_circular_ref(fieldType)
                _specialize_generic(obj, fieldName, fieldType)
            else:
                if _check_circular_refs(fieldType):
                    setattr(obj, fieldName, fieldType())
                else:
                    setattr(obj, fieldName, None)
        elif type(fieldType) == NewType or type(fieldType) == TypeVar:
            _add_circular_ref(fieldType)
            _define_var_type(obj, fieldName, fieldType)
        elif fieldType == Union:
            print('Union here')
            setattr(obj, fieldName, '')
            # pass
        else:
            logger.error('type: ' + str(fieldType) + ' for ' + fieldName + ' to manage')
            setattr(obj, fieldName, '')
    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during type initialization ' + fieldName)

def _init_typed_lst_as_type(obj, fieldName, fieldType):
    try:
        elementType = fieldType.__args__[0]

        if _check_circular_refs(elementType):
            _init_type(obj, elementType, fieldName)
        else:
            setattr(obj, fieldName, None)
    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during list initialization as type ' + fieldName)

def _specialize_generic(obj, fieldName, fieldType):
    """For internal use only"""
    global mergedClasses
    try:
        ##extract class from type name stringified of the field
        currentClass = getattr(sys.modules[obj.__module__], fieldType.__name__)

        if _check_circular_refs(currentClass):

            #welcome!!
            ## get name of the class
            className = get_class_name(fieldType)
            ## check if it is a Argued class
            if className.endswith(ARGUED_SIGNATURE_SUFFIX):
                if className in mergedClasses.keys():
                    setattr(obj, fieldName, mergedClasses[className]())
                else:
                    ##Extract the original parent recursive class
                    classParentName = className.removesuffix(ARGUED_SIGNATURE_SUFFIX)
                    ##Check if the object is of a class already managed
                    if not classParentName in str(fieldType.__bases__):
                        ## Check if the original class is present in the module
                        if hasattr(sys.modules[obj.__module__], classParentName):
                            baseClass = getattr(sys.modules[obj.__module__], classParentName)
                            mergedClass = types.new_class(className, (baseClass, dataclass(fieldType)))
                            setattr(obj, fieldName, mergedClass())
                            mergedClasses.update({ className: mergedClass })
                        else:
                            raise Exception('Original type ' + classParentName + ' from Generic field not retrieved!')
                    else:
                        setattr(obj, fieldName, fieldType())
            else: ## Generic type with no suffix 'Field'
                raise Exception(className + ' - Generic type in a no generated class!')
        else:
            setattr(obj, fieldName, None)
    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during generic specialization of ' + fieldName)

def _define_var_type(obj, fieldName, fieldType):
    """For internal use only"""
    try:
        if hasattr(sys.modules[obj.__module__], fieldType.__name__):
            currentClass = getattr(sys.modules[obj.__module__], fieldType.__name__)

            if _check_circular_refs(fieldType):
                setattr(obj, fieldName, currentClass())
            else:
                setattr(obj, fieldName, None)
        else:
            logger.error('something is wrong')
    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during variable type definition ' + fieldName)

def _mutation_init(obj, **kwargs):
    global currentPath, circularRefs, mergedClasses
    currentPath = None
    mergedClasses = {}
    circularRefs = {}
    try:
        _sub_class_init(obj, **kwargs)
        if hasattr(obj, 'args'):
            obj._args = obj.args
        from pygqlmap.enums import ArgType, OperationType
        from pygqlmap import GQLMutation
        super(GQLMutation, obj).__init__(op_type=OperationType.MUTATION, dataType=obj.type, argsType=ArgType.LITERAL_VALUES)
    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during Mutation init execution for ' + obj.__class__.__name__)

def _query_init(obj, **kwargs):
    global currentPath, circularRefs, mergedClasses
    currentPath = None
    mergedClasses = {}
    circularRefs = {}
    try:
        _sub_class_init(obj, **kwargs)
        if hasattr(obj, 'args'):
            obj._args = obj.args
        from pygqlmap.enums import ArgType, OperationType
        from pygqlmap import GQLQuery
        super(GQLQuery, obj).__init__(op_type=OperationType.QUERY, dataType=obj.type, argsType=ArgType.LITERAL_VALUES)
    except Exception as ex:
        raise handle_recursive_ex(ex, 'Error during Query init execution for ' + obj.__class__.__name__)

def _add_circular_ref(fieldType):
    global circularRefs, currentPath
    try:
        for circRefType,  circRefPath in circularRefs.keys():
            if circRefType == fieldType.__name__:
                if currentPath.__contains__(circRefPath):
                    return
        if int(mapConfig["recursionDepth"]) > 0:
            circularRefs.update({ (fieldType.__name__, currentPath): 1 if type(fieldType) == NewType else -1 })
        else:
            logger.warning(depthReached%(mapConfig["recursionDepth"], currentPath, fieldType.__name__))
        if not (fieldType.__name__, currentPath) in circularRefs.keys():
            circularRefs.update({ (fieldType.__name__, currentPath): 0 })
        else:
            pass
    except Exception as ex:
       raise handle_recursive_ex(ex, 'Error during circular refs adding for objects Init')

def _check_circular_refs(fieldType):
    """
        Recursion 0 ==> only 1 presence allowed
    """
    global circularRefs, currentPath
    try:
        for circulaRefTupKey, occurrences in circularRefs.items():
            if circulaRefTupKey[0] == fieldType.__name__:
                if currentPath.__contains__(circulaRefTupKey[1]):
                    if occurrences < int(mapConfig["recursionDepth"]):
                        circularRefs[circulaRefTupKey] += 1
                        return True
                    else:
                        return False

        return True
    except Exception as ex:
       raise handle_recursive_ex(ex, 'Error during circular refs check for objects Init')

def _update_current_path(obj, fieldName, fieldType):
    global currentPath
    if hasattr(obj, fieldName): return

    if currentPath.endswith(obj.__class__.__name__):
        if obj.__class__.__name__  == fieldType.__name__ + 'Field': pass
        currentPath += '.' + fieldType.__name__
    else:
        if currentPath.__contains__(obj.__class__.__name__):
            currentPath = currentPath[0: currentPath.rfind(obj.__class__.__name__) + len(obj.__class__.__name__)]
            currentPath += '.' + fieldType.__name__


def _rm_initialized_from_path(obj):
    global currentPath
    currentPath = currentPath[0: currentPath.rfind(obj.__class__.__name__)].removesuffix('.')

def _init_args(obj, args: dict, is_obj=False):
    try:
        if not is_obj:
            if hasattr(obj, ARGS_DECLARE):
                curr_obj = getattr(obj, ARGS_DECLARE)
            else:
                logger.warning('Arguments not allowed for ' + obj.__class__.__name__)
        else:
            curr_obj = obj
            args = dict(filter(lambda kvp: kvp[0] in curr_obj._fieldsshow.keys() and curr_obj._fieldsshow[kvp[0]], args.items()))

        for k_arg_key, k_arg_val in args.items():
            try:
                arg_val_type = type(k_arg_val)
                if arg_val_type in GQL_BUILTIN or issubclass(arg_val_type, Enum):
                    setattr(curr_obj, k_arg_key, k_arg_val)
                elif arg_val_type == list:
                    setattr(curr_obj, k_arg_key, manage_list(k_arg_val))
                else:
                    _init_args(getattr(curr_obj, k_arg_key), k_arg_val.__dict__, True)
            except Exception as ex:
                raise handle_recursive_ex(ex, 'Error in args as param init for argument ' + k_arg_key)
    except Exception as ex:
       raise handle_recursive_ex(ex, 'Error in args as param init for ' + obj.__class__.__name__)

def manage_list(list_val) -> list:
    curr_list = []
    try:
        for element in list_val:
            el_type = type(element)
            if el_type in GQL_BUILTIN or issubclass(el_type, Enum):
                curr_list.append(element)
            elif el_type == list:
                curr_list.append(manage_list(element))
            else:
                _init_args(element, element.__dict__, True)
                curr_list.append(element)

    except Exception as ex:
       raise handle_recursive_ex(ex, 'Error in args as param init for list')

    return curr_list