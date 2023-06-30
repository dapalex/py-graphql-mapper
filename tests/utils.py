from enum import Enum
from io import TextIOWrapper
import logging as logger
import os
import pathlib
import sys


class OutputType(Enum):
    COMMANDS = 1,
    SCHEMAS = 2,
    OTHER = 3

def cleanFolder(folder):
    for top, dirs, files in os.walk(folder):
        for file in files:
            os.remove(os.path.join(top,file))
        for dir in dirs:
            directory = os.path.join(folder, dir)
            cleanFolder(directory)
            os.rmdir(directory)

def cleanOutput(outType: OutputType):
    if outType == OutputType.COMMANDS:
        dirToClean = pathlib.Path(os.path.join(os.curdir, 'cmd_output'))
    if outType == OutputType.SCHEMAS:
        dirToClean = pathlib.Path(os.path.join(os.path.join(os.curdir, 'test'), 'output'))

    cleanFolder(dirToClean)

# def waitForInput(isToWait: str):
#     if isToWait and isToWait.lower() == 'y': input('Go on..')

# def ManageException(message: str):
#     logger.critical(message)


def redirectOutputToFile(fileName, append: bool = True):
    try:
        wrapper = open(fileName, 'a' if append else 'w')
        sys.stdout = wrapper
        return wrapper
    except Exception as ex:
        logger.error('Error during output redirect - ' + ex.args[0])

def restoreOutput(ioWrapper: TextIOWrapper):
    try:
        ioWrapper.close()
        sys.stdout = sys.stdout
    except Exception as ex:
        logger.error('Error during output restore - ' + ex.args[0])

def stringifyresult(py_result):
    result: str
    import inspect

    if  list in inspect.getmro(type(py_result)):
        result = str(py_result.__class__) + ' ['
        for el in py_result:
            result += ' ' + str(el)

        result + ' ]'
        return result
    else:
        return str(py_result)