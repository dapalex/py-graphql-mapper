import requests
from GraphQLClients.GdbcApi.Model.countries import countries
from enum import Enum
from GraphQLClients.GdbcApi.Model.country import Country
from GraphQLClients.GdbcApi.Model.currencies import currencies
from GraphQLClients.GdbcApi.Model.currency import currency
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.components import GQLOperation, GQLArgsSet
from pygqlmap.network import GQLResponse
from pygqlmap.gqlTypes import ID
from consts import gdbcHeaders, gdbcUrl
from utils import ManageException

async def testNestedObject(): 
    print('\n\nRunning testNestedObject...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(currencies())
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObject")

async def testSimpleObjectShowChange(): 
    print('\n\nRunning testSimpleObjectShowChange...')
    query = GQLOperation(OperationType.query, currency, 'myCurrencyQuery')
    
    query.setShow('currency.symbol', False)
    query.setShow('currency', False)
    print('currency.symbol -> Hide')
    print('currency -> Hide')
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        print('executeQuery FAILED - expected - ' + ex.args[0])
        
    print("End of testSimpleObjectShowChange")

async def testNestedObjectShowChange(): 
    print('\n\nRunning testNestedObjectShowChange...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')  
    
    # query.setShow('currencies.edges.cursor', False)
    query.setShow('currencies.edges.node.symbol', False)
    query.setShow('currencies.edges.node.countryCodes', False)
    query.setShow('currencies.edges.node', False)
    query.setShow('currencies.totalCount', False)
    # query.setShow('currencies.edges', False)
    query.setShow('currencies', False)
    
    print('currencies.edges.node.symbol -> Hide')
    print('currencies.edges.node.countryCodes -> Hide')
    # print('currencies.edges.node -> Hide')
    print('currencies.totalCount -> Hide')
    print('currencies -> Hide')
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectShowChange")

async def testComplexObjectShowChange(): 
    print('\n\nRunning testComplexObjectShowChange...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery') 
    
    neededArg = GQLArgsSet("countries.edges.node.region")
    neededArg.addArg("code", ID("CH"))
    query.setArgs(neededArg, ArgType.Variables)
    
    query.setShow('countries.edges.cursor', False)
    query.setShow('countries.edges.node.region.country.capital', False)
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('countries.edges.node.regions.pageInfo', False)
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.capital', False)
    query.setShow('countries.totalCount', False)
    
    print('countries.edges.cursor -> Hide')
    print('countries.edges.node.region.country.capital -> Hide')
    print('countries.edges.node.regions.pageInfo.hasNextPage -> Hide')
    print('countries.edges.node.regions.pageInfo -> Hide')
    print('countries.edges.node.callingCode -> Hide')
    print('countries.edges.node.capital -> Hide')
    print('countries.totalCount -> Hide')
    
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectShowChange")

async def testNestedObjectWithArgsAndVariables(): 
    print('\n\nRunning testNestedObjectWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    args = GQLArgsSet()
    args.addArg('first', 3)
    args.addArg(argKey='after', argValue='MTE=')
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectWithArgsAndVariables")

async def testNestedObjectWithLiteralValueArgs(): 
    print('\n\nRunning testNestedObjectWithLiteralValueArgs...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    args = GQLArgsSet()
    args.addArg('countryId', ID('CH'))
    query.setArgs(args, ArgType.LiteralValues)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectWithLiteralValueArgs")
          
async def testComplexObjectWithLiteralValueArgs(): 
    print('\n\nRunning testComplexObjectWithLiteralValueArgs...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    argsCntrs = GQLArgsSet('countries')
    argsCntrs.addArg('currencyCode', 'CNY')
    argsRegion = GQLArgsSet('countries.edges.node.region')
    argsRegion.addArg('code', "CH")
    query.setArgs([argsCntrs, argsRegion], ArgType.LiteralValues)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithLiteralValueArgs")
        
async def testComplexObjectWithLiteralValueArgs2(): 
    print('\n\nRunning testComplexObjectWithLiteralValueArgs2...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    argsRegion = GQLArgsSet('countries.edges.node.region')
    argsRegion.addArg('code', "CN")
    query.setArgs([argsRegion], ArgType.LiteralValues)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithLiteralValueArgs2")
        
async def testComplexObjectWithArgsAndVariables(): 
    print('\n\nRunning testComplexObjectWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    
    query.setShow('countries.edges.node.region', False)
    args = GQLArgsSet()
    args.addArg('first', 3)
    args.addArg('after', 'Mg==')
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithArgsAndVariables")

async def testNestedObjectShowChangeWithArgsAndVariables(): 
    print('\n\nRunning testNestedObjectShowChangeWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    query.setShow('currencies.edges.node.symbol', False)
    args = GQLArgsSet()
    args.addArg('countryId', ID("CH"))
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectShowChangeWithArgsAndVariables")

async def testNestedObjectWithLiteralValueArgsAndCursorPaginationArgs(): 
    print('\n\nRunning testNestedObjectWithLiteralValueArgsAndCursorPaginationArgs...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    args = GQLArgsSet()
    args.addArg('countryId', ID("CN"))
    query.setArgs(args, ArgType.LiteralValues)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectWithLiteralValueArgsAndCursorPaginationArgs")

async def testComplexObjectShowChangeWithArgsAndVariables(): 
    print('\n\nRunning testComplexObjectShowChangeWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    query.setShow('countries.edges.cursor', False)
    query.setShow('countries.edges.node.region', False)
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('countries.edges.node.regions.pageInfo', False)
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.capital', False)
    query.setShow('countries.totalCount', False)
    
    args = GQLArgsSet()
    args.addArg('first', 3)
    args.addArg('after', 'MTE=')
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectShowChangeWithArgsAndVariables")

async def testComplexObjectWithLiteralValueArgs2WithLog(): 
    print('\n\nRunning testComplexObjectWithLiteralValueArgs2WithLog...')
    try:
        query = GQLOperation(OperationType.query, countries, 'myCountriesQuery', logProgress=True)
        argsRegion = GQLArgsSet('countries.edges.node.region')
        argsRegion.addArg('code', "CN")
        query.setArgs([argsRegion], ArgType.LiteralValues)

        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response, True)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithLiteralValueArgs2WithLog")
 
class Language(Enum):
   """

   Language - The languages currently supported

   """

   DE = 'DE' ##German
   EN = 'EN' ##English
   ES = 'ES' ##Spanish
   FR = 'FR' ##French
   IT = 'IT' ##Italian
   PT = 'PT' ##Portuguese
   PT_BR = 'PT_BR' ##Portuguese (Brazil)
   RU = 'RU' ##Russian

async def testObjectWithComposedArgs(): 
    print('\n\nRunning testObjectWithComposedArgs...')
    try:
        query = GQLOperation(OperationType.query, Country, 'myCountryQuery', logProgress=True, rootName='country')
        argsRegion = GQLArgsSet()
        argsRegion.addArg('id', ID("CH"))
        argsRegion.addArg('displayOptions', {"asciiMode": True, "language": Language.EN })
        query.setArgs([argsRegion], ArgType.LiteralValues)

        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response, True)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.obj)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testObjectWithComposedArgs")

# def testGeneratedConnectionAsObject():
#     print('\n\nRunning testGeneratedConnectionAsObject...')
#     try:
#         query = GQLOperation(OperationType.query, Country, 'myCountryQuery', logProgress=True, rootName='country')
#         argsRegion = GQLArgsSet()
#         argsRegion.addArg('id', ID("CH"))
#         argsRegion.addArg('displayOptions', {"asciiMode": True, "language": Language.EN })
#         query.setArgs([argsRegion], ArgType.LiteralValues)

#         print('gqlSource GQL version: ' + query.exportGqlSource)
        
#         response = requests.request('POST', url=gdbcUrl, 
#                                     json= { "query": query.exportGqlSource },
#                                     headers=gdbcHeaders)
#         gqlResponse = GQLResponse(response, True)
        
#         gqlResponse.printMessageOutput()
#         gqlResponse.mapGQLDataToObj(query.obj)
#         print('resultObject: ' + str(gqlResponse.resultObject))
#     except Exception as ex:
#         ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
#     print("End of testGeneratedConnectionAsObject")