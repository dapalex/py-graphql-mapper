
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

    STEP 1: Instantiate the python class representing the GraphQL query
    STEP 2: Call set_show function of the python class to set the visibility of fields (path to declare with dot notation)
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT:
        a) The request toward the GraphQL server will not have the hidden fields
        b) The python class instance obtained from the response will not have the hidden fields
"""

import requests
from ..consts import GITHUB_HEADERS, GITHUB_URL
from ..output.github.queries import rateLimit
import logging as logger

def run_simple_obj_viewchange():
    logger.debug('\n\nRunning run_simple_obj_viewchange...')
##STEP 2
    query = rateLimit()
    query.name = 'mySimpleQueryVisibility'
##

##STEP 3
    query.set_show('rateLimit.cost', False)
    query.set_show('rateLimit.nodeCount', False)
    query.set_show('rateLimit.used', False)
##

    try:
##RESULT a)
        logger.debug('Query GQL syntax: ' + query.export_gql_source)
##

##STEP 4
        response = requests.request('POST', url=GITHUB_URL,
                                    json={ "query": query.export_gql_source },
                                    headers=GITHUB_HEADERS)
##

##STEP 5
        from pygqlmap.network import GQLResponse

        gqlResponse = GQLResponse(response)
##

        gqlResponse.print_msg_out()

##STEP 6
        gqlResponse.map_gqldata_to_obj(query.type)
##

##RESULT b)
        logger.info('result object: ' + str(gqlResponse.result_obj))
##
    except Exception as ex:
        raise ex

    logger.debug("End of run_simple_obj_viewchange")
