from datetime import datetime
from pygqlmap.enums import ArgType
from pygqlmap.network import GQLResponse
import requests
from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from .consts import GITHUB_HEADERS, GITHUB_URL
import logging as logger
from .utils import stringifyresult

def run_fetch_gh_schema():
    logger.debug('\nRunning run_fetch_gh_schema...')

    try:
        logger.debug('Calling GraphQL Server...')
        gqlSchema = fetch_schema_obj(GITHUB_URL, GITHUB_HEADERS, QUERY_SCHEMA_AND_TYPES)
        logger.debug('Response Received')

        if gqlSchema:
            logger.debug('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\github\\', log_progress=True, add_desc=True)

            logger.debug('Python types generated')
    except Exception as ex:
        raise ex

    logger.debug("End of run_fetch_gh_schema")

def run_fetch_gh_schema_no_desc():
    logger.debug('\nRunning run_fetch_gh_schema_no_desc...')

    try:
        logger.debug('Calling GraphQL Server...')
        gqlSchema = fetch_schema_obj(GITHUB_URL, GITHUB_HEADERS, QUERY_SCHEMA_AND_TYPES)
        logger.debug('Response Received')

        if gqlSchema:
            logger.debug('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\github_nodesc\\', log_progress=True, add_desc=False)

            logger.debug('Python types generated')
    except Exception as ex:
        raise ex

    logger.debug("End of run_fetch_gh_schema_no_desc")

def run_gh_licenses_query_with_list():
    logger.debug('\nRunning run_gh_licenses_query_with_list...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.queries import licenses

        query = licenses()

        logger.debug(query.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": query.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_licenses_query_with_list")

def run_add_comment_mutation_literal():
    logger.debug('\nRunning run_add_comment_mutation_literal... - stack limit for recursion depth')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations #, ProjectV2Order, ProjectV2OrderField

        mutation = Mutations.addComment.value()
        # restoreOutput(wrapper)
        logger.debug('Inserting python mutation input data...')

        mutation._args.input.subjectId = 'something'
        mutation._args.input.body = 'This is the body'
        mutation._args.input.clientMutationId = 'Me'
        mutation.type.commentEdge.node.repository.discussion._args.number = 3
        mutation.type.commentEdge.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.commentEdge.node.repository.environment._args.name = 'envName'
        mutation.type.commentEdge.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.commentEdge.node.repository.release._args.tagName = 'aTag'
        mutation.type.commentEdge.node.repository.label._args.name = 'aName'
        mutation.type.commentEdge.node.repository.milestone._args.number = 0
        mutation.type.commentEdge.node.repository.packages._args.repositoryId = 'ghjk'
        from .output.github.gql_types import Package, PackageEdge
        pack = Package()
        pack.version._args.version = '2'
        mutation.type.commentEdge.node.repository.packages.nodes = [pack]
        pack_edge = PackageEdge()
        pack_edge.node.version._args.version = '2.6'
        mutation.type.commentEdge.node.repository.packages.edges = [pack_edge]
        mutation.type.commentEdge.node.repository.project._args.number = 1

        # wrapper = redirectOutputToFile('mutationCreated.log')
        logger.debug(mutation.export_gql_source)
        # restoreOutput(wrapper)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL, json={ "query": mutation.export_gql_source }, headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_add_comment_mutation_literal")

def run_add_comment_mutation_vars():
    logger.debug('\nRunning run_add_comment_mutation_vars... - stack limit for recursion depth')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations #, ProjectV2Order, ProjectV2OrderField

        mutation = Mutations.addComment.value()
        # restoreOutput(wrapper)
        logger.debug('Inserting python mutation input data...')

        mutation._args.input.subjectId = 'something'
        mutation._args.input.body = 'This is the body'
        mutation._args.input.clientMutationId = 'Me'
        mutation.type.commentEdge.node.repository.discussion._args.number = 3
        mutation.type.commentEdge.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.commentEdge.node.repository.environment._args.name = 'envName'
        mutation.type.commentEdge.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.commentEdge.node.repository.release._args.tagName = 'aTag'
        mutation.type.commentEdge.node.repository.label._args.name = 'aName'
        mutation.type.commentEdge.node.repository.milestone._args.number = 0
        mutation.type.commentEdge.node.repository.packages._args.repositoryId = 'ghjk'
        from .output.github.gql_types import Package, PackageEdge
        pack = Package()
        pack.version._args.version = '2'
        mutation.type.commentEdge.node.repository.packages.nodes = [pack]
        pack_edge = PackageEdge()
        pack_edge.node.version._args.version = '2.6'
        mutation.type.commentEdge.node.repository.packages.edges = [pack_edge]
        mutation.type.commentEdge.node.repository.project._args.number = 1

        mutation._args_type = ArgType.VARIABLES
        # wrapper = redirectOutputToFile('mutationCreated.log')
        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)
        # restoreOutput(wrapper)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL, json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables }, headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_add_comment_mutation_vars")

