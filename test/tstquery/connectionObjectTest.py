
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a GraphQL connection type and build the python class instance containing the data from the response
    
    Query to reproduce:
    
    query MyQuery {
        currencies {
            totalCount
            edges {
                cursor
                node {
                    countryCodes            -> list of String
                    code                    -> String
                    symbol                  -> String
                }
            }
            pageInfo {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
            }
        }
    }


    STEP 1: Instantiate class representing the GraphQL query 
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The object currencies within gqlResponse.resultObject will contain the data from the GraphQL server
"""

import requests
from consts import gdbcUrl, gdbcHeaders
from output.GeoDBCities.queries import currencies
from utils import ManageException

async def testConnectionObject(): 
    print('\n\nRunning testConnectionObject...')
##STEP 2
    
    query = currencies()
    query.name = 'myCurrenciesQuery'
##
    
    try:
        print('Query GQL syntax: ' + query.exportGqlSource)
        
##STEP 3
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource }, 
                                    headers=gdbcHeaders)
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
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testConnectionObject")
