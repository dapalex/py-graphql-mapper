import inspect
import pathlib
import os
from configparser import ConfigParser

from pygqlmap.src.logger import Logger

#Read config.ini file
config_object = ConfigParser()
config_object.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.ini"), encoding='UTF-8')

if not config_object: raise Exception('Config file not')
#Get the USERINFO section
mapConfig = config_object["MAPCONFIG"]



class CustomException(Exception):
    """ Custom exception class """

def HandleRecursiveEx(ex, message: str = None):
    try:
        if ex and CustomException in inspect.getmro(type(ex)):
            return ex
        else:
            Logger.logErrorMessage(ex.args[0])
            return CustomException(message + ' - ' + ex.args[0])
    except:
        pass