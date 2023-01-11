import os
from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from .consts import GDBC_HEADERS, GDBC_URL
import logging as logger

def fetchGeoDBCitiesSchema():
    logger.info('\n\nRunning fetchGeoDBCitiesSchema...')

    try:
        gqlSchema = fetch_schema_obj(GDBC_URL, GDBC_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.info('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\GeoDBCities\\', log_progress=True)
            logger.info('Python types generated')

    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of fetchGeoDBCitiesSchema")

def fetchGeoDBCitiesSchemaNoDesc():
    logger.info('\n\nRunning fetchGeoDBCitiesSchemaNoDesc...')

    try:
        gqlSchema = fetch_schema_obj(GDBC_URL, GDBC_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.info('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\GeoDBCitiesNoDesc\\', add_desc=False, log_progress=True)
            logger.info('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of fetchGeoDBCitiesSchemaNoDesc")
