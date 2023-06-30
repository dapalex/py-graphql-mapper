
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Query to fetch a simple GraphQL type using Args and Variables
    and build the python class instance containing the data from the response.

    Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests

    Query to reproduce:

    query MyQuery {
        rateLimit {
            cost                -> Int
            limit               -> Int
            nodeCount           -> Int
            remaining           -> Int
            resetAt             -> String
            used                -> Int
        }
    }

    STEP 1: Instantiate the python class representing the GraphQL query
    STEP 2: Define arguments following object structure with argument type as Variables
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT: The object currency within gqlResponse.result_obj will contain the data from the GraphQL server
"""

import requests
from ..consts import GITHUB_HEADERS, GITHUB_URL
from ..output.github.queries import rateLimit
import logging as logger
from ..utils import stringifyresult

def run_simple_args_vars():
    logger.debug('\n\nRunning test_simple_args_vars...')
    try:

    ##STEP 2
        query = rateLimit()
        query.name = 'mySimpleQueryArgsVars'
    ##

    ##STEP 2
        from pygqlmap.enums import ArgType

        query._args.dryRun = False
        query._args_type = ArgType.VARIABLES
    ##

    ##RESULT
        logger.debug('Query GQL syntax: ' + query.export_gql_source)
        logger.debug('Variables: ' + query.export_gqlvariables)
    ##

##STEP 4
        response = requests.request('POST', url=GITHUB_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
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

##RESULT
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
##
    except Exception as ex:
        raise ex

    logger.debug("End of test_simple_args_vars")
