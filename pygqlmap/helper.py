import inspect
import logging as logger
import os
from configparser import ConfigParser

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
            logger.error(ex.args[0])
            return CustomException(message + ' - ' + ex.args[0])
    except:
        logger.warning('HandleRecursiveEx')