import os
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from .consts import gdbcHeaders, gdbcUrl
# from .utils import ManageException

def fetchGeoDBCitiesSchema(): 
    print('\n\nRunning fetchGeoDBCitiesSchema...')
    
    try:
        gqlSchema = fetchSchemaObject(gdbcUrl, gdbcHeaders, querySchemaAndTypes)
        
        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\GeoDBCities\\', logProgress=True)
            print('Python types generated')
            
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])
            
    print("End of fetchGeoDBCitiesSchema")

def fetchGeoDBCitiesSchemaNoDesc(): 
    print('\n\nRunning fetchGeoDBCitiesSchemaNoDesc...')
    
    try:
        gqlSchema = fetchSchemaObject(gdbcUrl, gdbcHeaders, querySchemaAndTypes)
        
        if gqlSchema:            
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\GeoDBCitiesNoDesc\\', addDescription=False, logProgress=True)
            print('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])
            
    print("End of fetchGeoDBCitiesSchemaNoDesc")
