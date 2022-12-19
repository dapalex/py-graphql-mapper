import pathlib
import os
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read(os.path.join(pathlib.Path('.').absolute(), "config.ini"), encoding='UTF-8')

#Get the USERINFO section
mapConfig = config_object["MAPCONFIG"]



