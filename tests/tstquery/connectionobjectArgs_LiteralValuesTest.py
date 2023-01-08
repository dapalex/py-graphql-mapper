
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

from pygqlmap.network import httpRequest
from ..consts import gdbcUrl, gdbcHeaders
from ..output.GeoDBCities.queries import currencies
import logging as logger

def runConnectionObjectArgs_LiteralValues():
    logger.info('\n\nRunning testConnectionObjectArgs_LiteralValues...')
##STEP 1
    query = currencies()
    query.name='myCurrenciesQuery'
##

##STEP 2
    from pygqlmap.enums import ArgType

    query._argsType = ArgType.LiteralValues
    query._args.last = 7
    query._args.before = 'MTE='
##
    try:
##RESULT
        logger.info('Query GQL syntax: ' + query.exportGqlSource)
##

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

        logger.info('resultObject: ' + str(gqlResponse.resultObject))

    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testConnectionObjectArgs_LiteralValues")
