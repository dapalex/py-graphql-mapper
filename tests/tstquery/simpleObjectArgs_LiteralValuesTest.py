
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Query to fetch a simple GraphQL type using Args as Literal Values
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

    STEP 1: Instantiate class representing the GraphQL query
    STEP 2: Set arguments following the object structure with argument type as LiteralValues
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server

    RESULT: The object currency within gqlResponse.resultObject will contain the data from the GraphQL server
"""

from pygqlmap.network import httpRequest
from ..consts import githubHeaders, githubUrl
from ..output.github.queries import rateLimit
import logging as logger

def runSimpleObjectArgs_LiteralValues():
    logger.info('\n\nRunning testSimpleObjectArgs_LiteralValues...')
##STEP 2
    query = rateLimit()
    query.name = 'mySimpleQueryArgs'
##

##STEP 3
    query._args.dryRun = True
##
    try:
        logger.info('Query GQL syntax: ' + query.exportGqlSource)

##STEP 4
        response = httpRequest(githubUrl,  { "query": query.exportGqlSource }, githubHeaders)
##

##STEP 5
        from pygqlmap.network import GQLResponse

        gqlResponse = GQLResponse(response)
##

        gqlResponse.printMessageOutput()

##STEP 6
        gqlResponse.mapGQLDataToObj(query.type)
##

##RESULT
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testSimpleObjectArgs_LiteralValues")