def run_gh_update_repo_mutation_literal():
    logger.debug('\nRunning run_gh_update_repo_mutation_literal...')
    try:
        from .output.github.mutations import Mutations

        logger.debug('Creating mutation python object...')
        mutation = Mutations.updateRepository.value()
        logger.debug('Inserting python mutation input data...')

        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.hasIssuesEnabled = True
        mutation._args.input.hasWikiEnabled = True
        mutation.type.repository.deployKeys = type(mutation.type.repository.deployKeys)(first=1, after='')
        mutation.type.repository.discussion._args.number = 1
        mutation.type.repository.discussions = type(mutation.type.repository.discussions)(first=1, after='')
        mutation.type.repository.discussionCategory._args.slug = "1"
        mutation.type.repository.discussionCategories = type(mutation.type.repository.discussionCategories)(first=1, after='')
        mutation.type.repository.environment._args.name = "nm"
        mutation.type.repository.label._args.name = "nmLbl"
        mutation.type.repository.milestone._args.number = 2
        from .output.github.gql_types import Package
        package = Package()
        package.version._args.version = "v13"
        mutation.type.repository.packages.nodes = [package]
        mutation.type.repository.project._args.number = 4
        mutation.type.repository.refs._args.refPrefix = 'pref'
        mutation.type.repository.release._args.tagName = 'tagE'
        mutation.type.repository.branchProtectionRules._args.first = 4
        mutation.type.repository.branchProtectionRules._args.after = ''
        mutation.type.repository.assignableUsers._args.first = 3
        mutation.type.repository.assignableUsers._args.after = ''

        mutation.type.repository.packages.edges.node.version._args.version = '1'
        mutation.type.repository.deployKeys._args.first = 6
        mutation.type.repository.deployments._args.first = 6

        logger.debug('Creating GQLOperation for mutation...')
        logger.debug(mutation.export_gql_source)

        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_update_repo_mutation_literal")

def run_gh_update_repo_mutation_vars():
    logger.debug('\nRunning run_gh_update_repo_mutation_vars...')
    try:
        from .output.github.mutations import Mutations

        logger.debug('Creating mutation python object...')
        mutation = Mutations.updateRepository.value()
        logger.debug('Inserting python mutation input data...')

        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.hasIssuesEnabled = True
        mutation._args.input.hasWikiEnabled = True
        mutation.type.repository.deployKeys = type(mutation.type.repository.deployKeys)(first=1, after='')
        mutation.type.repository.discussion._args.number = 1
        mutation.type.repository.discussions = type(mutation.type.repository.discussions)(first=1, after='')
        mutation.type.repository.discussionCategory._args.slug = "345"
        mutation.type.repository.discussionCategories = type(mutation.type.repository.discussionCategories)(first=1, after='')
        mutation.type.repository.environment._args.name = "nm"
        mutation.type.repository.environments = type(mutation.type.repository.environments)(first=1, after='')
        mutation.type.repository.label._args.name = "nmLbl"
        mutation.type.repository.milestone._args.number = 2
        from .output.github.gql_types import Package
        package = Package()
        package.version._args.version = "v13"
        mutation.type.repository.packages.nodes = [package]
        mutation.type.repository.project._args.number = 4
        mutation.type.repository.refs._args.refPrefix = 'pref'
        mutation.type.repository.release._args.tagName = 'tagE'
        mutation.type.repository.branchProtectionRules._args.first = 2
        mutation.type.repository.branchProtectionRules._args.after = ''
        mutation.type.repository.assignableUsers._args.first = 6
        mutation.type.repository.assignableUsers._args.after = ''

        mutation.type.repository.packages.edges.node.version._args.version = '2'
        mutation.type.repository.deployKeys._args.first = 5
        mutation.type.repository.deployments._args.first = 6

        mutation._args_type = ArgType.VARIABLES

        logger.debug('Creating GQLOperation for mutation...')
        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)

        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables },
                                    headers=GITHUB_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_update_repo_mutation_vars")

def run_gh_create_proj_mutation_literal():
    logger.debug('\nRunning run_gh_create_proj_mutation_literal...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateProjectInput

        mutation = Mutations.createProject.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = CreateProjectInput()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.name = "Test create project from Mutation" + datetime.now().ctime()
        mutation._args.input.repositoryIds = ["R_kgDOH7MI4g"]

        mutation.name = 'MycreateProjectMutation'

        mutation.type.project.columns._args.first = 2
        mutation.type.project.columns._args.after = ''
        mutation.type.project.owner.projects._args.first = 7
        mutation.type.project.owner.projects._args.after = ''

        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)
        gqlResponse.print_msg_out()

        if hasattr(gqlResponse.data, 'createProject') and hasattr(gqlResponse.data['createProject'], 'project'):
            with open('projectsCreated.log', 'a') as logProjCreated:
                logProjCreated.write(gqlResponse.data['createProject']['project']['id'] + '\n')

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_create_proj_mutation_literal")

