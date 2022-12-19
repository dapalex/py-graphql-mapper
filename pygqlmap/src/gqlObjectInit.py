import sys
from ctypes import Union
from enum import Enum
import inspect
from typing import Generic, NewType, TypeVar
from pygqlmap.src.logger import Logger
from .base import FieldsShow
from .consts import arguedSignatureSuffix
from .utils import getClassName, getObjectClassName
from pygqlmap.helper import mapConfig

circularRef: dict[str, int] = dict()

depthReached: str = 'Recursion depth %s reached for %s.%s of type %s - It has to be managed manually'
    
def subClassInit(obj, fields = None):
    """For internal use only"""
    global circularRef
    try:
        for fieldName in obj.__dataclass_fields__ if not fields else fields:
            try:
                fieldType = obj.__dataclass_fields__[fieldName].type if not fields else fields[fieldName]
                                
                if hasattr(obj, fieldName): 
                    continue
                if fieldType.__name__ in circularRef.keys() and circularRef[fieldType.__name__] < int(mapConfig["recursionDepth"]):
                    #recursion depth limit reached
                    Logger.logWarningMessage(depthReached%(mapConfig["recursionDepth"], getObjectClassName(obj), fieldName, fieldType.__name__))
                    setattr(obj, fieldName, fieldType.__name__) 
                    continue
                
                if fieldType == int or fieldType == float:
                    setattr(obj, fieldName, 0)
                elif fieldType == list or (hasattr(fieldType, '__origin__') and fieldType.__origin__ == list):
                    setattr(obj, fieldName, [])
                elif fieldType == bool:
                    setattr(obj, fieldName, False)
                elif fieldType == str:
                    setattr(obj, fieldName, '')
                elif inspect.isclass(fieldType):
                    if issubclass(fieldType, Enum):
                        setattr(obj, fieldName, list(map(lambda c: c.value, fieldType))[0]) ##set first value from enum
                    elif Generic in inspect.getmro(fieldType): ##recursive type
                        specializeGeneric(obj, fieldName, fieldType)
                    else:
                        setattr(obj, fieldName, fieldType())
                elif type(fieldType) == NewType or type(fieldType) == TypeVar:
                    defineVariableType(obj, fieldName, fieldType)
                elif fieldType == Union:
                    print('Union here')
                    setattr(obj, fieldName, '')
                    # pass
                else:
                    Logger.logErrorMessage('type: ' + str(fieldType) + ' for ' + fieldName + ' to manage')
                    setattr(obj, fieldName, '')
                    
            except Exception as ex:
                raise Exception('Exception during init of ' + fieldName + ' in ' + str(obj) + ' - ' + ex.args[0])
        
        if FieldsShow in inspect.getmro(type(obj)):
            obj.initFieldsShow() 
    except Exception as ex:
        raise ex

def specializeGeneric(obj, fieldName, fieldType):
    """For internal use only"""
    global circularRef
    try:
        currentClass = getattr(sys.modules[obj.__module__], fieldType.__name__)
        if not fieldType.__name__ in circularRef.keys() and int(mapConfig["recursionDepth"]) > 0:
            #welcome!!
            ## get name of the class
            className = getClassName(fieldType)
            ## check if it is a Argued class
            if className.endswith(arguedSignatureSuffix):
                ##Extract the original parent recursive class
                classParentName = className.removesuffix(arguedSignatureSuffix)
                ##Check if the object is is of a class already managed
                if not classParentName in str(fieldType.__bases__):
                    ## Check if the original class is present in the module
                    if hasattr(sys.modules[obj.__module__], classParentName):
                        ##Add the original class to the bases of the object
                        fieldType.__bases__ +=  (getattr(sys.modules[obj.__module__], classParentName),)
                        ##Reinstantiate the same object updated
                        setattr(obj, fieldName, fieldType())
                    else:
                        raise Exception('Original type ' + classParentName + ' from Generic field not retrieved!')
                else:
                    Logger.logInfoMessage('Generic type ' + className + ' already managed')
                    setattr(obj, fieldName, fieldType())
            else: ## Generic type with no suffix 'Field'
                raise Exception(className + ' - Generic type in a no generated class!')
        elif fieldType.__name__ in circularRef.keys() and circularRef[fieldType.__name__] < int(mapConfig["recursionDepth"]):
                currentClass = getattr(sys.modules[obj.__module__], fieldType.__name__)
                circularRef[fieldType.__name__] += 1
                setattr(obj, fieldName, currentClass())
        else:
            Logger.logWarningMessage(depthReached%(mapConfig["recursionDepth"], getObjectClassName(obj), fieldName, fieldType.__name__))
            setattr(obj, fieldName, fieldType.__name__)
    except Exception as ex:
        raise ex

def defineVariableType(obj, fieldName, fieldType):
    """For internal use only"""
    global circularRef
    try:
        if hasattr(sys.modules[obj.__module__], fieldType.__name__):
            currentClass = getattr(sys.modules[obj.__module__], fieldType.__name__)
            
            if fieldType.__name__ in circularRef.keys(): 
                if circularRef[fieldType.__name__] < int(mapConfig["recursionDepth"]):
                    circularRef[fieldType.__name__] += 1
                    setattr(obj, fieldName, currentClass())
                else:
                    #recursion depth limit reached
                    Logger.logWarningMessage(depthReached%(mapConfig["recursionDepth"], getObjectClassName(obj), fieldName, fieldType.__name__))
                    setattr(obj, fieldName, fieldType.__name__)
            else:
                circularRef.update({ fieldType.__name__: 1 })
                setattr(obj, fieldName, currentClass())
        else:
            Logger.logErrorMessage('something is wrong')
    except Exception as ex:
        raise ex
    
def operationInit(obj):
    subClassInit(obj)
    from pygqlmap.components import GQLMutation, GQLQuery
    if GQLMutation in obj.__class__.__bases__:
        mutationInit(obj)
    elif GQLQuery in obj.__class__.__bases__:
        queryInit(obj)
    else:
        Logger.logCriticalMessage('Construction of operation inconsistent!')
    
def mutationInit(obj):
        if hasattr(obj, 'args'):
            obj._args = obj.args
        from pygqlmap.enums import ArgType, OperationType
        from pygqlmap.components import GQLMutation
        super(GQLMutation, obj).__init__(operationType=OperationType.mutation, dataType=obj.type, argsType=ArgType.LiteralValues)

def queryInit(obj):
        if hasattr(obj, 'args'):
            obj._args = obj.args
        from pygqlmap.enums import ArgType, OperationType
        from pygqlmap.components import GQLQuery
        super(GQLQuery, obj).__init__(operationType=OperationType.query, dataType=obj.type, argsType=ArgType.LiteralValues)