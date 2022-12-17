import os
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from consts import *
from utils import ManageException

async def runDownloadCommandgdbcApiBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "CodeGenerator download ./commandsOutput/Github/schema.json -apiArgs ./test/GraphQLClients/gdbcApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGithubBySchemaFileRelPath")
    
async def runDownloadCommandGeoDBCitiesBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGeoDBCitiesBySchemaFileRelPath...')
    command = "CodeGenerator download ./commandsOutput/GeoDBCities/schema.json -apiArgs ./test/GraphQLClients/gdbcApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGeoDBCitiesBySchemaFileRelPath")
    
async def runGenerateCommandGeoDBCitiesByApiRelPath():
    print('\nRunning runGenerateCommandGeoDBCitiesByApiRelPath...')
    command = "CodeGenerator generate C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/commandsOutput/GeoDBCities -apiArgs ./test/GraphQLClients/gdbcApi/generatorArgs.json -v" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandGeoDBCitiesByApiRelPath")
    
async def fetchGeoDBCitiesSchema(): 
    print('\n\nRunning fetchGeoDBCitiesSchema...')
    
    try:
        gqlSchema = fetchSchemaObject(gdbcUrl, gdbcHeaders, querySchemaAndTypes)
        
        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='test\\output\\GeoDBCities\\', logProgress=True)
            print('Python types generated')
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
            
    print("End of fetchGeoDBCitiesSchema")

async def fetchGeoDBCitiesSchemaNoDesc(): 
    print('\n\nRunning fetchGeoDBCitiesSchemaNoDesc...')
    
    try:
        gqlSchema = fetchSchemaObject(gdbcUrl, gdbcHeaders, querySchemaAndTypes)
        
        if gqlSchema:            
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='test\\output\\GeoDBCitiesNoDesc\\', addDescription=False, logProgress=True)
            print('Python types generated')
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
            
    print("End of fetchGeoDBCitiesSchemaNoDesc")
