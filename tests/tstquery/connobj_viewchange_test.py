
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Query to fetch a GraphQL connection type
    and build the python class instance containing the data from the response.
    In addition it shows how to hide fields of a type in a query.

    PREREQUISITES:

    A mapped connection Query (see _gdbc_connobjTest.py STEP 1):

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

    STEP 1: Instantiate python class representing the GraphQL query
    STEP 2: Call set_show function of the object to set the visibility of field (path to declare with dot notation)
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT:
        a) The request toward the GraphQL server will not have the hidden fields
        b) The python class instance obtained from the response will not have the hidden fields
"""

import requests
from ..consts import GDBC_URL, GDBC_HEADERS
from ..output.gdbc.queries import currencies
import logging as logger
from ..utils import stringifyresult

def run_gdbc_connobj_viewchange():
    logger.debug('\n\nRunning run_gdbc_connobj_viewchange...')
##STEP 1
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation

    query = currencies()
    query.name = 'myCurrenciesQueryVisibility'
##

##STEP 2
    query.set_show('currencies.edges.node.symbol', False)
    query.set_show('currencies.edges.node.countryCodes', False)
    query.set_show('currencies.totalCount', False)
##

    try:
##RESULT a)
        logger.debug('Query GQL syntax: ' + query.export_gql_source)
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

##RESULT b)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
##
    except Exception as ex:
        raise ex

    logger.debug("End of run_gdbc_connobj_viewchange")
