
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Query to fetch a GraphQL connection type using Args as literal values
    and build the python class instance containing the data from the response

    PREREQUISITES:

    A mapped connection Query (see _gdbc_connobjTest.py STEP 1):

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

    STEP 1: Instantiate the python class representing the GraphQL query
    STEP 2: Define arguments following the object structure with argument type as LITERAL_VALUES
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT: The request toward the GraphQL server will have the query with arguments 'first' and 'after' with values first=3 and after='MTE=' as literal values
"""

import requests
from ..consts import GDBC_URL, GDBC_HEADERS
from ..output.gdbc.queries import currencies
import logging as logger

def run_gdbc_connobj_args_literal():
    logger.info('\n\nRunning run_gdbc_connobj_args_literal...')
##STEP 1
    query = currencies()
    query.name='myCurrenciesQuery'
##

##STEP 2
    from pygqlmap.enums import ArgType

    query._args_type = ArgType.LITERAL_VALUES
    query._args.last = 7
    query._args.before = 'MTE='
##
    try:
##RESULT
        logger.info('Query GQL syntax: ' + query.export_gql_source)
##

##STEP 3
        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
##

##STEP 4
        from pygqlmap.network import GQLResponse

        gqlResponse = GQLResponse(response)
##

        gqlResponse.print_msg_out()

##STEP 5
        gqlResponse.map_gqldata_to_obj(query.type)
##

        logger.info('Result object: ' + str(gqlResponse.result_obj))

    except Exception as ex:
        raise ex

    logger.info("End of run_gdbc_connobj_args_literal")
