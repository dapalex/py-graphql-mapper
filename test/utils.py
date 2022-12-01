
from enum import Enum
import os
import pathlib


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
        dirToClean = pathlib.Path(os.path.join(os.curdir, 'commandsOutput'))
    if outType == OutputType.SCHEMAS:
        dirToClean = pathlib.Path(os.path.join(os.path.join(os.curdir, 'test'), 'output'))
    
    cleanFolder(dirToClean)
        
def waitForInput(isToWait: str):
    if isToWait and isToWait.lower() == 'y': input('Go on..')
    
def ManageException(message: str):
    print(message)
    input()