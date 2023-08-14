import requests
from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse
from tests.output.re_nodesc.enums import Period
from tests.output.re_nodesc.gql_simple_types import InsightsChartDataInput
from tests.output.re_nodesc.gql_types import JFUJX_InsightsChartDataOutput_Field
from tests.output.re_nodesc.queries import allCoops, branding, version
from tests.utils import stringifyresult
from .consts import RE_HEADERS, RE_URL
import logging as logger

def run_fetch_re_schema():
    logger.debug('\n\nRunning run_fetch_re_schema...')

    try:
        gqlSchema = fetch_schema_obj(RE_URL, RE_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.debug('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\re\\', log_progress=True)
            logger.debug('Python types generated')

    except Exception as ex:
        raise ex

    logger.debug("End of run_fetch_re_schema")

def run_fetch_re_schema_no_desc():
    logger.debug('\n\nRunning run_fetch_re_schema_no_desc...')

    try:
        gqlSchema = fetch_schema_obj(RE_URL, RE_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.debug('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\re_nodesc\\', add_desc=False, log_progress=True)
            logger.debug('Python types generated')
    except Exception as ex:
        raise ex

    logger.debug("End of run_fetch_gdbc_schema_no_desc")

def run_re_version_literal():
    logger.debug('\n\nRunning run_re_version_literal...')
    query = version()
    query.name = 'myVersionQuery'

    query._args_type = ArgType.LITERAL_VALUES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=RE_URL,
                                    json={ "query": query.export_gql_source },
                                    headers=RE_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_re_version_literal")

def run_re_version_vars():
    logger.debug('\n\nRunning run_re_version_vars...')
    query = version()
    # query._args.first = 3
    # query._args.after = 'Mg=='
    query.name = 'myVersionQuery'

    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=RE_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=RE_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_re_version_vars")

def run_re_allcoops():
    logger.debug('\n\nRunning test_gdbc_complex_obj...')
##STEP 1
    query = allCoops()
##

    insightsChartDataInput = JFUJX_InsightsChartDataOutput_Field.InsightsChartDataOutputArgs()
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
