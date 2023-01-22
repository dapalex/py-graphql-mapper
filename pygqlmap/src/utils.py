import inspect
import typing
import logging as logger
import re
import sys
from enum import Enum
from pygqlmap.gql_types import ID
from pygqlmap.helper import handle_recursive_ex
from .consts import PRIMITIVES

stdOut = sys.stdout

def get_class_name(cls):
    return str(cls).split('\'')[1].split('.')[len(str(cls).split('\'')[1].split('.')) - 1]

def get_obj_class_name(obj):
    try:
        if len(splitType := str(type(obj)).split('\'')) > 0:
            if splitPath := splitType[1].split('.'):
                return splitPath[len(splitPath) - 1]
    except Exception as ex:
        logger.warning('get_obj_class_name - ' + ex.args[0])
        try:
            if obj.__doc__:
                return obj.__doc__.split('(')[0]
        except Exception as sex:
            logger.warning('Got an issue here - ' + sex.args[0])

    return str(type(obj))

def is_empty_field(field):
    if isinstance(field, str) or  isinstance(field, ID):
        return len(field) == 0
    elif isinstance(field, int) or isinstance(field, float):
        return field < 0
    elif isinstance(field, type): #should never get in
        return field
    elif isinstance(field,bool):
        return False
    elif isinstance(field, dict):
        return not not field
    elif isinstance(field, list):
        return not field
    elif Enum in inspect.getmro(type(field)):
        return field.value == None
    elif inspect.isclass(type(field)):
        out = True
        for innerField in field.__dataclass_fields__:
            out = out and is_empty_field(getattr(field, innerField))
        return out
    else:
        logger.error('type not managed!')

def is_none_or_builtin_primitive(obj):
    return type(obj) in PRIMITIVES

def pop_lst_element_by_ref(lst: list, element):
    while lst.index(element) >= 0:
        lstEl = lst[lst.index(element)]
        if id(lstEl) == id(element):
            return lst.pop(lst.index(element))

def get_dot_notation_info(dataInput: str) -> tuple:
    """for internal use

    Args:
        input (str): path through dot notation to a variable
        e.g.: <classInstanceA>.<classInstanceB>.<fieldName>

    Returns:
        tuple: structured version of input in
        ([path through objects], <fieldName>)
    """
    path = dataInput.split('.')
    variable = path.pop(len(path) - 1)
    return (path, variable)

def execute_regex(dataInput):
    ret = re.sub(r': *\'[!-&(-z]*\'', ' ', dataInput) #removes anything after : -> : '<anything>'
    ret = re.sub(r': *[-A-Za-z0-9]*', ' ', ret)
    ret = ret.replace('\'', ' ').replace(',', ' ')
    ret = ret.replace('[', ' ').replace(']', ' ')
    return ret

def check_arg_type(obj_type, obj, field_name):
    is_ok = True
    warn_el_msg = 'Argument element in %s of type %s differs from alias %s'
    warn_msg = 'Argument %s of type %s differs from alias %s'
    try:
        if type(obj_type) == typing._GenericAlias:
            if obj_type.__args__:
                for arg_type in obj_type.__args__:
                    for element in obj:
                        curr_ok = arg_type == type(element)
                        if not curr_ok:
                            logger.warning(warn_el_msg%(field_name, element.__class__.__name__, arg_type.__name__))
                        is_ok &= curr_ok
            curr_ok = obj_type.__origin__ == type(obj)
            if not curr_ok:
                logger.warning(warn_msg%(field_name, obj_type.__class__.__name__, obj_type.__origin__))
            return is_ok & curr_ok
        else:
            is_ok = type(obj) == obj_type
            if not is_ok:
                logger.warning(warn_msg%(field_name, type(obj).__name__, obj_type.__name__))
            return is_ok
    except Exception as ex:
        handle_recursive_ex(ex, 'Error during check of argument type' + field_name)