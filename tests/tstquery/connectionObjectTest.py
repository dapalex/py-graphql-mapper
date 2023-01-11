
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


    STEP 1: Instantiate the python class representing the GraphQL query
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server

    RESULT: The object currencies within gqlResponse.resultObject will contain the data from the GraphQL server
"""

from pygqlmap.network import httpRequest
from ..consts import gdbcUrl, gdbcHeaders
from ..output.GeoDBCities.queries import currencies
import logging as logger

def runConnectionObject():
    logger.info('\n\nRunning testConnectionObject...')
##STEP 2

    query = currencies()
    query.name = 'myCurrenciesQuery'
##

    try:
        logger.info('Query GQL syntax: ' + query.exportGqlSource)

##STEP 3
        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
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
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testConnectionObject")
