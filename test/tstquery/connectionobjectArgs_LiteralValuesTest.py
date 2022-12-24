
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a GraphQL connection type using Args as literal values
    and build the python class instance containing the data from the response
    
    PREREQUISITES:
    
    A mapped connection Query (see connectionObjectTest.py STEP 1):
    
    GraphQL version
    
    query MyQuery {
        currencies {
            totalCount
            edges {
                cursor
                node {
                    countryCodes            
                    code                    
                    symbol                  
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

    OBJECTIVE: Creating a query passing arguments and values

    STEP 1: Instantiate GQLOperation class representing the GraphQL query 
    STEP 2: Instantiate GQLArgs object structure with argument type as LiteralValues
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The request toward the GraphQL server will have the query with arguments 'first' and 'after' with values first=3 and after='MTE=' as literal values
"""

import requests
from consts import gdbcUrl, gdbcHeaders
from tstquery.connectionObjectTest import currencies
from utils import ManageException

async def testConnectionObjectArgs_LiteralValues(): 
    print('\n\nRunning testConnectionObjectArgs_LiteralValues...')
##STEP 1
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation
    
    query = GQLOperation(OperationType.query, currencies, operationName='myCurrenciesQuery')
##
    
##STEP 2
    from pygqlmap.components import GQLArgsSet
    from pygqlmap.enums import ArgType
    
    argsSet = GQLArgsSet()
    argsSet.addArg('last', 7)
    argsSet.addArg('before', 'MTE=')
    query.setArgs(argsSet, ArgType.LiteralValues)
##
    try:
##RESULT
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
        
        print('resultObject: ' + str(gqlResponse.resultObject))
        
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testConnectionObjectArgs_LiteralValues")
