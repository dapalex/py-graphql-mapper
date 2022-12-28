import inspect
import pathlib
import os
from configparser import ConfigParser

from pygqlmap.src.logger import Logger

#Read config.ini file
config_object = ConfigParser()
config_object.read(os.path.join(pathlib.Path('.').absolute(), "config.ini"), encoding='UTF-8')

#Get the USERINFO section
mapConfig = config_object["MAPCONFIG"]



class CustomException(Exception):
    """ Custom exception class """

def ManageException(ex, message: str = None):
    try:
        if ex and CustomException in inspect.getmro(type(ex)):
            return ex
        else:
            Logger.logErrorMessage(ex.args[0])
            return CustomException(message + ' - ' + ex.args[0])
    except:
        pass