# from datetime import datetime
# from enum import Enum
# from io import TextIOWrapper
# import sys
# import traceback

# stdOut = sys.stdout

# class LogLevel(Enum):
#      Info = 0,
#      Warning = 1,
#      Error = 2,
#      Critical = 3
     
# class Logger():
#     logProgress: bool
#     ioWrapper: TextIOWrapper = stdOut
        
#     def logMessage(level: LogLevel, message: str):
#         try:
#             msg = '{timeNow} - {lvl}: {msg}'
#             print(msg.format(timeNow=datetime.now(), lvl = level, msg=message))
#         except:
#             pass

#     def logInfoMessage(message):
#         try:
#             msg = '{timeNow} - ' + LogLevel.Info.name + ': {msg}'
#             print(msg.format(timeNow=datetime.now(), msg=message))
#         except:
#             pass

#     def logWarningMessage(message):
#         try:
#             msg = '{timeNow} - ' + LogLevel.Warning.name + ': {msg}'
#             print(msg.format(timeNow=datetime.now(), msg=message))
#         except:
#             pass

#     def logErrorMessage(message):
#         try:
#             msg = '{timeNow} - ' + LogLevel.Error.name + ': {msg}'
#             print(msg.format(timeNow=datetime.now(), msg=message))
#         except:
#             pass

#     def logCriticalMessage(message):
#         try:
#             msg = '{timeNow} - ' + LogLevel.Critical.name + ': {msg}'
#             print(msg.format(timeNow=datetime.now(), msg=message))
#             traceback.print_exc()
#         except:
#             pass
