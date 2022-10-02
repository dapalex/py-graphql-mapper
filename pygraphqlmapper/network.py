

import json
from builder import Builder
from enums import BuildingType
from gqlTypes import GQLObject


class GQLResponse():
    errors: dict
    data: dict
    resultObject: GQLObject
    logProgress: bool
    
    def __init__(self, response: str, logProgress: bool = False):    
        self.textResponse = response.text
        self.jsonResponse = json.loads(response.text)
        self.logProgress = logProgress
        
        if type(self.jsonResponse) == dict:
            if "errors" in self.jsonResponse.keys():
                self.errors = self.jsonResponse["errors"]
            if "data" in self.jsonResponse.keys():
                self.data = self.jsonResponse["data"]
                
    def mapGQLDataToObj(self, queryObject, buildType: BuildingType = BuildingType.Standard):
        if self.data:
            myBuilder = Builder(buildType, self.logProgress)
            self.resultObject = myBuilder.buildPyObject(self.data, queryObject)
        else:
            self.resultObject = None
    
    def printMessageOutput(self):
        if hasattr(self, 'data'):
            print('Data returned: ' + str(self.data))  
        elif hasattr(self, 'errors'):
            print('Response Errors: ' + str(self.errors))
        else:
            print('Issues with server: ' + self.textResponse)

                
