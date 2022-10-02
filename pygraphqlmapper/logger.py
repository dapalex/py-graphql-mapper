from datetime import datetime
from enum import Enum
from io import TextIOWrapper
import sys
import traceback

stdOut = sys.stdout

class LogLevel(Enum):
     Info = 0,
     Warning = 1,
     Error = 2,
     Critical = 3
     
class Logger():
    
    def logMessage(level: LogLevel, message: str):
        try:
            msg = '{timeNow} - {lvl}: {msg}'
            print(msg.format(timeNow=datetime.now(), lvl = level, msg=message))
        except:
            pass

    def logInfoMessage(message):
        try:
            msg = '{timeNow} - ' + LogLevel.Info.name + ': {msg}'
            print(msg.format(timeNow=datetime.now(), msg=message))
        except:
            pass

    def logWarningMessage(message):
        try:
            msg = '{timeNow} - ' + LogLevel.Warning.name + ': {msg}'
            print(msg.format(timeNow=datetime.now(), msg=message))
        except:
            pass

    def logErrorMessage(message):
        try:
            msg = '{timeNow} - ' + LogLevel.Error.name + ': {msg}'
            print(msg.format(timeNow=datetime.now(), msg=message))
        except:
            pass

    def logCriticalMessage(message):
        try:
            msg = '{timeNow} - ' + LogLevel.Critical.name + ': {msg}'
            print(msg.format(timeNow=datetime.now(), msg=message))
        except:
            pass


def redirectOutputToFile(file):
    wrapper = open(file, 'a')
    sys.stdout = wrapper
    return wrapper

def restoreOutput(ioWrapper: TextIOWrapper):
    ioWrapper.close()
    sys.stdout = stdOut
    
def writeToFile(file, content):
    wrapper = redirectOutputToFile(file)
    if content == 'stack':
        stack = traceback.extract_stack()
        for item in traceback.StackSummary.from_list(stack).format():
            sys.stdout.write(item)
    else:
        sys.stdout.write(content + '\n')
    restoreOutput(wrapper)