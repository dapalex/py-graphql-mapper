
import abc
from datetime import datetime
import sys
import os
import pathlib
import logging as logger
import requests




sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))

from pygqlmap.gql_operations import GQLQuery

from tests.output.re.enums import Period
from tests.output.re_nodesc.gql_simple_types import InsightsChartDataInput
from tests.output.re.gql_types import IROOZ_InsightsChartDataOutput_Field
from tests.output.re_nodesc.gql_types import InsightsChartDataOutput
from tests.output.re_nodesc.queries import allCoops, version
from tests.utils import stringifyresult
from tests.output.github.gql_types import AddCommentInput
# from output.github.queries import rateLimit
from codegen.generator import CodeGenerator
# from datetime import datetime
from codegen.network import fetch_schema_obj
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from pygqlmap.enums import ArgType
from pygqlmap.gql_types import ID, NonNull_ID
from pygqlmap.network import GQLResponse
from consts import GDBC_HEADERS, GDBC_URL
# from output.gdbc.gql_simple_types import Currency
# from output.gdbc.queries import currencies
from consts import *
# from output.github.gql_types import AddCommentInput
# from output.gdbc.queries import country
# from output.gdbc.gql_types import DisplayOptions
# from output.rapidapi.gql_simple_types import JYWXC_name_Field

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
                    callingCode                 (*)
                    wikiDataId
                    capital
                    name
                    currencyCodes               (*)
                    flagImageUri
                    numRegions
                    region {
                        fipsCode                (*)
                        isoCode                 (*)
                        wikiDataId              (*)
                        name
                        capital                 (*)
                        country {               (*)
                            code
                            callingCode
                            wikiDataId
                            capital
                            name
                            currencyCodes
                            flagImageUri
                            numRegions
                        }
                        populatedPlaces {       (*)
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
from consts import GDBC_HEADERS, GDBC_URL
# from ..utils import ManageException
from output.gdbc.queries import countries
import logging as logger
from utils import stringifyresult

def run_allcoops_findthisinterfaceunionorwhat():
    logger.debug('\n\nRunning test_gdbc_complex_obj...')
##STEP 1
    query = allCoops()
##

    insightsChartDataInput = IROOZ_InsightsChartDataOutput_Field.InsightsChartDataOutputArgs()
    insightsChartDataInput.input = InsightsChartDataInput()
    insightsChartDataInput.input.startDate = '2022-12-12'
    insightsChartDataInput.input.endDate = '2023-12-12'
    insightsChartDataInput.input.genFarmId = "02305"
    insightsChartDataInput.input.period = Period.Year

    query.type.generationfarm.insightsChartData._args = insightsChartDataInput
##RESULT a) and b)
    print('Query GQL syntax: ' + query.export_gql_source)
##

##STEP 4
    try:
        response = requests.request('POST', url=RE_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=RE_HEADERS)
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

run_allcoops_findthisinterfaceunionorwhat()