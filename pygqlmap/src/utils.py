import inspect
import re
import sys
from io import TextIOWrapper
from enum import Enum
from pygqlmap.gqlTypes import ID
from .logger import Logger
from .consts import primitives

stdOut = sys.stdout

def getClassName(cls):
    return str(cls).split('\'')[1].split('.')[len(str(cls).split('\'')[1].split('.')) - 1]

def getObjectClassName(object):
    try:
        if len(splitType := str(type(object)).split('\'')) > 0:
            if splitPath := splitType[1].split('.'):
                return splitPath[len(splitPath) - 1]
    except:
        try:
            if object.__doc__:
                return object.__doc__.split('(')[0]
        except:
            print('Got an issue here')
    
    return str(type(object))

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
        return not field
    elif inspect.isclass(type(field)):
        out = True
        for innerField in field.__dataclass_fields__:
            out = out and isEmptyField(getattr(field, innerField))
        return out
    else:
        Logger.logErrorMessage('type not managed!')
      
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

# def splitByArg(string: str, arg: str):
#     if not arg: return [string]
    
#     argFirstIndex = string.find(arg)
#     argLastIndex = string.rfind(arg)
    
#     strings = [string[0,argFirstIndex], string[argLastIndex,]]
#     return strings

def getDotNotationInfo(input: str) -> tuple:
    """for internal use

    Args:
        input (str): path through dot notation to a variable 
        e.g.: <classInstanceA>.<classInstanceB>.<fieldName>  

    Returns:
        tuple: structured version of input in
        ([path through objects], <fieldName>)
    """
    path = input.split('.')
    variable = path.pop(len(path) - 1) 
    return (path, variable)
    
def executeRegex(input):
    ret = re.sub(r': *\'[!-&(-z]*\'', ' ', input) #removes anything after : -> : '<anything>'
    ret = re.sub(r': *[-A-Za-z0-9]*', ' ', ret)
    ret = ret.replace('\'', ' ').replace(',', ' ')
    ret = ret.replace('[', ' ').replace(']', ' ')
    return ret
    
def redirectOutputToFile(fileName, append: bool = True):
    try:
        wrapper = open(fileName, 'a' if append else 'w')
        sys.stdout = wrapper
        return wrapper
    except Exception as ex:
        Logger.logErrorMessage('Error during output redirect - ' + ex.args[0])

def restoreOutput(ioWrapper: TextIOWrapper):
    try:
        ioWrapper.close()
        sys.stdout = stdOut
    except Exception as ex:
        Logger.logErrorMessage('Error during output restore - ' + ex.args[0])
