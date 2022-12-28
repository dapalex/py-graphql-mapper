import requests
from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse
from pygqlmap.gqlTypes import ID
from pygqlmap.helper import mapConfig
from consts import gdbcHeaders, gdbcUrl
from output.GeoDBCities.queries import country, currencies, countries
from utils import ManageException, redirectOutputToFile, restoreOutput

async def testNestedObject(): 
    print('\n\nRunning testNestedObject...')
    try:
        query = currencies()
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

async def testNestedObjectShowChange(): 
    print('\n\nRunning testNestedObjectShowChange...')
    query = currencies()
    query.name = 'MyCurrenciesQuery'
    
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
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectShowChange")

async def testComplexObjectShowChange(): 
    print('\n\nRunning testComplexObjectShowChange...')
    query = countries() 
    query.type.edges.node.region._args.code = "CH"
    query._argsType = ArgType.Variables
    
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
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectShowChange")

async def testNestedObjectWithArgsAndVariables(): 
    print('\n\nRunning testNestedObjectWithArgsAndVariables...')
    query = currencies() 
    query.name = 'myCurrenciesQuery'
    query._args.first = 3
    query._args.after = 'MTE='
    query._argsType = ArgType.Variables

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectWithArgsAndVariables")

async def testNestedObjectWithLiteralValueArgs(): 
    print('\n\nRunning testNestedObjectWithLiteralValueArgs...')
    query = currencies() 
    query._args.countryId = 'CH'

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectWithLiteralValueArgs")
          
async def testComplexObjectWithLiteralValueArgs(): 
    print('\n\nRunning testComplexObjectWithLiteralValueArgs...')
    from output.GeoDBCities.enums import IncludeDeletedFilterType
    query = countries() 
    query._args.currencyCode = 'CNY'
    query.type.edges.node.region._args.code = "CH"
    if int(mapConfig["recursionDepth"]) > 0:
        query.type.edges.node.region.populatedPlaces._args.includeDeleted = IncludeDeletedFilterType.SINCE_LAST_WEEK
        query.type.edges.node.region.populatedPlaces._args.namePrefix = "gua"
    query.type.edges.node.regions._args.namePrefix = 'gua' 
    query.type.edges.node.regions.edges.node.country
    
        
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithLiteralValueArgs")
        
async def testComplexObjectWithLiteralValueArgs2(): 
    print('\n\nRunning testComplexObjectWithLiteralValueArgs2...')
    query = countries() 
    query.type.edges.node.region._args.code = "CN"

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithLiteralValueArgs2")
        
async def testComplexObjectWithArgsAndVariables(): 
    print('\n\nRunning testComplexObjectWithArgsAndVariables...')
    query = countries() 
    query._args.first = 3
    query._args.after = 'Mg=='
    query.name = 'myCountriesQuery'
    
    query.setShow('countries.edges.node.region', False)
    query._argsType = ArgType.Variables

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectWithArgsAndVariables")

async def testNestedObjectShowChangeWithArgsAndVariables(): 
    print('\n\nRunning testNestedObjectShowChangeWithArgsAndVariables...')
    query = currencies()
    query._args.countryId = 'CH'
    query._argsType = ArgType.Variables

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testNestedObjectShowChangeWithArgsAndVariables")

async def testComplexObjectShowChangeWithArgsAndVariables(): 
    print('\n\nRunning testComplexObjectShowChangeWithArgsAndVariables...')
    query = countries()
    query._args.first = 3
    query._args.after = 'MTE='
    query.setShow('countries.edges.cursor', False)
    query.setShow('countries.edges.node.region', False)
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('countries.edges.node.regions.pageInfo', False)
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.capital', False)
    query.setShow('countries.totalCount', False)
    query._argsType = ArgType.Variables

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObjectShowChangeWithArgsAndVariables")

async def testObjectWithComposedArgs(): 
    print('\n\nRunning testObjectWithComposedArgs...')
    try:
        query = country()
        query.logProgress=True
        query._args.id = ID('CH')
        from output.GeoDBCities.enums import Language
        query._args.displayOptions = {"asciiMode": True, "language": Language.EN }
        query.type.region._args.code = 'Q12094'

        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource },
                                    headers=gdbcHeaders)
        gqlResponse = GQLResponse(response, True)
        
        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testObjectWithComposedArgs")
