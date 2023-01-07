import sys
import os
import pathlib
import unittest


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

from .geoDBCitiesApiUnitTest import (fetchGeoDBCitiesSchema, fetchGeoDBCitiesSchemaNoDesc)
from .githubApiUnitTest import (fetchGithubMutationTypes, fetchGithubMutationTypesFromSchemaNoDesc)
from .rapidApiUnitTest import (fetchRapidApiTestSchemaAndTypes, fetchRapidApiTestSchemaAndTypesNoDesc)

class TestCodegen(unittest.TestCase):
    
    def testGeoDBCitiesSchema(self):
      return fetchGeoDBCitiesSchema()
  
    def testGeoDBCitiesSchemaNoDesc(self):
      return fetchGeoDBCitiesSchemaNoDesc()
  
    def testGithubMutationTypesFromSchemaNoDesc(self):
      return fetchGithubMutationTypesFromSchemaNoDesc()
  
    def testGithubMutationTypes(self):
      return fetchGithubMutationTypes()
  
    def testRapidApiTestSchemaAndTypesNoDesc(self):
      return fetchRapidApiTestSchemaAndTypesNoDesc()
  
    def testRapidApiTestSchemaAndTypes(self):
      return fetchRapidApiTestSchemaAndTypes()
  