def run_gh_create_proj_mutation_vars():
    logger.debug('\nRunning run_gh_create_proj_mutation_vars...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateProjectInput

        mutation = Mutations.createProject.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = CreateProjectInput()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.name = "Test create project from Mutation" + datetime.now().ctime()
        mutation._args.input.repositoryIds = ["R_kgDOH7MI4g"]

        mutation.name = 'MycreateProjectMutation'

        mutation.type.project.columns._args.first = 2
        mutation.type.project.columns._args.after = ''
        mutation.type.project.owner.projects._args.first = 4
        mutation.type.project.owner.projects._args.after = ''

        mutation._args_type = ArgType.VARIABLES

        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)
        gqlResponse.print_msg_out()

        if hasattr(gqlResponse.data, 'createProject') and hasattr(gqlResponse.data['createProject'], 'project'):
            with open('projectsCreated.log', 'a') as logProjCreated:
                logProjCreated.write(gqlResponse.data['createProject']['project']['id'] + '\n')

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_create_proj_mutation_vars")

def run_gh_delete_proj_mutation_literal():
    logger.debug('\nRunning run_gh_delete_proj_mutation_literal...')
    try:

        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import DeleteProjectInput

        mutation = Mutations.deleteProject.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectInput()

        mutation._args.input.projectId = "projId"

        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_delete_proj_mutation_literal")

def run_gh_delete_proj_mutation_vars():
    logger.debug('\nRunning run_gh_delete_proj_mutation_vars...')
    try:

        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import DeleteProjectInput

        mutation = Mutations.deleteProject.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectInput()

        mutation._args.input.projectId = "projId"

        mutation._args_type = ArgType.VARIABLES

        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_delete_proj_mutation_vars")

