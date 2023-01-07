import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import unittest
from .geoDBCitiesApiUnitTest import (runDownloadCommandgdbcApiBySchemaFileRelPath, 
                                     runGenerateCommandGeoDBCitiesByApiRelPath, runGenerateCommandGeoDBCitiesBySchemaFileRelPath)
from .githubApiUnitTest import (runDownloadCommandGithubBySchemaFileRelPath, runGenerateCommandGithubByApiAbsPath)
from .helpUnitTest import runGeneratorCommandHelp
from .rapidApiUnitTest import (runDownloadCommandRapidApiBySchemaFileRelPath, runGenerateCommandRapidApiByApiAbsPath)


class TestCLI(unittest.TestCase):
    
    def testGeneratorCommandHelp(self):
      return runGeneratorCommandHelp()
  
    def testDownloadCommandgdbcApiBySchemaFileRelPath(self):
      return runDownloadCommandgdbcApiBySchemaFileRelPath()
  
    def testGenerateCommandGeoDBCitiesBySchemaFileRelPath(self):
      return runGenerateCommandGeoDBCitiesBySchemaFileRelPath()
  
    def testGenerateCommandGeoDBCitiesByApiRelPath(self):
      return runGenerateCommandGeoDBCitiesByApiRelPath()
  
    # def testDownloadCommandGithubBySchemaFileRelPath(self):
    #   return runDownloadCommandGithubBySchemaFileRelPath()
  
    # def testGenerateCommandGithubByApiAbsPath(self):
    #   return runGenerateCommandGithubByApiAbsPath()
  
    def testDownloadCommandRapidApiBySchemaFileRelPath(self):
      return runDownloadCommandRapidApiBySchemaFileRelPath()
  
    def testGenerateCommandRapidApiByApiAbsPath(self):
      return runGenerateCommandRapidApiByApiAbsPath()
  