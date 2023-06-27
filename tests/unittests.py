from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse
import requests
from pygqlmap.gql_types import ID
from pygqlmap.helper import mapConfig
from .consts import GDBC_HEADERS, GDBC_URL
from .output.gdbc.queries import country, currencies, countries, timeZones
import logging as logger

def run_gdbc_nested_object():
    logger.debug('\n\nRunning run_gdbc_nested_object...')
    try:
        query = currencies()
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gdbc_nested_object")

def run_gdbc_nested_obj_viewchange():
    logger.debug('\n\nRunning test_gdbc_nested_obj_viewchange...')
    query = currencies()
    query.name = 'MyCurrenciesQuery'

    # query.set_show('currencies.edges.cursor', False)
    query.set_show('currencies.edges.node.symbol', False)
    query.set_show('currencies.edges.node.countryCodes', False)
    query.set_show('currencies.edges.node', False)
    query.set_show('currencies.totalCount', False)
    # query.set_show('currencies.edges', False)
    query.set_show('currencies', False)

    logger.debug('currencies.edges.node.symbol -> Hide')
    logger.debug('currencies.edges.node.countryCodes -> Hide')
    # logger.debug('currencies.edges.node -> Hide')
    logger.debug('currencies.totalCount -> Hide')
    logger.debug('currencies -> Hide')
    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_nested_obj_viewchange")

def run_gdbc_complex_obj_viewchange_vars():
    logger.debug('\n\nRunning run_gdbc_complex_obj_viewchange_vars...')
    query = countries()
    query.type.edges.node.region._args.code = ID("CH")
    query._args_type = ArgType.VARIABLES

    query.set_show('countries.edges.cursor', False)
    query.set_show('countries.edges.node.region.country.capital', False)
    query.set_show('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.set_show('countries.edges.node.regions.pageInfo', False)
    query.set_show('countries.edges.node.callingCode', False)
    query.set_show('countries.edges.node.capital', False)
    query.set_show('countries.totalCount', False)

    logger.debug('countries.edges.cursor -> Hide')
    logger.debug('countries.edges.node.region.country.capital -> Hide')
    logger.debug('countries.edges.node.regions.pageInfo.hasNextPage -> Hide')
    logger.debug('countries.edges.node.regions.pageInfo -> Hide')
    logger.debug('countries.edges.node.callingCode -> Hide')
    logger.debug('countries.edges.node.capital -> Hide')
    logger.debug('countries.totalCount -> Hide')

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gdbc_complex_obj_viewchange_vars")

def run_gdbc_nested_obj_args_vars():
    logger.debug('\n\nRunning test_gdbc_nested_obj_args_vars...')
    query = currencies()
    query.name = 'myCurrenciesQuery'
    query._args.first = 3
    query._args.after = 'MTE='
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_nested_obj_args_vars")

def run_gdbc_nested_obj_args_literal():
    logger.debug('\n\nRunning test_gdbc_nested_obj_args_literal...')
    query = currencies()
    query._args.countryId = 'CH'

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_nested_obj_args_literal")

def run_gdbc_complex_obj_args_literal():
    logger.debug('\n\nRunning test_gdbc_complex_obj_args_literal...')
    from .output.gdbc.enums import IncludeDeletedFilterType
    query = countries()
    query._args.currencyCode = 'CNY'
    query.type.edges.node.region._args.code = "CH"
    if int(mapConfig["recursionDepth"]) > 0:
        query.type.edges.node.region.populatedPlaces._args.includeDeleted = IncludeDeletedFilterType.SINCE_LAST_WEEK
        query.type.edges.node.region.populatedPlaces._args.namePrefix = "gua"
    query.type.edges.node.regions._args.namePrefix = 'gua'
    query.type.edges.node.regions.edges.node.country


    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_complex_obj_args_literal")

def run_gdbc_complex_obj_args_literal_2():
    logger.debug('\n\nRunning test_gdbc_complex_obj_args_literal_2...')
    query = countries()
    query.type.edges.node.region._args.code = "CN"

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_complex_obj_args_literal_2")

def run_gdbc_complex_obj_args_vars():
    logger.debug('\n\nRunning test_gdbc_complex_obj_args_vars...')
    query = countries()
    query._args.first = 3
    query._args.after = 'Mg=='
    query.name = 'myCountriesQuery'

    query.set_show('countries.edges.node.region', False)
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_complex_obj_args_vars")

def run_gdbc_nested_obj_viewchange_args_vars():
    logger.debug('\n\nRunning test_gdbc_nested_obj_viewchange_args_vars...')
    query = currencies()
    query._args.countryId = ID('CH')
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_nested_obj_viewchange_args_vars")

def run_gdbc_complex_obj_viewchange_args_vars():
    logger.debug('\n\nRunning test_gdbc_complex_obj_viewchange_args_vars...')
    query = countries()
    query._args.first = 3
    query._args.after = 'MTE='
    query.set_show('countries.edges.cursor', False)
    query.set_show('countries.edges.node.region', False)
    query.set_show('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.set_show('countries.edges.node.regions.pageInfo', False)
    query.set_show('countries.edges.node.callingCode', False)
    query.set_show('countries.edges.node.capital', False)
    query.set_show('countries.totalCount', False)
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of test_gdbc_complex_obj_viewchange_args_vars")

def run_gdbc_obj_composed_args():
    logger.debug('\n\nRunning run_gdbc_obj_composed_args...')
    try:
        from .output.gdbc.enums import Language
        from .output.gdbc.gql_types import DisplayOptions

        query = country()
        query.log_progress=True
        disp_opt = DisplayOptions()
        disp_opt.asciiMode = True
        disp_opt.language = Language.EN
        query = country(id = ID('CH'), displayOptions = disp_opt)
        query.type.region._args.code = 'Q12094'

        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response, True)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gdbc_obj_composed_args")

def run_gdbc_nested_obj_with_list():
    logger.debug('\n\nRunning run_gdbc_obj_composed_args...')
    try:
        query = timeZones(first=10 )
        query.log_progress=True

        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response, True)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gdbc_obj_composed_args")
