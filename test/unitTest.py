from enums import OperationType, ArgType
from gqlTypes import GQLOperation, GQLArgs, ID, GQLArg
from network import GQLResponse
from models.countries import countries
from models.objSamples import currency, currencies, plainComplexQueryWVar, plainComplexVariables, plainNestedQuery
from gdbcApi.client import gdbcClient

async def testPlainNestedQueryCurrencies(): 
    print('\n\nRunning testPlainNestedQueryCurrencies...')
    try:
        response = gdbcClient.ExecuteQuery(plainNestedQuery)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(currencies())
            print('resultObject: ' + str(gqlResponse.resultObject))
    except:
        print('!!ExecuteQuery FAILED!!')

async def testPlainComplexQueryCountries(): 
    print('\n\nRunning testPlainComplexQueryCountries...')
    try:
        response = gdbcClient.ExecuteQuery(plainComplexQueryWVar, variables=plainComplexVariables)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(countries())
            print('resultObject: ' + str(gqlResponse.resultObject))
    except:
        print('!!ExecuteQuery FAILED!!')

async def testSimpleObject(): 
    print('\n\nRunning testSimpleObject...')
    query = GQLOperation(OperationType.query, currency, 'myCurrencyQuery')
    
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except:
        print('ExecuteQuery FAILED - Expected')

