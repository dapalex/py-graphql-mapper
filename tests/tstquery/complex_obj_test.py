
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Query to fetch a GraphQL complex type (made of objects, connections, and scalar fields) combining arguments usage as literal values
    with visibility usage for chosen fields, and finally build the python class instance containing the data from the response

    Query to reproduce:

    query myCountriesQuery  {
        countries {
            edges {
                cursor
                node {
                    code
                    callingCode
                    wikiDataId
                    capital
                    name
                    currencyCodes
                    flagImageUri
                    numRegions
                    region {
                        fipsCode
                        isoCode
                        wikiDataId
                        name
                        capital
                        country {
                            code
                            callingCode         (*)
                            wikiDataId
                            capital
                            name
                            currencyCodes       (*)
                            flagImageUri
                            numRegions
                        }
                        populatedPlaces {
                            totalCount
                        }
                    }
                    regions {
                        edges {
                            cursor
                        }
                        totalCount
                        pageInfo {
                            startCursor
                            endCursor
                            hasNextPage    (*)
                            hasPreviousPage
                        }
                    }
                }
            }
            totalCount
            pageInfo {
                startCursor
                endCursor
                hasNextPage      (*)
                hasPreviousPage
            }
        }
    }


    STEP 1: Instantiate the class representing the GraphQL query
    STEP 2: Set the arguments
    STEP 3: Call set_show function of GQLOperation class to set the visibility of chosen fields (path to declare with dot notation)
    STEP 4: Query the GraphQL server
    STEP 5: Pass the response received to the GQLResponse constructor
    STEP 6: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT:
        a) The request toward the GraphQL server will not have the hidden fields
        b) The request toward the GraphQL server will have the query with arguments 'currencyCode' and 'code'
        b) The python class instance obtained from the response will not have the hidden fields
"""

import requests
from ..consts import GDBC_HEADERS, GDBC_URL
# from ..utils import ManageException
from ..output.gdbc.queries import countries
import logging as logger
from ..utils import stringifyresult

def run_gdbc_complex_obj():
    logger.debug('\n\nRunning test_gdbc_complex_obj...')
##STEP 1
    query = countries()
    query.name = 'myCountriesQuery'
##

##STEP 2
    query._args.currencyCode = 'USD'
    query.type.edges.node.region._args.code = "AK"
##

##STEP 3
    query.set_show('countries.edges.node.callingCode', False)
    query.set_show('countries.edges.node.currencyCodes', False)
    query.set_show('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.set_show('currencies.pageInfo.hasNextPage', False)
##

##RESULT a) and b)
    logger.debug('Query GQL syntax: ' + query.export_gql_source)
##

##STEP 4
    try:
        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
##

##STEP 5
        from pygqlmap.network import GQLResponse

        gqlResponse = GQLResponse(response)
##

        gqlResponse.print_msg_out()

##STEP 6
        gqlResponse.map_gqldata_to_obj(query.type)
##

##RESULT c)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
##

    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_complex_obj")
