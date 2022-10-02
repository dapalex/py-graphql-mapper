import re
from types import NoneType
from typing import Set

def getClassName(object):
    try:
        if object.__doc__:
            return object.__doc__.split('(')[0]
        elif len(splitType := str(type(object)).split('\'')) > 0:
            if splitPath := splitType[1].split('.'):
                return splitPath[len(splitPath) - 1]
    except:
        print('Got an issue here')
        return str(type(object))

primitive = (int, str, bool, float, NoneType)

def isNoneOrBuiltinPrimitive(obj): ##CAREFUL LIST
    return isinstance(obj, primitive)

def filterCollection(collection: any, key: any = None, value: any = None):
    try:
        switch={
        'tuple': filterTuple,
        'dict': filterDict,
        'list': filterList,
        'set': filterSet
        }
        
        return switch[getClassName(collection)](collection, key, value)
    except:
        print("Exception during filtering")

def filterList(listToFilter, key=None, value=None):
    if not value == None:
        while listToFilter.index(value) >= 0:
            listToFilter.pop(listToFilter.index(value))

def filterDict(dictToFilter: dict, key=None, value=None):
    keysToDel = []
    for k, v in dictToFilter.items():
        if not key == None: 
            if k == key: 
                keysToDel.append(k)
                continue
        if not value == None: 
            if v == value:
                keysToDel.append(k)
                continue
    
    for keyToDel in keysToDel:
        dictToFilter.pop(keyToDel)

def filterTuple(tupleToFilter: tuple, key=None, value=None):
    if not value == None:
        lst = [tupleToFilter]
        filterList(lst, value)
        tupleToFilter = (lst)
    
def filterSet(setToFilter: set, key=None, value=None):
    if not value == None:
        while setToFilter.contains(value):
            setToFilter.discard(value)
            
def popListElementByRef(lst: list, element):
    while lst.index(element) >= 0:
        lstEl = lst[lst.index(element)]
        if id(lstEl) == id(element):
            return lst.pop(lst.index(element))
        
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
    
def graphQLize(inputSchema: str, argsToIgnore: list = []): 
    output= ''
    wentThrough = False
    if argsToIgnore:
        for args in argsToIgnore:
            if inputSchema.__contains__(args):
                inputList = inputSchema.split(args)
                output =  executeRegex(inputList[0]) + ' ' + args + ' ' + executeRegex(inputList[1])
                wentThrough = True
        
        return output if wentThrough else executeRegex(inputSchema)
    else:
        return executeRegex(inputSchema)
                
    # ret = re.sub(r': *\'[!-&(-z]*\'', ' ', inputSchema) #removes anything after : -> : '<anything>'
    # ret = re.sub(r': *[-A-Za-z0-9]*', ' ', ret)
    # ret = ret.replace('\'', ' ').replace(',', ' ')
    # ret = ret.replace('[', ' ').replace(']', ' ')
    
    # return ret

def executeRegex(input):
    ret = re.sub(r': *\'[!-&(-z]*\'', ' ', input) #removes anything after : -> : '<anything>'
    ret = re.sub(r': *[-A-Za-z0-9]*', ' ', ret)
    ret = ret.replace('\'', ' ').replace(',', ' ')
    ret = ret.replace('[', ' ').replace(']', ' ')
    return ret
    