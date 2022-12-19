
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response
    
    Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests
    
    Query to reproduce:
    
    query MyQuery {
        rateLimit {
            cost                -> Int     
            limit               -> Int                 
            nodeCount           -> Int
            remaining           -> Int
            resetAt             -> String
            used                -> Int        
        }
    }


    STEP 1: Define the python class corresponding to the GraphQL type within the query 
"""

##STEP 1
from pygqlmap.components import GQLObject
from utils import ManageException

class rateLimit(GQLObject):
   cost: int
   limit: int 
   nodeCount: int
   remaining: int
   resetAt: str
   used: int
   
   def __init__(self):
       self.cost = -1
       self.limit = -1
       self.nodeCount = -1
       self.remaining = -1
       self.resetAt = -1
       self.used = -1
       super().__init__()
##   
   
"""
    STEP 2: Instantiate GQLOperation class representing the GraphQL query 
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The object currency within gqlResponse.resultObject will contain the data from the GraphQL server
"""

import requests
from consts import githubHeaders, githubUrl

async def testSimpleObject(): 
    print('\n\nRunning testSimpleObject...')
##STEP 2
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation
    
    query = GQLOperation(OperationType.query, rateLimit, operationName='mySimpleQuery')
##
    
    try:
        print('Query GQL syntax: ' + query.exportGqlSource)
        
##STEP 3
        response = requests.request('POST', url=githubUrl, json= { "query": query.exportGqlSource }, headers=githubHeaders)
##
        
##STEP 4
        from pygqlmap.network import GQLResponse
        
        gqlResponse = GQLResponse(response)
##
        
        gqlResponse.printMessageOutput()
        
##STEP 5
        gqlResponse.mapGQLDataToObj(query.obj)
##
        
##RESULT
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testSimpleObject")
