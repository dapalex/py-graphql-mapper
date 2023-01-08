from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse, httpRequest
from pygqlmap.gqlTypes import ID
from pygqlmap.helper import mapConfig
from .consts import gdbcHeaders, gdbcUrl
from .output.GeoDBCities.queries import country, currencies, countries
import logging as logger

def runNestedObject():
    logger.info('\n\nRunning testNestedObject...')
    try:
        query = currencies()
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(currencies())
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testNestedObject")

def runNestedObjectShowChange():
    logger.info('\n\nRunning testNestedObjectShowChange...')
    query = currencies()
    query.name = 'MyCurrenciesQuery'

    # query.setShow('currencies.edges.cursor', False)
    query.setShow('currencies.edges.node.symbol', False)
    query.setShow('currencies.edges.node.countryCodes', False)
    query.setShow('currencies.edges.node', False)
    query.setShow('currencies.totalCount', False)
    # query.setShow('currencies.edges', False)
    query.setShow('currencies', False)

    logger.info('currencies.edges.node.symbol -> Hide')
    logger.info('currencies.edges.node.countryCodes -> Hide')
    # logger.info('currencies.edges.node -> Hide')
    logger.info('currencies.totalCount -> Hide')
    logger.info('currencies -> Hide')
    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testNestedObjectShowChange")

def runComplexObjectShowChange():
    logger.info('\n\nRunning testComplexObjectShowChange...')
    query = countries()
    query.type.edges.node.region._args.code = ID("CH")
    query._argsType = ArgType.Variables

    query.setShow('countries.edges.cursor', False)
    query.setShow('countries.edges.node.region.country.capital', False)
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('countries.edges.node.regions.pageInfo', False)
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.capital', False)
    query.setShow('countries.totalCount', False)

    logger.info('countries.edges.cursor -> Hide')
    logger.info('countries.edges.node.region.country.capital -> Hide')
    logger.info('countries.edges.node.regions.pageInfo.hasNextPage -> Hide')
    logger.info('countries.edges.node.regions.pageInfo -> Hide')
    logger.info('countries.edges.node.callingCode -> Hide')
    logger.info('countries.edges.node.capital -> Hide')
    logger.info('countries.totalCount -> Hide')

    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testComplexObjectShowChange")

def runNestedObjectWithArgsAndVariables():
    logger.info('\n\nRunning testNestedObjectWithArgsAndVariables...')
    query = currencies()
    query.name = 'myCurrenciesQuery'
    query._args.first = 3
    query._args.after = 'MTE='
    query._argsType = ArgType.Variables

    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)
        logger.info('variables GQL version: ' + query.exportGQLVariables)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testNestedObjectWithArgsAndVariables")

def runNestedObjectWithLiteralValueArgs():
    logger.info('\n\nRunning testNestedObjectWithLiteralValueArgs...')
    query = currencies()
    query._args.countryId = 'CH'

    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testNestedObjectWithLiteralValueArgs")

def runComplexObjectWithLiteralValueArgs():
    logger.info('\n\nRunning testComplexObjectWithLiteralValueArgs...')
    from .output.GeoDBCities.enums import IncludeDeletedFilterType
    query = countries()
    query._args.currencyCode = 'CNY'
    query.type.edges.node.region._args.code = "CH"
    if int(mapConfig["recursionDepth"]) > 0:
        query.type.edges.node.region.populatedPlaces._args.includeDeleted = IncludeDeletedFilterType.SINCE_LAST_WEEK
        query.type.edges.node.region.populatedPlaces._args.namePrefix = "gua"
    query.type.edges.node.regions._args.namePrefix = 'gua'
    query.type.edges.node.regions.edges.node.country


    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testComplexObjectWithLiteralValueArgs")

def runComplexObjectWithLiteralValueArgs2():
    logger.info('\n\nRunning testComplexObjectWithLiteralValueArgs2...')
    query = countries()
    query.type.edges.node.region._args.code = "CN"

    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testComplexObjectWithLiteralValueArgs2")

def runComplexObjectWithArgsAndVariables():
    logger.info('\n\nRunning testComplexObjectWithArgsAndVariables...')
    query = countries()
    query._args.first = 3
    query._args.after = 'Mg=='
    query.name = 'myCountriesQuery'

    query.setShow('countries.edges.node.region', False)
    query._argsType = ArgType.Variables

    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)
        logger.info('variables GQL version: ' + query.exportGQLVariables)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testComplexObjectWithArgsAndVariables")

def runNestedObjectShowChangeWithArgsAndVariables():
    logger.info('\n\nRunning testNestedObjectShowChangeWithArgsAndVariables...')
    query = currencies()
    query._args.countryId = ID('CH')
    query._argsType = ArgType.Variables

    try:
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)
        logger.info('variables GQL version: ' + query.exportGQLVariables)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testNestedObjectShowChangeWithArgsAndVariables")

def runComplexObjectShowChangeWithArgsAndVariables():
    logger.info('\n\nRunning testComplexObjectShowChangeWithArgsAndVariables...')
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
        logger.info('gqlSource GQL version: ' + query.exportGqlSource)
        logger.info('variables GQL version: ' + query.exportGQLVariables)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource, "variables": query.exportGQLVariables },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testComplexObjectShowChangeWithArgsAndVariables")

def runObjectWithComposedArgs():
    logger.info('\n\nRunning testObjectWithComposedArgs...')
    try:
        query = country()
        query.logProgress=True
        query._args.id = ID('CH')
        from .output.GeoDBCities.enums import Language
        query._args.displayOptions = {"asciiMode": True, "language": Language.EN }
        query.type.region._args.code = 'Q12094'

        logger.info('gqlSource GQL version: ' + query.exportGqlSource)

        response = httpRequest(gdbcUrl,
                                     { "query": query.exportGqlSource },
                                    gdbcHeaders)
        gqlResponse = GQLResponse(response, True)

        gqlResponse.printMessageOutput()
        gqlResponse.mapGQLDataToObj(query.type)
        logger.info('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of testObjectWithComposedArgs")
