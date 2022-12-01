import json

from .src.builder import QueryBuilder
from .src.enums import BuildingType

class GQLResponse():
    httpResponse = None
    errors = None
    data = None
    resultObject = None
    logProgress: bool= None
    
    def __init__(self, response: str, logProgress: bool = False):  
        self.httpResponse = response 
        self.jsonResponse = json.loads(response.text)
        self.logProgress = logProgress
        
        if type(self.jsonResponse) == dict:
            if "errors" in self.jsonResponse.keys():
                self.errors = self.jsonResponse["errors"]
            if "data" in self.jsonResponse.keys():
                self.data = self.jsonResponse["data"]
                
    def mapGQLDataToObj(self, mappedPyObject,  buildType: BuildingType = BuildingType.Standard):
        """Maps the json response to a python object and saves it in resultObject field

        Args:
            mappedPyObject (_type_, optional): python object mapped from a GraphQL type 
                                               A reference can be found in the GQLOperation object created as <queryObject>.obj
            buildType (BuildingType, optional): Options not yet implemented. Defaults to BuildingType.Standard.
        """
        if hasattr(self, 'data') and self.data:
            myBuilder = QueryBuilder(buildType, self.logProgress)
            self.resultObject = myBuilder.build(self.data, mappedPyObject)
        else:
            self.resultObject = None
        
    def printMessageOutput(self):
        """_summary_

        Raises:
            Exception: HTTP status code != 200
            Exception: Presence of errors in the json response
            Exception: Missing errors and data in the json response
        """
        print('Network result: ' + 'OK' if self.httpResponse.ok else 'KO')
        print('HTTP code: ' + str(self.httpResponse.status_code))
        
        if self.httpResponse.status_code != 200:
            raise Exception('HTTP Error: ' + self.httpResponse.text)
        else:
            if hasData :=(hasattr(self, 'data') and self.data):
                print('Data returned: ')
                print(json.dumps(self.data, indent=2))   
                
            if hasErrors :=(hasattr(self, 'errors') and self.errors):
                errOutput = ''
                for error in self.errors:
                    errOutput += str(error) + '\n'
                errOutput += '\n'
                raise Exception('Response Errors: ' + errOutput)

            if not hasData and not hasErrors:
                raise Exception('Inconsistent response: ' + self.httpResponse.text)