def run_gh_create_projectV2_mutation_literal():
    logger.debug('\nRunning run_gh_create_projectV2_mutation_literal...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateProjectV2Input

        mutation = Mutations.createProjectV2.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = CreateProjectV2Input()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()

        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_create_projectV2_mutation_literal")

def run_gh_create_projectV2_mutation_vars():
    logger.debug('\nRunning run_gh_create_projectV2_mutation_vars...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateProjectV2Input

        mutation = Mutations.createProjectV2.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = CreateProjectV2Input()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()

        mutation._args_type = ArgType.VARIABLES

        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_create_projectV2_mutation_vars")

def run_gh_delete_projectV2_mutation_literal():
    logger.debug('\nRunning run_gh_delete_projectV2_mutation_literal...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import DeleteProjectV2ItemInput

        mutation = Mutations.deleteProjectV2Item.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectV2ItemInput()

        mutation._args.input.projectId = "projId"
        mutation._args.input.itemId = "itemId"

        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_delete_projectV2_mutation_literal")

def run_gh_delete_projectV2_mutation_vars():
    logger.debug('\nRunning run_gh_delete_projectV2_mutation_vars...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import DeleteProjectV2ItemInput

        mutation = Mutations.deleteProjectV2Item.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectV2ItemInput()

        mutation._args.input.projectId = "projId"
        mutation._args.input.itemId = "itemId"

        mutation._args_type = ArgType.VARIABLES

        logger.debug(mutation.export_gql_source)
        logger.debug(mutation.export_gqlvariables)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_delete_projectV2_mutation_vars")

def run_gh_create_issue_mutation_literal():
    logger.debug('\nRunning run_gh_create_issue_mutation_literal...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateIssueInput

        mutation = Mutations.createIssue.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = CreateIssueInput()

        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()
        mutation._args.input.assigneeIds = ["MDQ6VXNlcjkxMzk2ODM3"]
        mutation._args.input.labelIds = ['LA_kwDOIOMoaM8AAAABFmBXvg', 'LA_kwDOIOMoaM8AAAABFmBXvQ']
        mutation._args.input.projectIds = ['PRO_kwHOBXKa5c4A32ah']

        mutation.type.issue.repository.discussion._args.number = 1
        mutation.type.issue.repository.discussionCategory._args.slug = "1"
        mutation.type.issue.repository.environment._args.name = "nm"
        mutation.type.issue.repository.label._args.name = "nmLbl"
        mutation.type.issue.repository.milestone._args.number = 2
        from .output.github.gql_types import Package, PackageEdge
        pack = Package()
        pack.version._args.version = "v13"
        pack_edge = PackageEdge()
        pack_edge.node.version._args.version = '2.6'
        mutation.type.issue.repository.packages.edges = [pack_edge]
        mutation.type.issue.repository.packages.nodes = [pack]
        mutation.type.issue.repository.project._args.number = 4
        mutation.type.issue.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.repository.release._args.tagName = 'tagE'


        mutation.type.issue.comments.edges.node.repository.discussion._args.number = 3
        mutation.type.issue.comments.edges.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.issue.comments.edges.node.repository.environment._args.name = 'envName'
        mutation.type.issue.comments.edges.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.comments.edges.node.repository.release._args.tagName = 'aTag'
        mutation.type.issue.comments.edges.node.repository.label._args.name = 'aName'
        mutation.type.issue.comments.edges.node.repository.milestone._args.number = 0
        mutation.type.issue.comments.edges.node.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.issue.comments.edges.node.repository.packages.nodes.version._args.version = '2'
        mutation.type.issue.comments.edges.node.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.issue.comments.edges.node.repository.project._args.number = 1

        mutation.type.issue.comments.nodes.repository.discussion._args.number = 3
        mutation.type.issue.comments.nodes.repository.discussionCategory._args.slug = 'slug'
        mutation.type.issue.comments.nodes.repository.environment._args.name = 'envName'
        mutation.type.issue.comments.nodes.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.comments.nodes.repository.release._args.tagName = 'aTag'
        mutation.type.issue.comments.nodes.repository.label._args.name = 'aName'
        mutation.type.issue.comments.nodes.repository.milestone._args.number = 0
        mutation.type.issue.comments.nodes.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.issue.comments.nodes.repository.packages.nodes.version._args.version = '2'
        mutation.type.issue.comments.nodes.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.issue.comments.nodes.repository.project._args.number = 1
        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_create_issue_mutation_literal")

def run_gh_create_issue_mutation_vars():
    logger.debug('\nRunning run_gh_create_issue_mutation_vars...')
    try:
        logger.debug('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateIssueInput

        mutation = Mutations.createIssue.value()
        logger.debug('Inserting python mutation input data...')
        mutation._args.input = CreateIssueInput()

        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()
        mutation._args.input.assigneeIds = ["MDQ6VXNlcjkxMzk2ODM3"]
        mutation._args.input.labelIds = ['LA_kwDOIOMoaM8AAAABFmBXvg', 'LA_kwDOIOMoaM8AAAABFmBXvQ']
        mutation._args.input.projectIds = ['PRO_kwHOBXKa5c4A32ah']

        mutation.type.issue.repository.discussion._args.number = 1
        mutation.type.issue.repository.discussionCategory._args.slug = "1"
        mutation.type.issue.repository.environment._args.name = "nm"
        mutation.type.issue.repository.label._args.name = "nmLbl"
        mutation.type.issue.repository.milestone._args.number = 2
        from .output.github.gql_types import Package, PackageEdge
        pack = Package()
        pack.version._args.version = "v13"
        pack_edge = PackageEdge()
        pack_edge.node.version._args.version = '2.6'
        mutation.type.issue.repository.packages.edges = [pack_edge]
        mutation.type.issue.repository.packages.nodes = [pack]
        mutation.type.issue.repository.project._args.number = 4
        mutation.type.issue.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.repository.release._args.tagName = 'tagE'


        mutation.type.issue.comments.edges.node.repository.discussion._args.number = 3
        mutation.type.issue.comments.edges.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.issue.comments.edges.node.repository.environment._args.name = 'envName'
        mutation.type.issue.comments.edges.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.comments.edges.node.repository.release._args.tagName = 'aTag'
        mutation.type.issue.comments.edges.node.repository.label._args.name = 'aName'
        mutation.type.issue.comments.edges.node.repository.milestone._args.number = 0
        mutation.type.issue.comments.edges.node.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.issue.comments.edges.node.repository.packages.nodes.version._args.version = '2'
        mutation.type.issue.comments.edges.node.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.issue.comments.edges.node.repository.project._args.number = 1

        mutation.type.issue.comments.nodes.repository.discussion._args.number = 3
        mutation.type.issue.comments.nodes.repository.discussionCategory._args.slug = 'slug'
        mutation.type.issue.comments.nodes.repository.environment._args.name = 'envName'
        mutation.type.issue.comments.nodes.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.comments.nodes.repository.release._args.tagName = 'aTag'
        mutation.type.issue.comments.nodes.repository.label._args.name = 'aName'
        mutation.type.issue.comments.nodes.repository.milestone._args.number = 0
        mutation.type.issue.comments.nodes.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.issue.comments.nodes.repository.packages.nodes.version._args.version = '2'
        mutation.type.issue.comments.nodes.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.issue.comments.nodes.repository.project._args.number = 1

        mutation._args_type = ArgType.VARIABLES

        logger.debug(mutation.export_gql_source)

        logger.debug('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source, "variables": mutation.export_gqlvariables },
                                    headers=GITHUB_HEADERS)
        logger.debug('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_create_issue_mutation_vars")
