
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

    STEP 1: Instantiate class representing the GraphQL query 
    STEP 2: Query the GraphQL server
    STEP 3: Pass the response received to the GQLResponse constructor
    STEP 4: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The object currency within gqlResponse.resultObject will contain the data from the GraphQL server
"""

from pygqlmap.network import httpRequest
from ..consts import githubHeaders, githubUrl
from ..output.github.queries import rateLimit
# from ..utils import ManageException

def testSimpleObject(): 
    print('\n\nRunning testSimpleObject...')
##STEP 2
    query = rateLimit()
    query.name = 'mySimpleQuery'
##
    
    try:
        print('Query GQL syntax: ' + query.exportGqlSource)
        
##STEP 3
        response = httpRequest(url=githubUrl, json= { "query": query.exportGqlSource }, headers=githubHeaders)
##
        
##STEP 4
        from pygqlmap.network import GQLResponse
        
        gqlResponse = GQLResponse(response)
##
        
        gqlResponse.printMessageOutput()
        
##STEP 5
        gqlResponse.mapGQLDataToObj(query.type)
##
        
##RESULT
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testSimpleObject")
