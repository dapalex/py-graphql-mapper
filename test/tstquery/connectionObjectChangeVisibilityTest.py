
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a GraphQL connection type 
    and build the python class instance containing the data from the response.
    In addition it shows how to hide fields of a type in a query. 
    
    PREREQUISITES:
    
    A mapped connection Query (see connectionObjectTest.py STEP 1):
    
    GraphQL version
    
    query MyQuery {
        currencies {
            totalCount                      (*)
            edges {
                cursor
                node {
                    countryCodes            (*)
                    code                    
                    symbol                  (*)
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

    Relating python classes

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
    
    OBJECTIVE: Hiding fields from the original python mapped class (above with (*))
    
    STEP 1: Instantiate GQLOperation class representing the GraphQL query 
    STEP 2: Call setShow function of GQLOperation class to set the visibility of field (path to declare with dot notation)
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: 
        a) The request toward the GraphQL server will not have the hidden fields
        b) The python class instance obtained from the response will not have the hidden fields
"""

import requests
from .consts import gdbcUrl, gdbcHeaders
from .output.GeoDBCities.queries import currencies
from .utils import ManageException

async def testConnectionObjectVisibility(): 
    print('\n\nRunning testConnectionObjectVisibility...')
##STEP 1
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation
    
    query = currencies()
    query.name = 'myCurrenciesQueryVisibility'
##
    
##STEP 2
    query.setShow('currencies.edges.node.symbol', False)
    query.setShow('currencies.edges.node.countryCodes', False)
    query.setShow('currencies.totalCount', False)
##
    
    try:
##RESULT a)
        print('Query GQL syntax: ' + query.exportGqlSource)
##
        
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
        
##RESULT b)
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testConnectionObjectVisibility")
