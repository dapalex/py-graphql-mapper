import inspect
import logging as logger
import re
import sys
from enum import Enum
from pygqlmap.gqlTypes import ID
from .consts import primitives

stdOut = sys.stdout

def getClassName(cls):
    return str(cls).split('\'')[1].split('.')[len(str(cls).split('\'')[1].split('.')) - 1]

def getObjectClassName(obj):
    try:
        if len(splitType := str(type(obj)).split('\'')) > 0:
            if splitPath := splitType[1].split('.'):
                return splitPath[len(splitPath) - 1]
    except:
        try:
            if obj.__doc__:
                return obj.__doc__.split('(')[0]
        except Exception as ex:
            logger.warning('Got an issue here')
    
    return str(type(obj))

def isEmptyField(field):
    if type(field) == str or  type(field) == ID:
        return len(field) == 0
    elif type(field) == int or type(field) == float:
        return field < 0
    elif type(field) == type: #should never get in
        return field 
    elif type(field) == bool:  
        return False
    elif type(field) == dict: 
        return not not field
    elif type(field) == list: 
        return not field
    elif Enum in inspect.getmro(type(field)): 
        return field.value == None
    elif inspect.isclass(type(field)):
        out = True
        for innerField in field.__dataclass_fields__:
            out = out and isEmptyField(getattr(field, innerField))
        return out
    else:
        logger.error('type not managed!')
      
def isNoneOrBuiltinPrimitive(obj):
    return isinstance(obj, primitives)

def popListElementByRef(lst: list, element):
    while lst.index(element) >= 0:
        lstEl = lst[lst.index(element)]
        if id(lstEl) == id(element):
            return lst.pop(lst.index(element))

def mergeTupleUniqueArguments(tup1: tuple, tup2: tuple):
    if tup2:
       
            tup1 = addTupleUniqueArgument(tup1, tup2[0], tup2[1])
    
    return tup1

def addTupleUniqueArgument(tup: tuple, strArgument, location):
    if (strArgument, location) not in tup:
        tup = tup + (strArgument, location)

    return tup

def getDotNotationInfo(dataInput: str) -> tuple:
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
    
def executeRegex(dataInput):
    ret = re.sub(r': *\'[!-&(-z]*\'', ' ', dataInput) #removes anything after : -> : '<anything>'
    ret = re.sub(r': *[-A-Za-z0-9]*', ' ', ret)
    ret = ret.replace('\'', ' ').replace(',', ' ')
    ret = ret.replace('[', ' ').replace(']', ' ')
    return ret
    