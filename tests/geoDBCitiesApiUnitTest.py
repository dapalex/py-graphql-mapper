import os
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from .consts import gdbcHeaders, gdbcUrl
import logging as logger

def fetchGeoDBCitiesSchema():
    logger.info('\n\nRunning fetchGeoDBCitiesSchema...')

    try:
        gqlSchema = fetchSchemaObject(gdbcUrl, gdbcHeaders, querySchemaAndTypes)

        if gqlSchema:
            logger.info('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\GeoDBCities\\', logProgress=True)
            logger.info('Python types generated')

    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of fetchGeoDBCitiesSchema")

def fetchGeoDBCitiesSchemaNoDesc():
    logger.info('\n\nRunning fetchGeoDBCitiesSchemaNoDesc...')

    try:
        gqlSchema = fetchSchemaObject(gdbcUrl, gdbcHeaders, querySchemaAndTypes)

        if gqlSchema:
            logger.info('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\GeoDBCitiesNoDesc\\', addDescription=False, logProgress=True)
            logger.info('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of fetchGeoDBCitiesSchemaNoDesc")