async def testNestedObject(): 
    print('\n\nRunning testNestedObject...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except:
        print('!!ExecuteQuery FAILED!!')

async def testComplexObject(): 
    print('\n\nRunning testComplexObject...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery') 
    
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testSimpleObjectShowChange(): 
    print('\n\nRunning testSimpleObjectShowChange...')
    query = GQLOperation(OperationType.query, currency, 'myCurrencyQuery')
    
    query.setShow('currency.symbol', False)
    query.setShow('currency', False)
    print('currency.symbol -> Hide')
    print('currency -> Hide')
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('ExecuteQuery FAILED - expected')

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
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testComplexObjectShowChange(): 
    print('\n\nRunning testComplexObjectShowChange...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery') 
    
    query.setShow('countries.edges.cursor', False)
    # query.setShow('countries.edges.node.region.country', False)
    query.setShow('countries.edges.node.region.country.capital', False)
    try:
        query.setShow('countries.edges.node.regions.pageInfo.nextCursor', False)
    except:
        pass
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('countries.edges.node.regions.pageInfo', False)
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.capital', False)
    # query.setShow('countries.edges.node', False)
    try:
        query.setShow('countries.edges.totalCount', False)
    except:
        pass
    # query.setShow('countries.edges', False) ##becomes gqledge?
    query.setShow('countries.totalCount', False)
    # query.setShow('countries', False)
    print('countries.edges.cursor -> Hide')
    print('countries.edges.node.region.country.capital -> Hide')
    print('countries.edges.node.regions.pageInfo.hasNextPage -> Hide')
    print('countries.edges.node.regions.pageInfo -> Hide')
    print('countries.edges.node.callingCode -> Hide')
    print('countries.edges.node.capital -> Hide')
    print('countries.totalCount -> Hide')
    
    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if response.status_code == 500:
            print("HTTP 500 expected, waiting for args")
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testNestedObjectWithArgsAndVariables(): 
    print('\n\nRunning testNestedObjectWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    args = GQLArgs()
    args.addArg(GQLArg(name='first', value=3))
    args.addArg(GQLArg(name='after', value='MTE='))
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource, variables=query.exportGQLVariables)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testNestedObjectWithEmbeddedArgs(): 
    print('\n\nRunning testNestedObjectWithEmbeddedArgs...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    args = GQLArgs()
    args.addArg(GQLArg('countryId', ID('CH')))
    query.setArgs(args, ArgType.EmbeddedArgs)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')
          
async def testComplexObjectWithEmbeddedArgs(): 
    print('\n\nRunning testComplexObjectWithEmbeddedArgs...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    argsCntrs = GQLArgs('countries')
    argsCntrs.addArg(GQLArg('currencyCode', 'CNY'))
    argsRegion = GQLArgs('countries.edges.node.region')
    argsRegion.addArg(GQLArg('code', "CH"))
    # argsRegion.addArg(GQLArg('types', ["CITY"]))
    query.setArgs([argsCntrs, argsRegion], ArgType.EmbeddedArgs)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')
        
async def testComplexObjectWithEmbeddedArgs2(): 
    print('\n\nRunning testComplexObjectWithEmbeddedArgs2...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    # argsCntrs = GQLArgs('countries')
    # argsCntrs.addArg(GQLArg('currencyCode', 'CNY'))
    argsRegion = GQLArgs('countries.edges.node.region')
    argsRegion.addArg(GQLArg('code', "CN"))
    # argsRegion.addArg(GQLArg('types', ["CITY"]))
    query.setArgs([argsRegion], ArgType.EmbeddedArgs)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')
        
async def testComplexObjectWithArgsAndVariables(): 
    print('\n\nRunning testComplexObjectWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    args = GQLArgs()
    args.addArg(GQLArg(name='first', value=3))
    args.addArg(GQLArg(name='after', value='Mg=='))
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource, variables=query.exportGQLVariables)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testNestedObjectShowChangeWithArgsAndVariables(): 
    print('\n\nRunning testNestedObjectShowChangeWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    query.setShow('currencies.edges.node.symbol', False)
    args = GQLArgs()
    args.addArg(GQLArg(name='countryId', value=ID("CH")))
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource, variables=query.exportGQLVariables)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testNestedObjectWithEmbeddedArgsAndCursorPaginationArgs(): 
    print('\n\nRunning testNestedObjectWithEmbeddedArgsAndCursorPaginationArgs...')
    query = GQLOperation(OperationType.query, currencies, 'myCurrenciesQuery')
    args = GQLArgs()
    args.addArg(GQLArg('countryId', ID("CN")))
    query.setArgs(args, ArgType.EmbeddedArgs)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testComplexObjectShowChangeWithArgsAndVariables(): 
    print('\n\nRunning testComplexObjectShowChangeWithArgsAndVariables...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
    query.setShow('countries.edges.cursor', False)
    query.setShow('countries.edges.node.region.country', False)
    query.setShow('countries.edges.node.region.country.capital', False)
    try:
        query.setShow('countries.edges.node.regions.pageInfo.nextCursor', False)
    except:
        pass
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('countries.edges.node.regions.pageInfo', False)
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.capital', False)
    # query.setShow('countries.edges.node', False)
    try:
        query.setShow('countries.edges.totalCount', False)
    except:
        pass
    # query.setShow('countries.edges', False) ##becomes gqledge?
    query.setShow('countries.totalCount', False)
    # query.setShow('countries', False)
    args = GQLArgs()
    args.addArg(GQLArg(name='first', value=3))
    args.addArg(GQLArg(name='after', value='MTE='))
    query.setArgs(args, ArgType.Variables)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        print('variables GQL version: ' + query.exportGQLVariables)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource, variables=query.exportGQLVariables)
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')

async def testComplexObjectWithEmbeddedArgs2WithLog(): 
    print('\n\nRunning testComplexObjectWithEmbeddedArgs2WithLog...')
    query = GQLOperation(OperationType.query, countries, 'myCountriesQuery', True)
    # argsCntrs = GQLArgs('countries')
    # argsCntrs.addArg(GQLArg('currencyCode', 'CNY'))
    argsRegion = GQLArgs('countries.edges.node.region')
    argsRegion.addArg(GQLArg('code', "CN"))
    # argsRegion.addArg(GQLArg('types', ["CITY"]))
    query.setArgs([argsRegion], ArgType.EmbeddedArgs)

    try:
        print('gqlSource GQL version: ' + query.exportGqlSource)
        
        response = gdbcClient.ExecuteQuery(query.exportGqlSource)
        gqlResponse = GQLResponse(response, True)
        
        gqlResponse.printMessageOutput()
        if hasattr(gqlResponse, 'data'):
            gqlResponse.mapGQLDataToObj(query.data)
            print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception:
        print('!!ExecuteQuery FAILED!!')
        