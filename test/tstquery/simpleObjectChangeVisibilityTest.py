
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a simple GraphQL type 
    and build the python class instance containing the data from the response.
    In addition it shows how to hide fields of a type in a query. 
    
    Query to reproduce:
    
    query MyQuery {
        rateLimit {
            cost                (*)     
            limit                          
            nodeCount           (*)
            remaining     
            resetAt          
            used                (*)        
        }
    }

    OBJECTIVE: Hiding fields from the original python mapped class (above with (*))
    
    STEP 1: Instantiate GQLOperation class representing the GraphQL query 
    STEP 2: Call setShow function of GQLOperation class to set the visibility of fields (path to declare with dot notation)
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: 
        a) The request toward the GraphQL server will not have the hidden fields
        b) The python class instance obtained from the response will not have the hidden fields
"""

import requests
from .consts import githubHeaders, githubUrl
from output.github.queries import rateLimit
from utils import ManageException

async def testSimpleObjectVisibility(): 
    print('\n\nRunning testSimpleObjectVisibility...')
##STEP 2    
    query = rateLimit()
    query.name = 'mySimpleQueryVisibility'
##
    
##STEP 3
    query.setShow('rateLimit.cost', False)
    query.setShow('rateLimit.nodeCount', False)
    query.setShow('rateLimit.used', False)
##
    
    try:
##RESULT a)
        print('Query GQL syntax: ' + query.exportGqlSource)
##
        
##STEP 4
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": query.exportGqlSource }, 
                                    headers=githubHeaders)
##
        
##STEP 5
        from pygqlmap.network import GQLResponse
        
        gqlResponse = GQLResponse(response)
##
        
        gqlResponse.printMessageOutput()
        
##STEP 6
        gqlResponse.mapGQLDataToObj(query.type)
##
        
##RESULT b)
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testSimpleObjectVisibility")
