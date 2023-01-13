from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse
import requests
from pygqlmap.gql_types import ID
from pygqlmap.helper import mapConfig
from .consts import GDBC_HEADERS, GDBC_URL
from .output.gdbc.queries import country, currencies, countries
import logging as logger

def runNestedObject():
    logger.info('\n\nRunning testNestedObject...')
    try:
        query = currencies()
        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testNestedObject")

def run_gdbc_nested_obj_viewchange():
    logger.info('\n\nRunning test_gdbc_nested_obj_viewchange...')
    query = currencies()
    query.name = 'MyCurrenciesQuery'

    # query.set_show('currencies.edges.cursor', False)
    query.set_show('currencies.edges.node.symbol', False)
    query.set_show('currencies.edges.node.countryCodes', False)
    query.set_show('currencies.edges.node', False)
    query.set_show('currencies.totalCount', False)
    # query.set_show('currencies.edges', False)
    query.set_show('currencies', False)

    logger.info('currencies.edges.node.symbol -> Hide')
    logger.info('currencies.edges.node.countryCodes -> Hide')
    # logger.info('currencies.edges.node -> Hide')
    logger.info('currencies.totalCount -> Hide')
    logger.info('currencies -> Hide')
    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_nested_obj_viewchange")

def run_gdbc_complex_obj_viewchange():
    logger.info('\n\nRunning test_gdbc_complex_obj_viewchange...')
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

    logger.info('countries.edges.cursor -> Hide')
    logger.info('countries.edges.node.region.country.capital -> Hide')
    logger.info('countries.edges.node.regions.pageInfo.hasNextPage -> Hide')
    logger.info('countries.edges.node.regions.pageInfo -> Hide')
    logger.info('countries.edges.node.callingCode -> Hide')
    logger.info('countries.edges.node.capital -> Hide')
    logger.info('countries.totalCount -> Hide')

    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_complex_obj_viewchange")

def run_gdbc_nested_obj_args_vars():
    logger.info('\n\nRunning test_gdbc_nested_obj_args_vars...')
    query = currencies()
    query.name = 'myCurrenciesQuery'
    query._args.first = 3
    query._args.after = 'MTE='
    query._args_type = ArgType.VARIABLES

    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)
        logger.info('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_nested_obj_args_vars")

def run_gdbc_nested_obj_args_literal():
    logger.info('\n\nRunning test_gdbc_nested_obj_args_literal...')
    query = currencies()
    query._args.countryId = 'CH'

    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_nested_obj_args_literal")

def run_gdbc_complex_obj_args_literal():
    logger.info('\n\nRunning test_gdbc_complex_obj_args_literal...')
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
        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_complex_obj_args_literal")

def run_gdbc_complex_obj_args_literal_2():
    logger.info('\n\nRunning test_gdbc_complex_obj_args_literal_2...')
    query = countries()
    query.type.edges.node.region._args.code = "CN"

    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_complex_obj_args_literal_2")

def run_gdbc_complex_obj_args_vars():
    logger.info('\n\nRunning test_gdbc_complex_obj_args_vars...')
    query = countries()
    query._args.first = 3
    query._args.after = 'Mg=='
    query.name = 'myCountriesQuery'

    query.set_show('countries.edges.node.region', False)
    query._args_type = ArgType.VARIABLES

    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)
        logger.info('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_complex_obj_args_vars")

def run_gdbc_nested_obj_viewchange_args_vars():
    logger.info('\n\nRunning test_gdbc_nested_obj_viewchange_args_vars...')
    query = currencies()
    query._args.countryId = ID('CH')
    query._args_type = ArgType.VARIABLES

    try:
        logger.info('gqlSource GQL version: ' + query.export_gql_source)
        logger.info('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_nested_obj_viewchange_args_vars")

def run_gdbc_complex_obj_viewchange_args_vars():
    logger.info('\n\nRunning test_gdbc_complex_obj_viewchange_args_vars...')
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
        logger.info('gqlSource GQL version: ' + query.export_gql_source)
        logger.info('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_complex_obj_viewchange_args_vars")

def run_gdbc_obj_composed_args():
    logger.info('\n\nRunning test_gdbc_obj_composed_args...')
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

        logger.info('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response, True)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_gdbc_obj_composed_args")
