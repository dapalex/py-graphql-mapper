from .output.github.gql_types import AddCommentInput
from .consts import GDBC_HEADERS, GDBC_URL, GITHUB_HEADERS, GITHUB_URL
import logging as logger
from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse
import requests
from pygqlmap.gql_types import ID
from pygqlmap.helper import mapConfig
from .consts import GDBC_HEADERS, GDBC_URL
from .output.gdbc.queries import country, currencies, countries
import logging as logger

def run_nested_obj_args_literal():
    logger.debug('\n\nRunning run_nested_obj_args_literal...')
    query = currencies(countryId="CH")
    # query._args.countryId = 'CH'

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_nested_obj_args_literal")

def run_nested_obj_args_vars():
    logger.debug('\n\nRunning run_nested_obj_args_vars...')
    query = currencies(first=3, after='MTE=')
    query.name = 'myCurrenciesQuery'
    # query._args.first = 3
    # query._args.after = 'MTE='
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_nested_obj_args_vars")

def run_complex_obj_args_literal():
    logger.debug('\n\nRunning run_complex_obj_args_literal...')
    from .output.gdbc.enums import IncludeDeletedFilterType
    query = countries(currencyCode='CNY')
    # query._args.currencyCode = 'CNY'
    query.type.edges.node.region = type(query.type.edges.node.region)(code="CH")
    # query.type.edges.node.region._args.code = "CH"
    if int(mapConfig["recursionDepth"]) > 0:
        query.type.edges.node.region.populatedPlaces._args.includeDeleted = IncludeDeletedFilterType.SINCE_LAST_WEEK
        query.type.edges.node.region.populatedPlaces._args.namePrefix = "gua"
    query.type.edges.node.regions._args.namePrefix = 'gua'
    query.type.edges.node.regions.edges.node.country


    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_complex_obj_args_literal")

def run_complex_obj_args_vars():
    logger.debug('\n\nRunning run_complex_obj_args_vars...')
    query = countries(first=3, after='Mg==')
    # query._args.first = 3
    # query._args.after = 'Mg=='
    query.name = 'myCountriesQuery'

    query.set_show('countries.edges.node.region', False)
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_complex_obj_args_vars")

