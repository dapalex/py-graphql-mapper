import os
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from .consts import gdbcHeaders, gdbcUrl
# from .utils import ManageException

def runDownloadCommandgdbcApiBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "pygqlcodegen download ./commandsOutput/Github/schema.json -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/gdbcApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGithubBySchemaFileRelPath")
    
def runDownloadCommandGeoDBCitiesBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGeoDBCitiesBySchemaFileRelPath...')
    command = "pygqlcodegen download ./commandsOutput/GeoDBCities/schema.json -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/gdbcApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGeoDBCitiesBySchemaFileRelPath")
    
def runGenerateCommandGeoDBCitiesByApiRelPath():
    print('\nRunning runGenerateCommandGeoDBCitiesByApiRelPath...')
    command = "pygqlcodegen generate C:/Users/compl/Desktop/Python/proj/py-graphql-mapper/tests/commandsOutput/GeoDBCities -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/gdbcApi/generatorArgs.json -v" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandGeoDBCitiesByApiRelPath")
    
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
