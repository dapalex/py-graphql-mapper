
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
    STEP 5: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT: The object currencies within gqlResponse.result_obj will contain the data from the GraphQL server
"""

import requests
from ..consts import GDBC_URL, GDBC_HEADERS
from ..output.gdbc.queries import currencies
import logging as logger

def run_gdbc_connobj():
    logger.info('\n\nRunning test_gdbc_connobj...')
##STEP 2

    query = currencies()
    query.name = 'myCurrenciesQuery'
##

    try:
        logger.info('Query GQL syntax: ' + query.export_gql_source)

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

##RESULT
        logger.info('Result object: ' + str(gqlResponse.result_obj))
##
    except Exception as ex:
        raise ex

    logger.info("End of test_gdbc_connobj")
