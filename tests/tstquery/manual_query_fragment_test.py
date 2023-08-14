"""
    USE CASE DESCRIPTION:
    This test shows how to simulate a fragment behavior creating a manual python object as fragment and integrate it in multiple queries from the generated code.

    Fragment to reproduce:

    currency {
        code
        symbol
    }

    Queries to reproduce:

    query1  fraggedAllCoops {
        allCoops {
            id
            currency {                    #python CurrencyFragment "fragment"
                code
                symbol
            }
            name
            code
            generationfarm {
                id
                currency {                #python CurrencyFragment "fragment"
                    code
                    symbol
                }
                name
            }
        }
    }

    query2 fraggedCurrencies {
        currency {                #python CurrencyFragment "fragment"
            code
            symbol
        }
    }
    STEP 1: Define the python class corresponding to the GraphQL fragment you intend to reuse
"""
##STEP 1
from pygqlmap.components import GQLObject
import logging as logger
import requests

from ..utils import stringifyresult

class CurrencyFragment(GQLObject):
   code: str
   symbol: str

##

"""
    STEP 2: Instantiate the first generated query integrating the fragment
    STEP 3: Execute the first query and parse response
    STEP 4: Instantiate the second generated query integrating the fragment
    STEP 5: Execute the first query and parse response

    RESULT: The python class has been used as fragment
"""
from ..consts import GITHUB_URL, GITHUB_HEADERS, RE_HEADERS, RE_URL

from pygqlmap.network import GQLResponse
from tests.output.re_nodesc.queries import allCoops, currencies

def run_manual_query_fragment():
    logger.debug('\n\nRunning run_manual_query_fragment...')
    try:
##STEP 2
        query1 = allCoops()
        query1.name = 'fraggedAllCoops'
        query1.type.currency = CurrencyFragment()
        query1.type.generationfarm.currency = CurrencyFragment()

        #remove not shown fields for the example
        query1.set_show("allCoops.*", False)
        query1.set_show("allCoops.id", True)
        query1.set_show("allCoops.currency", True)
        query1.set_show("allCoops.name", True)
        query1.set_show("allCoops.code", True)
        query1.set_show("allCoops.generationfarm.*", False)
        query1.set_show("allCoops.generationfarm.id", True)
        query1.set_show("allCoops.generationfarm.currency", True)
        query1.set_show("allCoops.generationfarm.name", True)


##

##STEP 3
        response = requests.request('POST', url=RE_URL,
                                        json={ "query": query1.export_gql_source },
                                    headers=RE_HEADERS)

        gqlResponse1 = GQLResponse(response)
##

##STEP 4
        query2 = currencies()
        query2.name = 'fraggedCurrencies'
        query2.type = CurrencyFragment()
##

##STEP 5
        response2 = requests.request('POST', url=RE_URL,
                                        json={ "query": query2.export_gql_source },
                                    headers=RE_HEADERS)

        gqlResponse2 = GQLResponse(response)
##

##RESULT
        logger.debug('Query GQL syntax: ' + query1.export_gql_source)
        gqlResponse1.print_msg_out()
        gqlResponse1.map_gqldata_to_obj(query1.type)
        logger.info('result object 1: ' + stringifyresult(gqlResponse1.result_obj))
        logger.debug('Query GQL syntax: ' + query2.export_gql_source)
        gqlResponse2.print_msg_out()
        gqlResponse2.map_gqldata_to_obj(query2.type)
        logger.info('result object 2: ' + stringifyresult(gqlResponse2.result_obj))
##
    except Exception as ex:
        raise ex

logger.debug("End of run_manual_query_fragment")
