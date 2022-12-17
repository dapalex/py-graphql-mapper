
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


    STEP 1: Define the python class corresponding to the GraphQL connection type and 'currency' corresponding the the connection node within the query 
"""
##STEP 1
from pygqlmap.components import GQLConnection, GQLEdges, GQLObject
from utils import ManageException


class currency(GQLObject): 
    countryCodes: list
    code: str
    symbol: str
    
    def __init__(self):
        self.countryCodes = []
        self.code = ''
        self.symbol = ''
        super().__init__()

class currencies(GQLConnection): 
    
    def __init__(self):
        super().__init__(GQLEdges(currency())) 
    
##

"""
    STEP 2: Instantiate GQLOperation class representing the GraphQL query 
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The object currencies within gqlResponse.resultObject will contain the data from the GraphQL server
"""

import requests
from consts import gdbcUrl, gdbcHeaders

async def testConnectionObject(): 
    print('\n\nRunning testConnectionObject...')
##STEP 2
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation
    
    query = GQLOperation(OperationType.query, currencies, operationName='myCurrenciesQuery')
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
        gqlResponse.mapGQLDataToObj(query.obj)
##
        
##RESULT
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testConnectionObject")