def run_complex_obj_viewchange_args_literal():
    logger.debug('\n\nRunning run_complex_obj_viewchange_args_literal...')
    query = countries()
    query.type.edges.node.region = type(query.type.edges.node.region)(code=ID("CH"))
    query._args_type = ArgType.LITERAL_VALUES

    query.set_show('countries.edges.cursor', False)
    query.set_show('countries.edges.node.region.country.capital', False)
    query.set_show('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.set_show('countries.edges.node.regions.pageInfo', False)
    query.set_show('countries.edges.node.callingCode', False)
    query.set_show('countries.edges.node.capital', False)
    query.set_show('countries.totalCount', False)

    logger.debug('countries.edges.cursor -> Hide')
    logger.debug('countries.edges.node.region.country.capital -> Hide')
    logger.debug('countries.edges.node.regions.pageInfo.hasNextPage -> Hide')
    logger.debug('countries.edges.node.regions.pageInfo -> Hide')
    logger.debug('countries.edges.node.callingCode -> Hide')
    logger.debug('countries.edges.node.capital -> Hide')
    logger.debug('countries.totalCount -> Hide')

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_complex_obj_viewchange_args_literal")

def run_complex_obj_viewchange_args_vars():
    logger.debug('\n\nRunning run_complex_obj_viewchange_args_vars...')
    query = countries(first = 3, after = 'MTE=')
    # query._args.first = 3
    # query._args.after = 'MTE='
    query.set_show('countries.edges.cursor', False)
    query.set_show('countries.edges.node.region', False)
    query.set_show('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.set_show('countries.edges.node.regions.pageInfo', False)
    query.set_show('countries.edges.node.callingCode', False)
    query.set_show('countries.edges.node.capital', False)
    query.set_show('countries.totalCount', False)
    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('variables GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_complex_obj_viewchange_args_vars")

def run_obj_composed_args_literal():
    logger.debug('\n\nRunning run_obj_composed_args_literal...')
    try:
        from .output.gdbc.enums import Language
        from .output.gdbc.gql_types import DisplayOptions

        disp_opt = DisplayOptions()
        disp_opt.asciiMode = True
        disp_opt.language = Language.EN
        query = country(id = ID('CH'), displayOptions = disp_opt)
        query.log_progress=True
        query.type.region = type(query.type.region)(code = 'Q12094')

        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response, True)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_obj_composed_args_literal")

def run_obj_composed_args_vars():
    logger.debug('\n\nRunning run_obj_composed_args_vars...')
    try:
        from .output.gdbc.enums import Language
        from .output.gdbc.gql_types import DisplayOptions

        disp_opt = DisplayOptions()
        disp_opt.asciiMode = True
        disp_opt.language = Language.EN
        query = country(id = ID('CH'), displayOptions = disp_opt)
        query._args_type = ArgType.VARIABLES
        query.log_progress=True
        query.type.region = type(query.type.region)(code = ID('Q12094'))

        logger.debug('gqlSource GQL version: ' + query.export_gql_source)
        logger.debug('gqlSource GQL version: ' + query.export_gqlvariables)

        response = requests.request('POST', url=GDBC_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=GDBC_HEADERS)
        gqlResponse = GQLResponse(response, True)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_obj_composed_args_vars")

def run_add_comment_mutation_args_literal():
    logger.debug('\nRunning run_add_comment_mutation_args_literal... - stack limit for recursion depth')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations #, ProjectV2Order, ProjectV2OrderField

        mut_input = AddCommentInput()
        mut_input.subjectId = 'something'
        mut_input.body = 'This is the body'
        mut_input.clientMutationId = 'Me'
        mutation = Mutations.addComment.value(input=mut_input)
        # restoreOutput(wrapper)
        logger.debug('Inserting python mutation input data...')
        mutation.type.commentEdge.node.repository.packages = type(mutation.type.commentEdge.node.repository.packages)(repositoryId='ghjk')
        mutation.type.commentEdge.node.repository.discussion._args.number = 3
        mutation.type.commentEdge.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.commentEdge.node.repository.environment._args.name = 'envName'
        mutation.type.commentEdge.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.commentEdge.node.repository.release._args.tagName = 'aTag'
        mutation.type.commentEdge.node.repository.label._args.name = 'aName'
        mutation.type.commentEdge.node.repository.milestone._args.number = 0
        from .output.github.gql_types import Package, PackageEdge
        pack = Package()
        pack.version._args.version = '2'
        mutation.type.commentEdge.node.repository.packages.nodes = [pack]
        pack_edge = PackageEdge()
        pack_edge.node.version._args.version = '2.6'
        mutation.type.commentEdge.node.repository.packages.edges = [pack_edge]
        mutation.type.commentEdge.node.repository.project._args.number = 1

        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL, json={ "query": mutation.export_gql_source }, headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_add_comment_mutation_args_literal")

def run_add_comment_mutation_args_vars():
    logger.debug('\nRunning run_add_comment_mutation_args_vars... - stack limit for recursion depth')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations #, ProjectV2Order, ProjectV2OrderField

        mut_input = AddCommentInput()
        mut_input.subjectId = 'something'
        mut_input.body = 'This is the body'
        mut_input.clientMutationId = 'Me'
        mutation = Mutations.addComment.value(input=mut_input)
        mutation._args_type = ArgType.VARIABLES

        logger.debug('Inserting python mutation input data...')
        mutation.type.commentEdge.node.repository.packages = type(mutation.type.commentEdge.node.repository.packages)(repositoryId='ghjk')
        mutation.type.commentEdge.node.repository.discussion._args.number = 3
        mutation.type.commentEdge.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.commentEdge.node.repository.environment._args.name = 'envName'
        mutation.type.commentEdge.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.commentEdge.node.repository.release._args.tagName = 'aTag'
        mutation.type.commentEdge.node.repository.label._args.name = 'aName'
        mutation.type.commentEdge.node.repository.milestone._args.number = 0
        from .output.github.gql_types import Package, PackageEdge
        pack = Package()
        pack.version._args.version = '2'
        mutation.type.commentEdge.node.repository.packages.nodes = [pack]
        pack_edge = PackageEdge()
        pack_edge.node.version._args.version = '2.6'
        mutation.type.commentEdge.node.repository.packages.edges = [pack_edge]
        mutation.type.commentEdge.node.repository.project._args.number = 1

        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL, json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables  }, headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_add_comment_mutation_args_vars")