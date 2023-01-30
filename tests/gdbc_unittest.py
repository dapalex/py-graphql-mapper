from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from .consts import GDBC_HEADERS, GDBC_URL
import logging as logger

def run_fetch_gdbc_schema():
    logger.debug('\n\nRunning run_fetch_gdbc_schema...')

    try:
        gqlSchema = fetch_schema_obj(GDBC_URL, GDBC_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.debug('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\gdbc\\', log_progress=True)
            logger.debug('Python types generated')

    except Exception as ex:
        raise ex

    logger.debug("End of run_fetch_gdbc_schema")

def run_fetch_gdbc_schema_no_desc():
    logger.debug('\n\nRunning run_fetch_gdbc_schema_no_desc...')

    try:
        gqlSchema = fetch_schema_obj(GDBC_URL, GDBC_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.debug('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\gdbc_nodesc\\', add_desc=False, log_progress=True)
            logger.debug('Python types generated')
    except Exception as ex:
        raise ex

    logger.debug("End of run_fetch_gdbc_schema_no_desc")
